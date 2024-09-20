from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer
from FlaUILibrary.flaui.module import Button


class ButtonKeywords:
    """
    Interface implementation from robotframework usage for element keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for element keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def invoke_button(self, identifier, msg=None):
        """
        Invokes the invokable element given by identifier.
        If button could not be found by xpath False will be returned.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element is not invokable |
        | Action not supported |

        Arguments:
        | Argument      | Type   | Description                   |
        | identifier    | string | XPath identifier from element |
        | msg           | string | Custom error message |

        Example:
        | Invoke Button  <XPATH>  msg=Custom error message |
       
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.BUTTON, msg)
        module.action(Button.Action.INVOKE_BUTTON,
                      Button.create_value_container(xpath=identifier, element=element),
                      msg)
