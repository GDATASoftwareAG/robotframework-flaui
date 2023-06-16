import os
import copy
import platform
import time
from enum import Enum
from FlaUI.Core.Capturing import Capture  # pylint: disable=import-error
from System import Exception as CSharpException  # pylint: disable=import-error
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
        persist: bool

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        CAPTURE = "CAPTURE"
        RESET = "RESET"
        DELETE_ALL_SCREENSHOTS = "DELETE_ALL_SCREENSHOTS"

    def __init__(self, directory, is_enabled):
        """
        Creates screenshot module to capture desktop or element images by an error.

        ``directory`` Directory to store captured images. If not set log path will be used from robot by default.
        """
        self.is_enabled = is_enabled
        self.directory = directory
        self.name = ""
        self._temp_index = 1
        self._persist_index = 1
        self._hostname = platform.node().lower()
        self._filename = "test_{}_{}_{}_{}.jpg"
        self._temp_screenshots = []
        self._max_retry = 3
        self._sleep = 2  # Sleep in seconds

    @staticmethod
    def create_value_container(persist=False):
        """
        Helper to create container object.

        Args:
            persist (bool): Flag to persist screenshot or to create only as temp and delete if test was success.
        """
        return Screenshot.Container(persist=persist)

    def execute_action(self, action: Action, values: ValueContainer):
        """
        Get action method to execute a specific method by implementation.

        * Action.CAPTURE
              * Values : ["persist"]
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
            self.Action.CAPTURE: lambda: self._capture(values["persist"]),
            self.Action.RESET: lambda: self._reset_temp_screenshots(),
            self.Action.DELETE_ALL_SCREENSHOTS: lambda: self._remove_all_created_screenshots()
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _capture(self, persist: bool):
        """
        Capture image from desktop.
        """
        image = None

        try:
            if persist:
                filepath = os.path.join(self._get_path(), self._filename.format(self._hostname,
                                                                                self.name,
                                                                                self._get_current_time_in_ms(),
                                                                                self._persist_index))
            else:
                filepath = os.path.join(self._get_path(), self._filename.format(self._hostname,
                                                                                self.name,
                                                                                self._get_current_time_in_ms(),
                                                                                self._temp_index))

            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)

            try:
                image = Capture.Screen()
                image.ToFile(filepath)
                if not persist:
                    robotlog.log_screenshot(filepath)
                    self._temp_screenshots.append(filepath)
            except CSharpException:
                robotlog.log("Error to save image " + filepath)

        finally:
            if persist:
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
    def _get_current_time_in_ms():
        return int(time.time() * 1000)
