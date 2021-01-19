from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.module import (Element, ListBox)


class ListBoxKeywords:
    """
    Interface implementation from robotframework usage for listbox keywords.
    """

    def __init__(self, module):
        """Constructor for Listbox keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def listbox_selection_should_be(self, identifier, item, msg=None):
        """Checks if the selected listbox items are same with the given ones.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type            | Description                   |
        | identifier | string          | XPath identifier from element |
        | item       | several strings | Name of items                 |
        | msg        | string | Custom error message                   |

        Examples:
        | Listbox Selection Should Be <XPATH>  <STRING>                |
        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        self._module.action(ListBox.Action.SHOULD_HAVE_SELECTED_ITEM,
                            [self._module.cast_element_to_type(element, InterfaceType.LISTBOX), item],
                            msg)

    @keyword
    def select_listbox_item_by_index(self, identifier, index, msg=None):
        """Selects item from combobox with given index number

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | index of item                 |
        | msg        | string | Custom error message          |

        Examples:
        | Select Listbox Item By Index  <XPATH>  <INDEX>      |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        self._module.action(ListBox.Action.SELECT_ITEM_BY_INDEX,
                            [self._module.cast_element_to_type(element, InterfaceType.LISTBOX), index],
                            msg)

    @keyword
    def listbox_should_contain(self, identifier, name, msg=None):
        """Checks if listbox contains the given item.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | name       | string | Name of item                  |
        | msg        | string | Custom error message          |

        Examples:
        | Listbox Should Contain <XPATH>  <STRING> |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        self._module.action(ListBox.Action.SHOULD_CONTAIN,
                            [self._module.cast_element_to_type(element, InterfaceType.LISTBOX), name],
                            msg)

    @keyword
    def get_listbox_items_count(self, identifier, msg=None):
        """Return count of rows in listbox.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get Listbox Items Count  <XPATH>  |
        | Should Be Equal  ${COUNT}  <VALUE_TO_COMPARE> |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        return self._module.action(ListBox.Action.GET_ITEMS_COUNT,
                                   [self._module.cast_element_to_type(element, InterfaceType.LISTBOX)],
                                   msg)
