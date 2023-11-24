from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import Checkbox
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class CheckBoxKeywords:
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.CHECKBOX, msg)
        module.action(Checkbox.Action.SET_CHECKBOX_BUTTON_STATE,
                      Checkbox.create_value_container(element=element, state=value),
                      msg)

    @keyword
    def get_checkbox_state(self, identifier, msg=None):
        """
        Return actual checked state ${True} or ${False} from checkbox.

        XPaths syntax is explained in `XPath locator`.

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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.CHECKBOX, msg)
        return module.action(Checkbox.Action.GET_CHECKBOX_BUTTON_STATE,
                             Checkbox.create_value_container(element=element),
                             msg)
