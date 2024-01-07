from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import Selector
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class ListBoxKeywords:
    """
    Interface implementation from robotframework usage for listbox keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for Listbox keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def get_all_names_from_listbox(self, identifier, msg=None):
        """
        Get all names from a listbox as a list.
        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                           |
        | identifier | string          | XPath identifier from listbox element |
        | msg        | string          | Custom error message                  |

        Examples:
        | ${data}  Get All Names From Listbox  <XPATH> <MSG>                   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTBOX, msg)
        return module.action(Selector.Action.GET_ALL_NAMES,
                             Selector.create_value_container(element=element, msg=msg),
                             msg)

    @keyword
    def get_all_texts_from_listbox(self, identifier, msg=None):
        """
        Get all texts from a listbox as a list.
        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                           |
        | identifier | string          | XPath identifier from listbox element |
        | msg        | string          | Custom error message                  |

        Examples:
        | ${data}  Get All Texts From Listbox  <XPATH> <MSG>                   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTBOX, msg)
        return module.action(Selector.Action.GET_ALL_TEXTS,
                             Selector.create_value_container(element=element, msg=msg),
                             msg)

    @keyword
    def listbox_selection_should_be(self, identifier, item, msg=None):
        """
        Checks if the selected listbox items are same with the given ones.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                   |
        | identifier | string          | XPath identifier from element |
        | item       | several strings | Name of items                 |
        | msg        | string | Custom error message                   |

        Examples:
        | Listbox Selection Should Be <XPATH>  <STRING>                |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTBOX, msg)
        module.action(Selector.Action.SHOULD_HAVE_SELECTED_ITEM,
                      Selector.create_value_container(element=element, name=item, msg=msg),
                      msg)

    @keyword
    def select_listbox_item_by_index(self, identifier, index, msg=None):
        """
        Selects item from listbox with given index number

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | index of item                 |
        | msg        | string | Custom error message          |

        Examples:
        | Select Listbox Item By Index  <XPATH>  <INDEX>      |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTBOX, msg)
        module.action(Selector.Action.SELECT_ITEM_BY_INDEX,
                      Selector.create_value_container(element=element, index=index, msg=msg),
                      msg)

    @keyword
    def select_listbox_item_by_name(self, identifier, name, msg=None):
        """
        Selects item from listbox by name.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | name from item                |
        | msg        | string | Custom error message          |

        Examples:
        | Select Listbox Item By Name  <XPATH>  <NAME>      |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTBOX, msg)
        module.action(Selector.Action.SELECT_ITEM_BY_NAME,
                      Selector.create_value_container(element=element, name=name, msg=msg),
                      msg)

    @keyword
    def listbox_should_contain(self, identifier, name, msg=None):
        """
        Checks if listbox contains the given item.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | Name of item                  |
        | msg        | string | Custom error message          |

        Examples:
        | Listbox Should Contain  <XPATH>  <STRING> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTBOX, msg)
        module.action(Selector.Action.SHOULD_CONTAIN,
                      Selector.create_value_container(element=element, name=name, msg=msg),
                      msg)

    @keyword
    def listbox_should_not_contain(self, identifier, name, msg=None):
        """
        Checks if listbox does not contain the given item.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | Name of item                  |
        | msg        | string | Custom error message          |

        Examples:
        | Listbox Should Not Contain  <XPATH>  <STRING> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTBOX, msg)
        module.action(Selector.Action.SHOULD_NOT_CONTAIN,
                      Selector.create_value_container(element=element, name=name, msg=msg),
                      msg)

    @keyword
    def get_listbox_items_count(self, identifier, msg=None):
        """
        Return count of rows in listbox.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get Listbox Items Count  <XPATH>  |
        | Should Be Equal  ${COUNT}  <VALUE_TO_COMPARE> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTBOX, msg)
        return module.action(Selector.Action.GET_ITEMS_COUNT,
                             Selector.create_value_container(element=element, msg=msg),
                             msg)
