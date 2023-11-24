from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import Window
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class WindowKeywords:
    """
    Interface implementation from robotframework usage for window keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for mouse keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def close_window(self, identifier, msg=None):
        """
        Try to close window from element.

        Arguments:
        | Argument   | Type   | Description                             |
        | identifier | string | XPath identifier from element to search |
        | msg        | string | Custom error message                    |

        Example:
        | Launch Application  <APPLICATION>           |
        | Close Window  <XPATH_TO_APPLICATION_WINDOW> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.WINDOW, msg=msg)
        module.action(Window.Action.CLOSE_WINDOW,
                      Window.Container(element=element),
                      msg)
