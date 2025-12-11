from robotlibcore import keyword
from FlaUILibrary.flaui.enum.interfacetype import InterfaceType
from FlaUILibrary.flaui.module.window import Window
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class WindowKeywords:
    """
    Interface implementation from robotframework usage for window keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for window keywords.

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
        element = module.get_element(identifier=identifier, ui_type=InterfaceType.WINDOW, msg=msg)
        module.action(Window.Action.CLOSE_WINDOW,
                      Window.create_value_container(element=element),
                      msg)

    @keyword
    def resize_window(self, identifier, width: int, height: int, msg=None):
        """
        Try to resize window from element to given width and height.

        Arguments:
        | Argument   | Type   | Description                             |
        | identifier | string | XPath identifier from element to search |
        | width      | int    | New width of the window                  |
        | height     | int    | New height of the window                 |
        | msg        | string | Custom error message                     |

        Example:
        | Launch Application  <APPLICATION>                  |
        | Resize Window  <XPATH_TO_APP_WINDOW>  1024  768     |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier=identifier, ui_type=InterfaceType.WINDOW, msg=msg)
        module.action(Window.Action.RESIZE_WINDOW,
                      Window.create_value_container(element=element, width=width, height=height),
                      msg)
