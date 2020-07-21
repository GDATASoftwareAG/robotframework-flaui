from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.module import (ListControl, Element)


class ComboBoxKeywords:

    def __init__(self, module):
        """Constructor for combobox keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def get_selected_items_from_combobox(self, identifier, msg=None):
        """Get all selected items from combobox as string. If nothing is selected empty string  will be returned.

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
        element = self._module.cast_element_to_type(self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                                                    InterfaceType.COMBOBOX)
        return self._module.action(ListControl.Action.GET_SELECTED_ITEMS_FROM_LIST_CONTROL, [element], msg)

    @keyword
    def select_combobox_item_by_index(self, identifier, index, msg=None):
        """Selects item from combobox with given index number

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
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        self._module.action(ListControl.Action.SELECT_LIST_CONTROL_ITEM_BY_INDEX,
                            [self._module.cast_element_to_type(element, InterfaceType.COMBOBOX), index],
                            msg)

    @keyword
    def combobox_should_contain(self, identifier, name, msg=None):
        """Checks if Combobox contains an item

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
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        self._module.action(ListControl.Action.LIST_CONTROL_SHOULD_CONTAIN,
                            [self._module.cast_element_to_type(element, InterfaceType.COMBOBOX), name],
                            msg)

    @keyword
    def get_combobox_items_count(self, identifier, msg=None):
        """Return actual count of items in combobox.

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
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        return self._module.action(ListControl.Action.GET_LIST_CONTROL_ITEMS_COUNT,
                                   [self._module.cast_element_to_type(element, InterfaceType.COMBOBOX)],
                                   msg=msg)
