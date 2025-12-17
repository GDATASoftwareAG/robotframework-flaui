import os
import time
from enum import Enum
from typing import Any, Optional
from FlaUI.Core.Capturing import Capture  # pylint: disable=import-error
from System import Exception as CSharpException  # pylint: disable=import-error
from System import Convert as CSharpConvert  # pylint: disable=import-error
from System.IO import MemoryStream  # pylint: disable=import-error
from System.Drawing.Imaging import ImageFormat  # pylint: disable=import-error
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.robotframework import robotlog


# pylint: disable=too-many-instance-attributes
class Screenshot(ModuleInterface):
    """
    Screenshot module wrapper for FlaUI usage.
    Wrapper module executes methods from Capture.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from screenshot module.
        """
        element: Optional[Any]
        enabled: Optional[bool]
        mode: Optional[str]
        directory: Optional[str]
        name: Optional[str]
        suffix: Optional[str]
        force: Optional[bool]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        CAPTURE = "SCREENSHOT_CAPTURE"
        FORCE_CAPTURE = "SCREENSHOT_FORCE_CAPTURE"
        CAPTURE_ELEMENT = "SCREENSHOT_CAPTURE_ELEMENT"
        IS_ENABLED = "SCREENSHOT_IS_ENABLED"
        SET_ENABLED_TO = "SCREENSHOT_SET_ENABLED_TO"
        SET_MODE = "SCREENSHOT_SET_MODE"
        GET_MODE = "SCREENSHOT_GET_MODE"
        SET_DIRECTORY = "SCREENSHOT_SET_DIRECTORY"
        SET_NAME = "SCREENSHOT_SET_NAME"
        SET_FILE_SUFFIX = "SCREENSHOT_SET_FILE_SUFFIX"

    class ScreenshotMode(Enum):
        """
        Supported modes for screenshots.
        """
        FILE = "File"
        BASE64 = "Base64"

    def __init__(self):
        """
        Creates screenshot module to capture desktop or element images by an error.
        """
        self._img_counter = 1
        self._is_enabled = True
        self._directory = None
        self._hostname = self._clean_invalid_windows_syntax(os.environ.get('COMPUTERNAME').lower())
        self._suffix = "jpg"
        self._filename = "test_{}_{}_{}.{}"
        self._name = ""
        self._mode = self.ScreenshotMode.FILE

    @staticmethod
    def create_value_container(element=None,
                               enabled=None,
                               mode=None,
                               directory=None,
                               name=None,
                               suffix=None,
                               force=None) -> Container:
        """
        Helper to create container object.

        Args:
            element (Object): UIA2 or UIA3 element to screenshot
            enabled (bool): True to enable screenshot, False to disable screenshot.
            mode (string): Mode to capture screenshot for Base64 or Image capturing.
            directory (string): Directory to capture screenshot.
            name (string): Additional name of screenshot. Will be used to capture test name.
            suffix (string): Additional suffix of screenshot filetype.
            force (bool): True to force screenshot capturing even if disabled.
        """
        return Screenshot.Container(element=element,
                                    enabled=enabled,
                                    mode=mode,
                                    directory=directory,
                                    name=name,
                                    suffix=suffix,
                                    force=Converter.cast_to_bool(force))

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.FORCE_CAPTURE:
                lambda: self._capture(values),
            self.Action.CAPTURE:
                lambda: self._capture(values),
            self.Action.CAPTURE_ELEMENT:
                lambda: self._capture(values),
            self.Action.IS_ENABLED:
                lambda: self._is_screenshot_enabled(),
            self.Action.SET_ENABLED_TO:
                lambda: self._set_enabled_to(values),
            self.Action.SET_MODE:
                lambda: self._set_mode(values),
            self.Action.GET_MODE:
                lambda: self._get_mode(),
            self.Action.SET_DIRECTORY:
                lambda: self._set_directory(values),
            self.Action.SET_NAME:
                lambda: self._set_name(values),
            self.Action.SET_FILE_SUFFIX:
                lambda: self._set_file_suffix(values)
        }
        # pylint: enable=unnecessary-lambda

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _is_screenshot_enabled(self) -> bool:
        """
        Return whether the screenshot module is currently enabled.

        Returns:
            bool: True when screenshot capturing is enabled, False otherwise.
        """
        return self._is_enabled

    def _set_name(self, container: Container) -> None:
        """
        Set a sanitized name fragment to include in generated screenshot filenames.

        The provided name will have whitespace converted to underscores and any
        invalid Windows filename characters removed.

        Args:
            container (Screenshot.Container): Container holding:
                - container['name']: Name string to include in the filename.
        """
        name = container['name']
        self._name = self._clean_invalid_windows_syntax(name.replace(" ", "_").lower())

    def _set_directory(self, container: Container) -> None:
        """
        Configure an additional relative directory under the test log directory
        where screenshots should be written.

        Args:
            container (Screenshot.Container): Container holding:
                - container['directory']: Relative directory path (string).
        """
        directory = container['directory']
        self._directory = directory

    def _set_file_suffix(self, container: Container) -> None:
        """
        Set the file suffix (extension) to use for screenshot files.

        Args:
            container (Screenshot.Container): Container holding:
                - container['suffix']: File suffix without a leading dot (e.g., 'png' or 'jpg').
        """
        suffix = container['suffix']
        self._suffix = suffix

    def _set_mode(self, container: Container) -> None:
        """
        Set the screenshot output mode.

        Supported modes (case-insensitive):
            - 'FILE'   : Save screenshots to files and return file paths.
            - 'BASE64' : Return screenshots as Base64-encoded PNG strings.

        Args:
            container (Screenshot.Container): Container holding:
                - container['mode']: Mode name (string).

        Raises:
            FlaUiError: If an unsupported mode is provided.
        """
        mode = container['mode']

        if mode.upper() == 'FILE':
            self._mode = self.ScreenshotMode.FILE
        elif mode.upper() == 'BASE64':
            self._mode = self.ScreenshotMode.BASE64
        else:
            FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported)

    def _get_mode(self) -> ScreenshotMode:
        """
        Return the currently configured screenshot mode.

        Returns:
            Screenshot.ScreenshotMode: Current mode enum value.
        """
        return self._mode

    def _set_enabled_to(self, container: Container) -> None:
        """
        Enable or disable the screenshot module.

        When disabled, captures are skipped unless the call uses the 'force' flag.

        Args:
            container (Screenshot.Container): Container holding:
                - container['enabled']: Boolean to enable (True) or disable (False).
        """
        enabled = container['enabled']
        self._is_enabled = enabled

    def _capture(self, container: Container) -> Optional[str]:
        """
        Capture a screenshot for the given element or the full screen, depending on
        the configured mode and the provided container values.

        Behavior:
            - If module is disabled and not forced, returns None.
            - In FILE mode: saves an image file and returns the file path.
            - In BASE64 mode: returns a Base64 PNG string.

        Args:
            container (Screenshot.Container): Container holding:
                - container['element']: Optional UI element to capture.
                - container['force']: Optional bool to force capture even if disabled.

        Returns:
            str | None: File path (FILE), Base64 string (BASE64), or None (not captured).

        Raises:
            FlaUiError: If an invalid screenshot mode is configured.
        """
        element = container['element']
        force_screenshot = container['force']

        if not force_screenshot and not self._is_enabled:
            return None

        if self._mode == self.ScreenshotMode.FILE:
            return self._capture_file(element)

        if self._mode == self.ScreenshotMode.BASE64:
            return self._capture_base64(element)

        raise FlaUiError("Invalid screenshot mode selected. Available modes: "
                         + '\n'.join([str(mode) for mode in self.ScreenshotMode]))

    def _capture_file(self, element: Any) -> str:
        """
        Capture an image and save it to a file.

        The file path is constructed from the configured hostname, name fragment,
        a timestamp, and the configured suffix. The file is logged via robotlog.

        Args:
            element (Any): UI element to capture, or None to capture the full screen.

        Returns:
            str: Absolute path to the saved image file.

        Raises:
            FlaUiError: If saving the image fails.
        """
        image = None

        directory = self._get_path()
        filepath = os.path.join(directory,
                                self._filename.format(
                                    self._hostname,
                                          self._name,
                                          self._get_current_time_in_ms(),
                                          self._suffix
                                ))

        if not os.path.exists(directory):
            os.makedirs(directory)

        try:
            if element:
                image = Capture.Element(element)
            else:
                image = Capture.Screen()

            image.ToFile(filepath)

            # Log screenshot from temp or persist mode
            robotlog.log_screenshot(filepath)
        except CSharpException as exc:
            raise FlaUiError("Error to save image " + filepath) from exc
        finally:
            self._img_counter += 1
            if image is not None:
                # C# --> class CaptureImage : IDisposable
                image.Dispose()

        return filepath

    def _capture_base64(self, element: Any) -> str:
        """
        Capture an image and return it as a Base64-encoded PNG string.

        The captured image is converted to a PNG and encoded using the .NET
        Convert.ToBase64String API. The Base64 string is logged via robotlog.

        Args:
            element (Any): UI element to capture, or None to capture the full screen.

        Returns:
            str: Base64-encoded PNG image string.

        Raises:
            FlaUiError: If conversion to Base64 fails.
        """
        image = None

        try:
            if element:
                image = Capture.Element(element)
            else:
                image = Capture.Screen()

            stream = MemoryStream()
            image.Bitmap.Save(stream, ImageFormat.Png)
            base64 = CSharpConvert.ToBase64String(stream.GetBuffer())
            stream.Close()

            # Log screenshot from temp or persist mode
            robotlog.log_screenshot_base64(base64)
            return base64
        except CSharpException as exc:
            raise FlaUiError("Error to save as base64 encoded string: " + element) from exc
        finally:
            self._img_counter += 1
            if image is not None:
                # C# --> class CaptureImage : IDisposable
                image.Dispose()

    def _get_path(self) -> str:
        """
        Compute the absolute directory path used for storing screenshots.

        If a custom relative directory was configured via _set_directory, it is
        appended to the Robot Framework log directory.

        Returns:
            str: Absolute path to the directory where screenshots are written.
        """
        output_dir = robotlog.get_log_directory().replace("/", os.sep)
        if self._directory:
            return str(os.path.join(output_dir, self._directory).replace("/", os.sep))

        return output_dir

    @staticmethod
    def _clean_invalid_windows_syntax(filename, special_characters="\"|%:/,.\\[]<>*?") -> str:
        """
        Remove characters that are not allowed in Windows filenames.

        Args:
            filename (str): Input string to sanitize.
            special_characters (str): Characters to remove from the filename.

        Returns:
            str: Sanitized filename with invalid characters removed.
        """
        return ''.join([c for c in filename if c not in special_characters])

    @staticmethod
    def _get_current_time_in_ms() -> int:
        """
        Return the current time in milliseconds since the epoch.

        Returns:
            int: Current time in milliseconds.
        """
        return int(time.time() * 1000)
