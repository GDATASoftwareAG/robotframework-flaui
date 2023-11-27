from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import Tab
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class TabKeywords:
    """
    Interface implementation from robotframework usage for tab keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for tab keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def get_tab_items_names(self, identifier, msg=None):
        """
        Return child TabItems names from the parent Tab element.

        XPaths syntax is explained in `XPath locator`.

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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TAB, msg=msg)
        return module.action(Tab.Action.GET_TAB_ITEMS_NAMES,
                             Tab.create_value_container(element=element),
                             msg)

    @keyword
    def select_tab_item_by_name(self, identifier, name, msg=None):
        """
        Return child TabItems names from the parent Tab element.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | Name from tab to select       |
        | msg        | string | Custom error message          |

        Examples:
        | Select Tab Item By Name  <XPATH>  <NAME> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TAB, msg=msg)
        return module.action(Tab.Action.SELECT_TAB_ITEM_BY_NAME,
                             Tab.create_value_container(element=element, name=name),
                             msg)
