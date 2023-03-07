from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import ToggleButton
from FlaUILibrary.flaui.automation.uia import UIA


class ToggleButtonKeywords:
    """
    Interface implementation from robotframework usage for checkbox keywords.
    """

    def __init__(self, module: UIA):
        """
        Constructor for checkbox keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

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
        element = self._module.get_element(identifier, InterfaceType.TOGGLEBUTTON, msg=msg)
        return self._module.action(ToggleButton.Action.TOGGLE,
                                   ToggleButton.create_value_container(element=element),
                                   msg)
