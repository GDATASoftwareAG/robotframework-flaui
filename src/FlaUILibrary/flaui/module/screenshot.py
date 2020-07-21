import os
import copy
import platform
import time
from enum import Enum
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface
from FlaUILibrary.robotframework import robotlog
from FlaUI.Core.Capturing import Capture


class Screenshot(ModuleInterface):
    """Screenshot module wrapper for FlaUI usage."""

    class Action(Enum):
        """Enum declaration."""
        CAPTURE = "CAPTURE",
        RESET = "RESET",
        DELETE_ALL_SCREENSHOTS = "DELETE_ALL_SCREENSHOTS"

    def __init__(self, directory, is_enabled):
        """Creates screenshot module to capture desktop or element images by an error.

        ``directory`` Directory to store captured images. If not set log path will be used from robot by default.
        """
        self.is_enabled = is_enabled
        self.directory = directory
        self.name = ""
        self._index = 0
        self._hostname = platform.node().lower()
        self._filename = "test_{}_{}_{}.jpg"
        self._files = []
        self._max_retry = 3
        self._sleep = 2  # Sleep in seconds

    def execute_action(self, action, values=None):
        """Get action method to execute a specific method by implementation.

        Args:
            action (Action): Specific action to call for execution.
            values (Object): Parameter values to use for method execution.
        """

        switcher = {
            self.Action.CAPTURE: lambda: self._capture(),
            self.Action.RESET: lambda: self._reset(),
            self.Action.DELETE_ALL_SCREENSHOTS: lambda: self._remove_all_created_screenshots()
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _capture(self):
        """Capture image from desktop."""
        image = None

        try:
            image = Capture.Screen()
            self._index += 1

            filepath = os.path.join(self._get_path(), self._filename.format(self._hostname, self.name, self._index))
            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)

            try:
                image.ToFile(filepath)
            except:
                robotlog.log("Error to save image " + filepath)

            self._files.append(filepath)

        finally:
            if image is not None:
                """ C# --> class CaptureImage : IDisposable  """
                image.Dispose()

        return filepath

    def _get_path(self):
        """Get directory path if set if not by default fallback will be used to obtain log directory
           from robot test case.
        """
        output_dir = robotlog.get_log_directory().replace("/", os.sep)

        if self.directory is not None:
            return os.path.join(output_dir, self.directory).replace("/", os.sep)

        return output_dir

    def _remove_all_created_screenshots(self):
        """Remove all created image files.

        Returns:
            True if all files are deleted otherwise False
        """
        for file in copy.copy(self._files):
            if self._remove_file(file):
                self._files.remove(file)

        if not self._files:
            return True

        return False

    def _remove_file(self, file):
        """
        Try to remove file. Retry operation for each file deletion is maximum three times.

        Args:
            file (String) : Filepath to delete.

        Returns:
            True if file is removed otherwise False
        """
        for x in range(self._max_retry):
            try:
                os.remove(file)
                return True
            except:
                time.sleep(self._sleep)

        return False

    def _reset(self):
        """Reset mechanism for default parameter usage."""
        self._index = 0
        self._files.clear()
