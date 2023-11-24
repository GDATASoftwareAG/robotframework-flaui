from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import ToggleButton
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class ToggleButtonKeywords:
    """
    Interface implementation from robotframework usage for checkbox keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for checkbox keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def toggle(self, identifier, msg=None):
        """
        Toggle given element.

        If pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Toggle  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TOGGLEBUTTON, msg=msg)
        return module.action(ToggleButton.Action.TOGGLE,
                             ToggleButton.create_value_container(element=element),
                             msg)
