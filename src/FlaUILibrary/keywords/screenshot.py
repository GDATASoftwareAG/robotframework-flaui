from robot.utils import is_truthy
from robotlibcore import keyword
from FlaUILibrary.flaui.module.screenshot import Screenshot
from FlaUILibrary.robotframework import robotlog
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer

class ScreenshotKeywords:
    """
    Interface implementation from Robotframework usage for screenshot keywords.
    """

    def __init__(self, screenshots: Screenshot, container: AutomationInterfaceContainer):
        """Creates screenshot keywords module to handle image capturing.

        ``screenshots`` Screenshots module for image capturing
        ``container`` User automation container to handle element interaction
        """
        self._screenshots = screenshots
        self._container = container

    @keyword
    def set_screenshot_log_mode(self, log_mode: str):
        self._screenshots.set_mode(log_mode)

    @keyword
    def take_screenshot(self, identifier=None, msg=None):
        """ Takes a screenshot of the whole desktop. Returns screenshot depending on log mode (File -> filepath, Base64 -> encoded string).

        Arguments:
        | Argument      | Type   | Description          |
        | identifier    | string | XPath identifier from element |
        | msg           | string | Custom error message          |

        Example:
        | Take Screenshot |
        """
        image_var = None
        if identifier:
            module = self._container.create_or_get_module()
            element = module.get_element(identifier, None, msg)
            image_var = self._screenshots.execute_action(Screenshot.Action.CAPTURE_ELEMENT,
                                                    Screenshot.create_value_container(element))
        else:
            image_var = self._screenshots.execute_action(Screenshot.Action.CAPTURE,
                                                    Screenshot.create_value_container())

        if image_var:
            if self._screenshots._mode == Screenshot.ScreenshotMode.BASE64:
                robotlog.log_screenshot_base64(image_var)
            else:
                robotlog.log_screenshot(image_var)

        return image_var

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
