import os
import platform
import time
from enum import Enum
from typing import Any, Union
from FlaUI.Core.Capturing import Capture  # pylint: disable=import-error
from System import Exception as CSharpException  # pylint: disable=import-error
from System import Convert as CSharpConvert  # pylint: disable=import-error
from System.IO import MemoryStream  # pylint: disable=import-error
from System.Drawing.Imaging import ImageFormat  # pylint: disable=import-error
from FlaUILibrary.flaui.util.automationelement import AutomationElement
from FlaUILibrary.flaui.util.converter import Converter
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
        keywords: list
        xpath: Union[str, AutomationElement]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        CAPTURE = "CAPTURE"
        CAPTURE_ELEMENT = "CAPTURE_ELEMENT"
        CAPTURE_BASE64 = "CAPTURE_BASE64"
        CAPTURE_ELEMENT_BASE64 = "CAPTURE_ELEMENT_BASE64"

    def __init__(self, directory, is_enabled, automation: Any):
        """
        Creates screenshot module to capture desktop or element images by an error.

        ``directory`` Directory to store captured images. If not set log path will be used from robot by default.
        """
        self.img_counter = 1
        self.is_enabled = is_enabled
        self.directory = directory
        self._name = ""
        self._hostname = self._clean_invalid_windows_syntax(platform.node().lower())
        self._filename = "test_{}_{}_{}_{}.jpg"
        self._automation = automation

    def set_name(self, name):
        """
        Set screenshot filename as lower text.
        Removes all invalid windows syntax and replace all empty characters into '_'

        Args:
            name (str): Filename to set.
        """
        self._name = self._clean_invalid_windows_syntax(name.replace(" ", "_").lower())

    @staticmethod
    def create_value_container(keywords=None, xpath=None):
        """
        Helper to create container object.

        Args:
            keywords (list): List from all blacklisted or whitelisted keywords.
        """
        if keywords is None:
            keywords = []

        return Screenshot.Container(keywords=keywords, xpath=Converter.cast_to_xpath_string(xpath))

    def execute_action(self, action: Action, values: ValueContainer):
        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.CAPTURE: lambda: self._capture(),
            self.Action.CAPTURE_ELEMENT: lambda: self._capture(xpath=values.xpath),
            self.Action.CAPTURE_BASE64: lambda: self._capture_base64(),
            self.Action.CAPTURE_ELEMENT_BASE64: lambda: self._capture_base64(xpath=values.xpath),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _capture(self, xpath=None):
        """
        Capture image from desktop.
        """
        image = None

        try:
            filepath = os.path.join(self._get_path(), self._filename.format(self._hostname,
                                                                            self._name,
                                                                            self._get_current_time_in_ms(),
                                                                            self.img_counter))

            directory = os.path.dirname(filepath)

            if not os.path.exists(directory):
                os.makedirs(directory)

            try:
                if xpath:
                    image = Capture.Element(self._automation.GetDesktop().FindFirstByXPath(xpath))
                else:
                    image = Capture.Screen()
                image.ToFile(filepath)

                # Log screenshot from temp or persist mode
                robotlog.log_screenshot(filepath)

            except CSharpException:
                robotlog.log("Error to save image " + filepath)

        finally:
            self.img_counter += 1
            if image is not None:
                # C# --> class CaptureImage : IDisposable
                image.Dispose()

        return filepath

    def _capture_base64(self, xpath=None):
        image = None

        try:
            if xpath:
                image = Capture.Element(self._automation.GetDesktop().FindFirstByXPath(xpath))
            else:
                image = Capture.Screen()
            stream = MemoryStream()
            image.Bitmap.Save(stream, ImageFormat.Png)
            base64 = CSharpConvert.ToBase64String(stream.GetBuffer())
            stream.Close()

            # Log screenshot from temp or persist mode
            robotlog.log_screenshot_base64(base64)

        except CSharpException:
            robotlog.log("Error to save image " + xpath)

        finally:
            self.img_counter += 1
            if image is not None:
                # C# --> class CaptureImage : IDisposable
                image.Dispose()

        return base64

    def _get_path(self):
        """
        Get directory path for logging.
        """
        output_dir = robotlog.get_log_directory().replace("/", os.sep)

        if self.directory is not None:
            return os.path.join(output_dir, self.directory).replace("/", os.sep)

        return output_dir

    @staticmethod
    def _clean_invalid_windows_syntax(filename, special_characters="\"|%:/,.\\[]<>*?"):
        return ''.join([c for c in filename if c not in special_characters])

    @staticmethod
    def _get_current_time_in_ms():
        return int(time.time() * 1000)
