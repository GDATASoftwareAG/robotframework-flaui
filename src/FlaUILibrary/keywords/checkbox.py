from robotlibcore import keyword
from FlaUILibrary.flaui.interface import InterfaceType
from FlaUILibrary.flaui.module import ToggleButton


class CheckBoxKeywords:
    """
    Interface implementation from robotframework usage for checkbox keywords.
    """

    def __init__(self, module):
        """
        Constructor for checkbox keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def set_checkbox_state(self, identifier, value, msg=None):
        """
        Set checkbox state to ${True} or ${False}

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | enable     | bool   | ${True} / ${False}            |
        | msg        | string | Custom error message          |

        Examples:
        | Set Checkbox State  <XPATH>  ${True/False} |

        """
        element = self._module.get_element(identifier, InterfaceType.CHECKBOX, msg)
        self._module.action(ToggleButton.Action.SET_TOGGLE_BUTTON_STATE,
                            ToggleButton.create_value_container(element=element, state=value),
                            msg)

    @keyword
    def get_checkbox_state(self, identifier, msg=None):
        """
        Return actual checked state ${True} or ${False} from checkbox.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${value}  Get Checkbox State  <XPATH> |
        | Should Be Equal  ${value}  ${False/True} |

        Returns:
        | <True> if checkbox is set otherwise <False> |

        """
        element = self._module.get_element(identifier, InterfaceType.CHECKBOX, msg)
        return self._module.action(ToggleButton.Action.GET_TOGGLE_BUTTON_STATE,
                                   ToggleButton.create_value_container(element=element),
                                   msg)
