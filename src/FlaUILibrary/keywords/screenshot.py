from robot.utils import is_truthy
from robotlibcore import keyword
from FlaUILibrary.flaui.module.screenshot import Screenshot
from FlaUILibrary.robotframework import robotlog


class ScreenshotKeywords:
    """
    Interface implementation from Robotframework usage for screenshot keywords.
    """

    def __init__(self, screenshots: Screenshot):
        """Creates screenshot keywords module to handle image capturing.

        ``screenshots`` Screenshots module for image capturing.
        """
        self._screenshots = screenshots

    @keyword
    def take_screenshot(self):
        """ Takes a screenshot of the whole desktop. Returns path to the screenshot if screenshot was created.

        Example:
        | Take Screenshot |
        """
        filepath = self._screenshots.execute_action(Screenshot.Action.CAPTURE,
                                                    Screenshot.create_value_container())

        if filepath:
            robotlog.log_screenshot(filepath)

        return filepath

    @keyword
    def take_screenshots_on_failure(self, enabled):
        """
        Takes a screenshot of the whole desktop if no element is attached otherwise attached element will be captured.
        Returns path to the screenshot file.

        Arguments:
        | Argument   | Type   | Description      |
        | enabled    | string | True or False    |

        Example:
        | Take Screenshots On Failure  ${FALSE/TRUE} |
        """
        if is_truthy(enabled):
            self._screenshots.is_enabled = True
        else:
            self._screenshots.is_enabled = False

    @keyword
    def set_screenshot_directory(self, directory=None):
        """
        Set directory for captured images. If no directory is set default output directory will be used from robot.

        Arguments:
        | Argument   | Type   | Description                                  |
        | directory | string | Relative or absolute path to directory folder |

        Example:
        | Set Screenshot Directory  <STRING_PATH> |
        """
        self._screenshots.directory = directory
