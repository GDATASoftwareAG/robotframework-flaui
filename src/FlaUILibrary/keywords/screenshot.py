from robot.utils import is_truthy
from robotlibcore import keyword
from FlaUILibrary.flaui.module.screenshot import Screenshot
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
    def get_screenshot_log_mode(self):
        """Returns the current logging mode of the screenshot module. Default is 'File'.

        Example:
        | ${log_mode} = | Get Screenshot Log Mode |
        """
        return self._screenshots.get_mode()

    @keyword
    def set_screenshot_log_mode(self, log_mode: str):
        """Sets the logging mode of the screenshot module. Default is 'File'.
        Mode 'File' logs screenshots as files in the screenshot directory.
        Mode 'Base64' logs screenshots as base64 encoded strings embedded in the test report.

        Arguments:
        | Argument      | Type   | Description          |
        | log_mode      | string | File | Base64        |

        Example:
        | Set Screenshot Log Mode    Base64 |
        """
        self._screenshots.set_mode(log_mode)

    @keyword
    def take_screenshot(self, identifier=None, msg=None):
        """ Takes a screenshot of the whole desktop or the element, from the optionally provided identifier. 
        Returns screenshot depending on log mode.
        Screenshot mode File -> returns filepath
        Screenshot mode Base64 -> returns encoded base64 string of image

        Arguments:
        | Argument      | Type   | Description          |
        | identifier    | string | XPath identifier from element |
        | msg           | string | Custom error message          |

        Example:
        | Take Screenshot |
        | Take Screenshot   <XPATH> |
        | Take Screenshot   <XPATH>    "Your custom error message" |
        """
        image_var = None
        if identifier:
            module = self._container.create_or_get_module()
            element = module.get_element(identifier, msg=msg)
            image_var = self._screenshots.execute_action(Screenshot.Action.CAPTURE_ELEMENT,
                                                    Screenshot.create_value_container(element=element))
        else:
            image_var = self._screenshots.execute_action(Screenshot.Action.CAPTURE,
                                                    Screenshot.create_value_container())

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
