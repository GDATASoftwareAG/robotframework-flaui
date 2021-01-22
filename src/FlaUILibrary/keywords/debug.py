from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.module import (Debug, Element)


class DebugKeywords:
    """
    Interface implementation from robotframework usage for debugging keywords.
    """

    def __init__(self, module):
        """Constructor for debugging keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def get_childs_from_element(self, identifier, msg=None):
        """Gets full output from element and childs output. Information to print out are AutomationId, Name,
        ControlType and FrameworkId.

        Example output ${CHILDS}  <XPATH>:
          AutomationId:, Name:Warning, ControlType:dialog, FrameworkId:Win32
          ------> AutomationId:, Name:Warning, ControlType:pane, FrameworkId:Win32
          ------> AutomationId:1002, Name:, ControlType:document, FrameworkId:Win32
          ------> AutomationId:1, Name:OK, ControlType:button, FrameworkId:Win32
          ------> AutomationId:1009, Name:Do not display further messages, ControlType:check box, FrameworkId:Win32
          ------> AutomationId:1011, Name:Web protection, ControlType:text, FrameworkId:Win32

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${CHILDS}  Get Child From Element  <XPATH> |
        | Log  <XPATH> |

        """
        return self._module.action(Debug.Action.GET_CHILDS_FROM_ELEMENT,
                                   self._module.action(Element.Action.GET_ELEMENT, identifier, msg))

    @keyword
    def get_uia_identifier(self):
        """Gets given windows user automation identifier which is in usage for the test.

        Possible Identifier are : UIA2 or UIA3

        Examples:
        | ${IDENTIFIER}  Get UIA Identifier  |
        | Log  <IDENTIFIER> |
        """
        return self._module.identifier()
