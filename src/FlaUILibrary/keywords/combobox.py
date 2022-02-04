from robotlibcore import keyword
from FlaUILibrary.flaui.interface import InterfaceType
from FlaUILibrary.flaui.module import Selector
from FlaUILibrary.flaui.uia import UIA


class ComboBoxKeywords:
    """
    Interface implementation from robotframework usage for combobox keywords.
    """

    def __init__(self, module: UIA):
        """
        Constructor for combobox keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

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
        element = self._module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        return self._module.action(Selector.Action.GET_ALL_NAMES,
                                   Selector.create_value_container(element=element, msg=msg),
                                   msg)

    @keyword
    def get_selected_items_from_combobox(self, identifier, msg=None):
        """
        Get all selected items from combobox as string. If nothing is selected empty string  will be returned.

        For example:
          Value_1
          Value_2

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${data}  Get Selected Items From Combobox  <XPath>   |
        """
        element = self._module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        return self._module.action(Selector.Action.GET_SELECTED_ITEMS,
                                   Selector.create_value_container(element=element, msg=msg),
                                   msg)

    @keyword
    def select_combobox_item_by_index(self, identifier, index, msg=None):
        """
        Selects item from combobox with given index number

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | index of item                 |
        | msg        | string | Custom error message          |

        Examples:
        | Select Combobox Item By Index  <XPATH>  <INDEX> |

        """
        element = self._module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        self._module.action(Selector.Action.SELECT_ITEM_BY_INDEX,
                            Selector.create_value_container(element=element, index=index, msg=msg),
                            msg)

    @keyword
    def combobox_should_contain(self, identifier, name, msg=None):
        """
        Checks if Combobox contains an item

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | Name from item                |
        | msg        | string | Custom error message          |

        Examples:
        | Combobox Should Contain  <XPATH>  <NAME> |

        """
        element = self._module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        self._module.action(Selector.Action.SHOULD_CONTAIN,
                            Selector.create_value_container(element=element, name=name, msg=msg),
                            msg)

    @keyword
    def get_combobox_items_count(self, identifier, msg=None):
        """
        Return actual count of items in combobox.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get Combobox Items Count  <XPATH> |
        | Should Be Equal  ${value}  ${COUNT}         |

        """
        element = self._module.get_element(identifier, InterfaceType.COMBOBOX, msg)
        return self._module.action(Selector.Action.GET_ITEMS_COUNT,
                                   Selector.create_value_container(element=element, msg=msg),
                                   msg=msg)
