from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import Textbox
from FlaUILibrary.flaui.automation.uia import UIA


class TextBoxKeywords:
    """
    Interface implementation from robotframework usage for textbox keywords.
    """

    def __init__(self, module: UIA):
        """
        Constructor for textbox keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def get_text_from_textbox(self, identifier, msg=None):
        """
        Return text from textbox element.

        XPaths syntax is explained in `XPath locator`.

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
        element = self._module.get_element(identifier, InterfaceType.TEXTBOX, msg=msg)
        return self._module.action(Textbox.Action.GET_TEXT_FROM_TEXTBOX,
                                   Textbox.create_value_container(element=element),
                                   msg=msg)

    @keyword
    def set_text_to_textbox(self, identifier, value, msg=None):
        """
        Inputs value to a textbox module.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from textbox |
        | value      | string | Value to set to textbox       |
        | msg        | string | Custom error message          |

        Examples:
        | Set Text To Textbox  <XPATH>  <VALUE> |

        """
        element = self._module.get_element(identifier, InterfaceType.TEXTBOX, msg=msg)
        self._module.action(Textbox.Action.SET_TEXT_TO_TEXTBOX,
                            Textbox.create_value_container(element=element, value=value),
                            msg)
