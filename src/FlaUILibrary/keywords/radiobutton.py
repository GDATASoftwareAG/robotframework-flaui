from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import Checkbox as Radio
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class RadioButtonKeywords:
    """
    Interface implementation from robotframework usage for radio button keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for radiobutton keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def select_radiobutton(self, identifier, msg=None):
        """
        Select given radiobutton by xpath.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Select Radiobutton  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.RADIOBUTTON, msg=msg)
        module.action(Radio.Action.SET_CHECKBOX_BUTTON_STATE,
                      self._create_value_container(element=element, state=True),
                      msg)

    @keyword
    def get_radiobutton_state(self, identifier, msg=None):
        """
        Return actual state ${True} or ${False} from radiobutton.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${value}  Get Radiobutton State <XPATH> |
        | Should Be Equal  ${value}  ${False/True} |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.RADIOBUTTON, msg=msg)
        return module.action(Radio.Action.GET_CHECKBOX_BUTTON_STATE,
                             self._create_value_container(element=element),
                             msg)

    @staticmethod
    def _create_value_container(element=None, state=None):
        """
        Helper to create container object.
        """
        return Radio.Container(element=element,
                               state=None if not state else bool(state))
