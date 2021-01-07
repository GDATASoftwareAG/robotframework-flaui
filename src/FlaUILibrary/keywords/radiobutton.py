from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.module import (ToggleButton, Element)


class RadioButtonKeywords:
    """
    Interface implementation from robotframework usage for radio button keywords.
    """

    def __init__(self, module):
        """Constructor for radiobutton keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def select_radiobutton(self, identifier, msg=None):
        """Select given radiobutton by xpath.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Select Radiobutton  <XPATH> |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        self._module.action(ToggleButton.Action.SET_TOGGLE_BUTTON_STATE,
                            [self._module.cast_element_to_type(element, InterfaceType.RADIOBUTTON), True],
                            msg)

    @keyword
    def get_radiobutton_state(self, identifier, msg=None):
        """Return actual  state ${True} or ${False} from radiobutton.

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
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        return self._module.action(ToggleButton.Action.GET_TOGGLE_BUTTON_STATE,
                                   [self._module.cast_element_to_type(element, InterfaceType.RADIOBUTTON)],
                                   msg)
