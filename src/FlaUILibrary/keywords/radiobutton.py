from robotlibcore import keyword
from FlaUILibrary.flaui.interface import InterfaceType
from FlaUILibrary.flaui.module import ToggleButton


class RadioButtonKeywords:
    """
    Interface implementation from robotframework usage for radio button keywords.
    """

    def __init__(self, module):
        """
        Constructor for radiobutton keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def select_radiobutton(self, identifier, msg=None):
        """
        Select given radiobutton by xpath.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Select Radiobutton  <XPATH> |

        """
        element = self._module.get_element(identifier, InterfaceType.RADIOBUTTON, msg=msg)
        self._module.action(ToggleButton.Action.SET_TOGGLE_BUTTON_STATE,
                            self._create_value_container(element=element, state=True),
                            msg)

    @keyword
    def get_radiobutton_state(self, identifier, msg=None):
        """
        Return actual state ${True} or ${False} from radiobutton.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${value}  Get Radiobutton State <XPATH> |
        | Should Be Equal  ${value}  ${False/True} |

        """
        element = self._module.get_element(identifier, InterfaceType.RADIOBUTTON, msg=msg)
        return self._module.action(ToggleButton.Action.GET_TOGGLE_BUTTON_STATE,
                                   self._create_value_container(element=element),
                                   msg)

    @staticmethod
    def _create_value_container(element=None, state=None):
        """
        Helper to create container object.
        """
        return ToggleButton.Container(element=element,
                                      state=None if not state else bool(state))
