from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.module import (Window, Element)


class WindowKeywords:
    """
    Interface implementation from robotframework usage for window keywords.
    """

    def __init__(self, module):
        """Constructor for mouse keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self.module = module

    @keyword
    def close_window(self, identifier, msg=None):
        """Try to close window from element.

        Arguments:
        | Argument   | Type   | Description                             |
        | identifier | string | XPath identifier from element to search |
        | msg        | string | Custom error message                    |

        Example:
        | Launch Application  <APPLICATION>           |
        | Close Window  <XPATH_TO_APPLICATION_WINDOW> |

        """
        element = self.module.action(Element.Action.GET_ELEMENT, identifier, msg)
        self.module.action(Window.Action.CLOSE_WINDOW,
                           self.module.cast_element_to_type(element, InterfaceType.WINDOW),
                           msg)
