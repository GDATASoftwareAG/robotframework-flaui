from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import (Combobox, Selector)
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class ComboBoxKeywords:
    """
    Interface implementation from robotframework usage for combobox keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for combobox keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def get_all_names_from_combobox(self, identifier, msg=None):
        """
        Get all names from a combobox as a list.
        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                            |
        | identifier | string          | XPath identifier from combobox element |
        | msg        | string          | Custom error message                   |

        Examples:
        | ${data}  Get All Names From Combobox  <XPATH> <MSG>                   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        return module.action(Selector.Action.GET_ALL_NAMES,
                             Selector.create_value_container(element=element, msg=msg),
                             msg)

    @keyword
    def get_all_texts_from_combobox(self, identifier, msg=None):
        """
        Get all texts from a combobox as a list.
        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                            |
        | identifier | string          | XPath identifier from combobox element |
        | msg        | string          | Custom error message                   |

        Examples:
        | ${data}  Get All Texts From Combobox  <XPATH> <MSG>                   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        return module.action(Selector.Action.GET_ALL_TEXTS,
                             Selector.create_value_container(element=element, msg=msg),
                             msg)

    @keyword
    def get_all_selected_texts_from_combobox(self, identifier, msg=None):
        """
        Get all selected items from combobox as list.
        If nothing is selected empty list will be returned.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${data}  Get All Selected Texts From Combobox  <XPath>   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        return module.action(Selector.Action.GET_ALL_TEXTS_FROM_SELECTION,
                             Selector.create_value_container(element=element, msg=msg),
                             msg)

    @keyword
    def get_all_selected_names_from_combobox(self, identifier, msg=None):
        """
        Get all selected items from combobox as list.
        If nothing is selected empty list will be returned.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${data}  Get All Selected Names From Combobox  <XPath>   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        return module.action(Selector.Action.GET_ALL_NAMES_FROM_SELECTION,
                             Selector.create_value_container(element=element, msg=msg),
                             msg)

    @keyword
    def select_combobox_item_by_index(self, identifier, index, msg=None):
        """
        Selects item from combobox with given index number.
        Combobox will be automatic collapsed after selection is done.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | index of item                 |
        | msg        | string | Custom error message          |

        Examples:
        | Select Combobox Item By Index  <XPATH>  <INDEX> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        module.action(Selector.Action.SELECT_ITEM_BY_INDEX,
                      Selector.create_value_container(element=element, index=index, msg=msg),
                      msg)
        module.action(Combobox.Action.COLLAPSE_COMBOBOX,
                      Selector.create_value_container(element=element),
                      msg)

    @keyword
    def select_combobox_item_by_name(self, identifier, name, msg=None):
        """
        Selects item from combobox with given name.
        Combobox will be automatic collapsed after selection is done.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | name of item to select        |
        | msg        | string | Custom error message          |

        Examples:
        | Select Combobox Item By Name  <XPATH>  <NAME> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        module.action(Selector.Action.SELECT_ITEM_BY_NAME,
                      Selector.create_value_container(element=element, name=name, msg=msg),
                      msg)
        module.action(Combobox.Action.COLLAPSE_COMBOBOX,
                      Selector.create_value_container(element=element),
                      msg)

    @keyword
    def combobox_should_contain(self, identifier, name, msg=None):
        """
        Checks if Combobox contains an item

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | Name from item                |
        | msg        | string | Custom error message          |

        Examples:
        | Combobox Should Contain  <XPATH>  <NAME> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        module.action(Selector.Action.SHOULD_CONTAIN,
                      Selector.create_value_container(element=element, name=name, msg=msg),
                      msg)

    @keyword
    def get_combobox_items_count(self, identifier, msg=None):
        """
        Return actual count of items in combobox.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get Combobox Items Count  <XPATH> |
        | Should Be Equal  ${value}  ${COUNT}         |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        return module.action(Selector.Action.GET_ITEMS_COUNT,
                             Selector.create_value_container(element=element, msg=msg),
                             msg=msg)

    @keyword
    def collapse_combobox(self, identifier, msg=None):
        """
        Collapse combobox.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Collapse Combobox  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        module.action(Combobox.Action.COLLAPSE_COMBOBOX,
                      Selector.create_value_container(element=element),
                      msg)

    @keyword
    def expand_combobox(self, identifier, msg=None):
        """
        Expand combobox.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Expand Combobox  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        module.action(Combobox.Action.EXPAND_COMBOBOX,
                      Selector.create_value_container(element=element),
                      msg)
