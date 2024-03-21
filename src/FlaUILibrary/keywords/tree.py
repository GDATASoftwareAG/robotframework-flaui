from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import Tree
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class TreeKeywords:
    """
    Interface implementation from robotframework usage for tree keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for tree keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def get_root_treeitems_count(self, identifier, msg=None):
        """
        Return count of items in the first level of the tree.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get Root TreeItems Count  <XPATH>  |
        | Should Be Equal  ${COUNT}  <VALUE_TO_COMPARE> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        return module.action(Tree.Action.GET_ROOT_ITEMS_COUNT,
                             Tree.create_value_container(element=element),
                             msg)

    @keyword
    def get_all_visible_treeitems_count(self, identifier, msg=None):
        """
        Returns the count of every visible tree item.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get All Visible TreeItems Count  <XPATH>  |
        | Should Be Equal  ${COUNT}  <TOTAL_COUNT_OF_VISIBLE_TREEITEMS> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        return module.action(Tree.Action.GET_VISIBLE_ITEMS_COUNT,
                             Tree.create_value_container(element=element),
                             msg)

    @keyword
    def get_all_visible_treeitems_names(self, identifier, msg=None):
        """
        Returns a list of names of every visible tree item.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | @{LIST_OF_NAMES_OF_VISIBLE_TREEITEMS}  Create List name1  name2  name3 |
        | ${Name}  Get All Visible TreeItems Names  <XPATH>                      |
        | Should Be Equal  ${Name}  ${LIST_OF_NAMES_OF_VISIBLE_TREEITEMS}        |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        return module.action(Tree.Action.GET_VISIBLE_ITEMS_NAMES,
                             Tree.create_value_container(element=element),
                             msg)

    @keyword
    def expand_all_treeitems(self, identifier, msg=None):
        """
        Expands every expandable Tree items of the given tree.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                   |
        | identifier | string          | XPath identifier from element |
        | msg        | string          | Custom error message          |

        Examples:
        | Expand All TreeItems  <XPATH>                 |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        module.action(Tree.Action.EXPAND_ALL,
                      Tree.create_value_container(element=element),
                      msg)

    @keyword
    def collapse_all_treeitems(self, identifier, msg=None):
        """
        Collapse every collapsable tree items of the given tree.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                   |
        | identifier | string          | XPath identifier from element |
        | msg        | string          | Custom error message          |

        Examples:
        | Collapse All TreeItems <XPATH>                 |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        module.action(Tree.Action.COLLAPSE_ALL,
                      Tree.create_value_container(element=element),
                      msg)

    @keyword
    def treeitem_should_be_visible(self, identifier, name, msg=None):
        """
        Iterates every visible tree item. And fails if a node does not contain by given name.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                   |
        | identifier | string          | XPath identifier from element |
        | name       | string          | Name of treeitem              |
        | msg        | string          | Custom error message          |

        Examples:
        | TreeItem Should Be Visible  <XPATH>  <Name>            |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        module.action(Tree.Action.ITEM_SHOULD_BE_VISIBLE,
                      Tree.create_value_container(element=element, item=name),
                      msg)

    @keyword
    def get_selected_treeitems_name(self, identifier, msg=None):
        """
        Selects item from tree with given index number

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${Name}  Get Selected Treeitems Name  ${XPATH_TREE} |
        | Should Be Equal     ${Name}  <Name>                 |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        return module.action(Tree.Action.GET_SELECTED_ITEMS_NAME,
                             Tree.create_value_container(element=element),
                             msg)

    @keyword
    def select_visible_treeitem_by_name(self, identifier, name, msg=None):
        """
        Selects item from tree by name.
        If the given name could not be found or was not visible in tree FlauiError will be thrown.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | name from item                |
        | msg        | string | Custom error message          |

        Examples:
        | Select visible TreeItem By Name  <XPATH>  <NAME>   |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        module.action(Tree.Action.SELECT_ITEM_BY_NAME,
                      Tree.create_value_container(element=element, item=name),
                      msg)

    @keyword
    def select_treeitem(self, identifier, item, msg=None):
        """
        Selects item from tree by hybrid pointers, series of indexes and names.

        Tree item will be located using the following syntax:
        N:Name1->I:index2->N:Name3
        Means in the root level of tree the item with name Name1 will be expanded.
        Under it will be taken the item with index of (int) index2 and expanded.
        Under it there is an item with name Name3 will be selected.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | item       | string | Hybrid solution               |
        | msg        | string | Custom error message          |

        Examples:
        | ${item}=  N:name1->N:name2->N:name3      |
        | Select TreeItem   <XPATH>  ${item}      |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        module.action(Tree.Action.SELECT_ITEM,
                      Tree.create_value_container(element=element, item=item),
                      msg)

    @keyword
    def expand_treeitem(self, identifier, item, msg=None):
        """
        Expands item from tree by hybrid pointers, series of indexes and names.

        Tree item will be located using the following syntax:
        N:Name1->I:index2->N:Name3
        Means in the root level of tree the item with name Name1 will be expanded.
        Under it will be taken the item with index of (int) index2 and expanded.
        Under it there is an item with name Name3 will be expanded.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | item       | string | Hybrid solution               |
        | msg        | string | Custom error message          |

        Examples:
        | ${item}=  N:name1->N:name2->N:name3      |
        | Expand TreeItem   <XPATH>  ${item}      |


        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        module.action(Tree.Action.EXPAND_ITEM,
                      Tree.create_value_container(element=element, item=item),
                      msg)

    @keyword
    def collapse_treeitem(self, identifier, item, msg=None):
        """
        Collapses item from tree by hybrid pointers, series of indexes and names.

        Tree item will be located using the following syntax:
        N:Name1->I:index2->N:Name3
        Means in the root level of tree the item with name Name1 will be expanded.
        Under it will be taken the item with index of (int) index2 and expanded.
        Under it there is an item with name Name3 will be Collapsed.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | item       | string | Hybrid solution               |
        | msg        | string | Custom error message          |

        Examples:
        | ${item}=  N:name1->N:name2->N:name3        |
        | Collapse TreeItem   <XPATH>  ${item}      |


        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        module.action(Tree.Action.COLLAPSE_ITEM,
                      Tree.create_value_container(element=element, item=item),
                      msg)

    @keyword
    def selected_treeitem_should_be(self, identifier, item, msg=None):
        """
        Checks if the selected tree items are same with the given ones.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                   |
        | identifier | string          | XPath identifier from element |
        | item       | string          | Name of treeitem              |
        | msg        | string          | Custom error message          |

        Examples:
        | Selected TreeItem Should Be  <XPATH>  <item>                 |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.TREE, msg=msg)
        module.action(Tree.Action.SELECTED_ITEM_SHOULD_BE,
                      Tree.create_value_container(element=element, item=item),
                      msg)

    @keyword
    def set_tree_item_seperator(self, seperator, msg=None):
        """
        Sets specific tree item seperator to split.

        XPaths syntax is explained in `XPath locator`.

        Arguments:
        | Argument   | Type            | Description                   |
        | seperator  | string          | Seperator to set to split up  |

        Examples:
        | Set Tree Item Seperator  <seperator>                         |
        """
        module = self._container.create_or_get_module()
        module.action(Tree.Action.SET_SEPERATOR,
                      Tree.create_value_container(seperator=seperator),
                      msg)
