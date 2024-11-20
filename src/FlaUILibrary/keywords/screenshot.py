from robotlibcore import keyword
from FlaUILibrary.flaui.module.screenshot import Screenshot
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class ScreenshotKeywords:
    """
    Interface implementation from Robotframework usage for screenshot keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer, directory: str, is_enabled: bool):
        """Creates screenshot keywords module to handle image capturing.

        ``container`` User automation container to handle element interaction
        """
        self._container = container
        self.set_screenshot_directory(directory)
        self.take_screenshots_on_failure(is_enabled)

    @keyword
    def get_screenshot_log_mode(self):
        """Returns the current logging mode of the screenshot module. Default is 'File'.

        Example:
        | ${log_mode}  Get Screenshot Log Mode |
        """
        module = self._container.create_or_get_module()
        return module.action(Screenshot.Action.GET_MODE, Screenshot.create_value_container())

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
        module = self._container.create_or_get_module()
        module.action(Screenshot.Action.SET_MODE, Screenshot.create_value_container(mode=log_mode))

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
        module = self._container.create_or_get_module()
        if identifier:
            element = module.get_element(identifier, msg=msg)
            image = module.action(Screenshot.Action.CAPTURE_ELEMENT,
                                  Screenshot.create_value_container(element=element))
        else:
            image = module.action(Screenshot.Action.FORCE_CAPTURE, Screenshot.create_value_container())

        return image

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
        module = self._container.create_or_get_module()
        module.action(Screenshot.Action.SET_ENABLED_TO, Screenshot.create_value_container(enabled=enabled))

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
        module = self._container.create_or_get_module()
        module.action(Screenshot.Action.SET_DIRECTORY, Screenshot.create_value_container(directory=directory))
