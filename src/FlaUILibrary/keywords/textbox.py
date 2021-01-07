from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.module import (Textbox, Element)


class TextBoxKeywords:
    """
    Interface implementation from robotframework usage for textbox keywords.
    """

    def __init__(self, module):
        """Constructor for textbox keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def get_text_from_textbox(self, identifier, msg=None):
        """Return text from textbox element.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | name       | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${TEXT}  Get Text From Textbox  <XPATH> |

        Returns:
        | Text string from textbox |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        return self._module.action(Textbox.Action.GET_TEXT_FROM_TEXTBOX,
                                   self._module.cast_element_to_type(element, InterfaceType.TEXTBOX),
                                   msg=msg)

    @keyword
    def set_text_to_textbox(self, identifier, value, msg=None):
        """Inputs value to a textbox module.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from textbox |
        | value      | string | Value to set to textbox       |
        | msg        | string | Custom error message          |

        Examples:
        | Set Text To Textbox  <XPATH>  <VALUE> |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        self._module.action(Textbox.Action.SET_TEXT_TO_TEXTBOX,
                            [self._module.cast_element_to_type(element, InterfaceType.TEXTBOX), value],
                            msg)
