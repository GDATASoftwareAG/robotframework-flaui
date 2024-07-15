from robot.utils import is_truthy
from robotlibcore import keyword
from FlaUILibrary.flaui.module.screenshot import Screenshot
from FlaUILibrary.robotframework import robotlog


class ScreenshotKeywords:
    """
    Interface implementation from Robotframework usage for screenshot keywords.
    """

    class ScreenshotType(Enum):
        FILE = "FILE"
        BASE64 = "BASE64"

    def __init__(self, screenshots: Screenshot):
        """Creates screenshot keywords module to handle image capturing.

        ``screenshots`` Screenshots module for image capturing.
        """
        self._screenshots = screenshots

    @keyword
    def take_screenshot(self, base64 = False):
        """ Takes a screenshot of the whole desktop. Returns path of screenshot created if ``base64`` is False (default).
        Otherwise returns base64 encoded string of screenshot image.

        Arguments:
        | Argument      | Type   | Description          |
        | base64        | string | True or False        |

        Example:
        | Take Screenshot |
        """
        image_var = None

        if is_truthy(base64):
            image_var = self._screenshots.execute_action(Screenshot.Action.CAPTURE_BASE64,
                                                            Screenshot.create_value_container())
            if image_var:
                robotlog.log_screenshot_base64(image_var)
        else:
            image_var = self._screenshots.execute_action(Screenshot.Action.CAPTURE if,
                                                        Screenshot.create_value_container())
            if image_var:
                robotlog.log_screenshot(image_var)

        return image_var

    @keyword
    def take_screenshot_from_element(self, element, base64 = False):
        """ Takes a screenshot of the identified application window. Returns path of screenshot created.
        
        Arguments:
        | Argument      | Type   | Description          |
        | element       | string | XPath identifier from element |
        | base64        | string | True or False        |

        Example:
        | Take Screenshot From Element   <XPATH>|
        """
        image_var = None

        if is_truthy(base64):
            image_var = self._screenshots.execute_action(Screenshot.Action.CAPTURE_BASE64,
                                                            Screenshot.create_value_container(xpath=element))
            if image_var:
                robotlog.log_screenshot_base64(image_var)
        else:
            image_var = self._screenshots.execute_action(Screenshot.Action.CAPTURE if,
                                                        Screenshot.create_value_container(xpath=element))
            if image_var:
                robotlog.log_screenshot_base64(image_var)

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
