from robotlibcore import keyword
from FlaUILibrary.flaui.interface import InterfaceType
from FlaUILibrary.flaui.module import Window


class WindowKeywords:
    """
    Interface implementation from robotframework usage for window keywords.
    """

    def __init__(self, module):
        """
        Constructor for mouse keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

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
        element = self._module.get_element(identifier, InterfaceType.WINDOW, msg=msg)
        self._module.action(Window.Action.CLOSE_WINDOW,
                            Window.Container(element=element),
                            msg)
