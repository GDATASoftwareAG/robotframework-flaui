import os
import platform
import time
from enum import Enum
from typing import Any, Optional
from FlaUI.Core.Capturing import Capture  # pylint: disable=import-error
from System import Exception as CSharpException  # pylint: disable=import-error
from System import Convert as CSharpConvert  # pylint: disable=import-error
from System.IO import MemoryStream  # pylint: disable=import-error
from System.Drawing.Imaging import ImageFormat  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
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

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        CAPTURE = "CAPTURE"
        FORCE_CAPTURE = "FORCE_CAPTURE"
        CAPTURE_ELEMENT = "CAPTURE_ELEMENT"
        IS_ENABLED = "IS_ENABLED"
        SET_ENABLED_TO = "SET_ENABLED_TO"
        SET_MODE = "SET_MODE"
        GET_MODE = "GET_MODE"
        SET_DIRECTORY = "SET_DIRECTORY"
        SET_NAME = "SET_NAME"

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
        self._hostname = self._clean_invalid_windows_syntax(platform.node().lower())
        self._filename = "test_{}_{}_{}.jpg"
        self._name = ""
        self._mode = self.ScreenshotMode.FILE

    @staticmethod
    def create_value_container(element=None,
                               enabled=None,
                               mode=None,
                               directory=None,
                               name=None):
        """
        Helper to create container object.

        Args:
            element (Object): UIA2 or UIA3 element to screenshot
            enabled (bool): True to enable screenshot, False to disable screenshot.
            mode (string): Mode to capture screenshot for Base64 or Image capturing.
            directory (string): Directory to capture screenshot.
            name (string): Additional name of screenshot. Will be used to capture test name.
        """
        return Screenshot.Container(element=element, enabled=enabled, mode=mode, directory=directory, name=name)

    def execute_action(self, action: Action, values: ValueContainer):
        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.FORCE_CAPTURE: lambda: self._capture(element=values['element']),
            self.Action.CAPTURE: lambda: self._capture() if self._is_enabled else None,
            self.Action.CAPTURE_ELEMENT: lambda: self._capture(element=values['element'] if self._is_enabled else None),
            self.Action.IS_ENABLED: lambda: self._is_enabled,
            self.Action.SET_ENABLED_TO: lambda: self._set_enabled_to(values['enabled']),
            self.Action.SET_MODE: lambda: self._set_mode(values['mode']),
            self.Action.GET_MODE: lambda: self._get_mode(),
            self.Action.SET_DIRECTORY: lambda: self._set_directory(values['directory']),
            self.Action.SET_NAME: lambda: self._set_name(values['name'])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _set_name(self, name: str) -> None:
        """
        Set name from snapshot file to include. Will remove all whitespaces into underscores.

        Args:
            name (str): Additional name to include to screenshot.
        """
        self._name = self._clean_invalid_windows_syntax(name.replace(" ", "_").lower())

    def _set_directory(self, directory: str) -> None:
        """
        Set additional relative directory path to store snapshots.

        Args:
            directory (str): Relative path from directory.
        """
        self._directory = directory

    def _set_mode(self, mode: str):
        """
        Set screenshot logging mode. Available modes: File, Base64

        Args:
            mode (str): Screenshot mode to set.
        """
        if mode.upper() == 'FILE':
            self._mode = self.ScreenshotMode.FILE
        elif mode.upper() == 'BASE64':
            self._mode = self.ScreenshotMode.BASE64
        else:
            FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported)

    def _get_mode(self):
        """
        Return the configured screenshot logging mode.
        """
        return self._mode

    def _set_enabled_to(self, enabled: bool):
        """
        Enable or disable screenshot module.

        Args:
            enabled (bool): True to enable screenshot, False to disable screenshot.
        """
        self._is_enabled = enabled

    def _capture(self, element=None):
        """
        Capture desktop or element image as screenshot.

        If mode is File -> Filepath will be returned.
        If mode is Base64 -> Base64 string will be returned.

        Args:
            element (Object): UIA2 or UIA3 element to screenshot.

        Raises:
            FlaUiError: If mode is not supported.
        """
        if self._mode == self.ScreenshotMode.FILE:
            return self._capture_file(element)
        if self._mode == self.ScreenshotMode.BASE64:
            return self._capture_base64(element)

        raise FlaUiError("Invalid screenshot mode selected. Available modes: "
                         + '\n'.join([str(mode) for mode in self.ScreenshotMode]))

    def _capture_file(self, element=None):
        """
        Capture image from desktop or element as screenshot in file.

        Args:
            element (Object): UIA2 or UIA3 element to screenshot.

        Raises:
            FlaUiError: If image could not be saved.
        """
        image = None

        directory = self._get_path()
        filepath = os.path.join(directory, self._filename.format(self._hostname,
                                                                 self._name,
                                                                 self._get_current_time_in_ms()))

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

    def _capture_base64(self, element=None):
        """
        Capture image from desktop or element as screenshot as base64.

        Args:
            element (Object): UIA2 or UIA3 element to screenshot.

        Raises:
            FlaUiError: If image could not be created as base64.
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

    def _get_path(self):
        """
        Get directory path for logging.
        """
        output_dir = robotlog.get_log_directory().replace("/", os.sep)
        if self._directory:
            return os.path.join(output_dir, self._directory).replace("/", os.sep)

        return output_dir

    @staticmethod
    def _clean_invalid_windows_syntax(filename, special_characters="\"|%:/,.\\[]<>*?"):
        return ''.join([c for c in filename if c not in special_characters])

    @staticmethod
    def _get_current_time_in_ms():
        return int(time.time() * 1000)
