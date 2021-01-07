from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.module import (Tab, Element)


class TabKeywords:
    """
    Interface implementation from robotframework usage for tab keywords.
    """

    def __init__(self, module):
        """Constructor for tab keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def get_tab_items_names(self, identifier, msg=None):
        """Return child TabItems names from the parent Tab element.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | @{CHILD_TAB_ITEMS}  Get Tab Items Names  <XPATH> |

        Returns:
        | List<String> child TabItem elements names from the Tab element. |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        return self._module.action(Tab.Action.GET_TAB_ITEMS_NAMES,
                                   [self._module.cast_element_to_type(element, InterfaceType.TAB)],
                                   msg)

    @keyword
    def select_tab_item_by_name(self, identifier, name, msg=None):
        """Return child TabItems names from the parent Tab element.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | Name from tab to select       |
        | msg        | string | Custom error message          |

        Examples:
        | Select Tab Item By Name  <XPATH>  <NAME> |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        return self._module.action(Tab.Action.SELECT_TAB_ITEM_BY_NAME,
                                   [self._module.cast_element_to_type(element, InterfaceType.TAB), name],
                                   msg)
