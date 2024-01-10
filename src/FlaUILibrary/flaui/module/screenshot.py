import os
import copy
import platform
import time
from enum import Enum
from FlaUI.Core.Capturing import Capture  # pylint: disable=import-error
from System import Exception as CSharpException  # pylint: disable=import-error
from FlaUILibrary.flaui.enum import ScreenshotMode
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
        mode: ScreenshotMode
        keywords: list

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        CAPTURE = "CAPTURE"
        RESET = "RESET"
        DELETE_ALL_SCREENSHOTS = "DELETE_ALL_SCREENSHOTS"
        SET_WHITELIST = "SET_WHITELIST"
        SET_BLACKLIST = "SET_BLACKLIST"
        CLEAR_WHITELIST = "CLEAR_WHITELIST"
        CLEAR_BLACKLIST = "CLEAR_BLACKLIST"

    def __init__(self, directory, is_enabled):
        """
        Creates screenshot module to capture desktop or element images by an error.

        ``directory`` Directory to store captured images. If not set log path will be used from robot by default.
        """
        self.is_enabled = is_enabled
        self.directory = directory
        self.whitelist = []
        self.blacklist = []
        self.name = ""
        self._temp_index = 1
        self._persist_index = 1
        self._hostname = platform.node().lower()
        self._filename = "test_{}_{}_{}_{}.jpg"
        self._temp_screenshots = []
        self._max_retry = 3
        self._sleep = 2  # Sleep in seconds

    @staticmethod
    def create_value_container(mode=ScreenshotMode.TEMP, keywords=None):
        """
        Helper to create container object.

        Args:
            mode (ScreenshotMode): Enum to persist screenshot or to create only as temp and delete if test was success.
            keywords (list): List from all blacklisted or whitelisted keywords.
        """
        if keywords is None:
            keywords = []

        return Screenshot.Container(mode=mode, keywords=keywords)

    def execute_action(self, action: Action, values: ValueContainer):
        """
        Get action method to execute a specific method by implementation.

        * Action.CAPTURE
              * Values : ["persist"]
              * Returns : None

        * Action.SET_WHITELIST || SET_BLACKLIST || CLEAR_WHITELIST || CLEAR_BLACKLIST
              * Values : ["keywords"]
              * Returns : None

        * Action.RESET || DELETE_ALL_SCREENSHOTS
              * Values : None
              * Returns : None

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.CAPTURE: lambda: self._capture(values["mode"]),
            self.Action.RESET: lambda: self._reset_temp_screenshots(),
            self.Action.DELETE_ALL_SCREENSHOTS: lambda: self._remove_all_created_screenshots(),
            self.Action.SET_WHITELIST: lambda : self._set_whitelist(values["keywords"]),
            self.Action.SET_BLACKLIST: lambda: self._set_blacklist(values["keywords"]),
            self.Action.CLEAR_WHITELIST: lambda: self._set_whitelist(values["keywords"]),
            self.Action.CLEAR_BLACKLIST: lambda: self._set_blacklist(values["keywords"]),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _set_whitelist(self, keywords: list):
        """
        Sets whitelist to screenshot module.
        """
        self.whitelist = keywords

    def _set_blacklist(self, keywords: list):
        """
        Sets blacklist to screenshot module.
        """
        self.blacklist = keywords

    def _capture(self, mode: ScreenshotMode):
        """
        Capture image from desktop.
        """
        image = None

        try:
            if mode == ScreenshotMode.PERSIST:
                filepath = os.path.join(self._get_path(), self._filename.format(self._clean_invalid_windows_syntax(
                                                                                    self._hostname),
                                                                                self._clean_invalid_windows_syntax(
                                                                                    self.name),
                                                                                self._get_current_time_in_ms(),
                                                                                self._persist_index))
            elif mode == ScreenshotMode.TEMP:
                filepath = os.path.join(self._get_path(), self._filename.format(self._clean_invalid_windows_syntax(
                                                                                    self._hostname),
                                                                                self._clean_invalid_windows_syntax(
                                                                                    self.name),
                                                                                self._get_current_time_in_ms(),
                                                                                self._temp_index))
            else:
                return

            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)

            try:
                image = Capture.Screen()
                image.ToFile(filepath)

                # Log screenshot from temp or persist mode
                robotlog.log_screenshot(filepath)

                # Store temp failed tests
                if mode == ScreenshotMode.TEMP:
                    self._temp_screenshots.append(filepath)

            except CSharpException:
                robotlog.log("Error to save image " + filepath)

        finally:
            if mode == ScreenshotMode.PERSIST:
                self._persist_index += 1
            else:
                self._temp_index += 1

            if image is not None:
                # C# --> class CaptureImage : IDisposable
                image.Dispose()

        return filepath

    def _get_path(self):
        """
        Get directory path for logging.
        """
        output_dir = robotlog.get_log_directory().replace("/", os.sep)

        if self.directory is not None:
            return os.path.join(output_dir, self.directory).replace("/", os.sep)

        return output_dir

    def _remove_all_created_screenshots(self):
        """
        Remove all created image files.

        Returns:
            True if all files are deleted otherwise False
        """
        for file in copy.copy(self._temp_screenshots):
            if self._remove_file(file):
                self._temp_screenshots.remove(file)

        if not self._temp_screenshots:
            return True

        return False

    def _remove_file(self, file: str):
        """
        Try to remove file. Retry operation for each file deletion is maximum three times.

        Args:
            file (String) : Filepath to delete.

        Returns:
            True if file is removed otherwise False
        """
        repeat_counter = 0
        while repeat_counter < self._max_retry:
            try:
                os.remove(file)
                return True
            except OSError:
                time.sleep(self._sleep)
            repeat_counter += 1

        return False

    def _reset_temp_screenshots(self):
        """
        Reset temp screenshots parameter.
        """
        self._temp_index = 1
        self._temp_screenshots.clear()

    @staticmethod
    def _clean_invalid_windows_syntax(filename, special_characters="\"|%:/,.\\[]<>*?"):
        return ''.join([c for c in filename if c not in special_characters])

    @staticmethod
    def _get_current_time_in_ms():
        return int(time.time() * 1000)
