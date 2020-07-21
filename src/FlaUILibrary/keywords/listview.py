from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.module import (ListView, Element)


class ListViewKeywords:

    def __init__(self, module):
        """Constructor for list view keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def get_selected_listview_rows(self, identifier, msg=None):
        """Get all selected rows as string. Representation for each cell is a pipe. If nothing is selected empty string
        will be returned.

        For example:
          | Value_1 | Value_2 | Value_3 |

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${data}  Get Selected Listview Rows  <XPath>   |
        """
        element = self._module.cast_element_to_type(self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                                                    InterfaceType.LISTVIEW)
        return self._module.action(ListView.Action.GET_SELECTED_LIST_VIEW_ROWS, [element], msg)

    @keyword
    def select_listview_row_by_index(self, identifier, index, msg=None):
        """Select rows from list view with the given index.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | IndexNumber                   |
        | msg        | string | Custom error message          |
        
        Examples:
        | Select Listview Row By Index  <XPath>  <INDEX>      |

        """
        element = self._module.cast_element_to_type(self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                                                    InterfaceType.LISTVIEW)
        self._module.action(ListView.Action.SELECT_LIST_VIEW_ROW_BY_INDEX, [element, index], msg)
    
    @keyword
    def select_listview_row_by_name(self, identifier, index, name, msg=None):
        """Select rows from list view with the given name in the given column index.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | Column IndexNumber            |
        | name       | string | Column items Name             |
        | msg        | string | Custom error message          |
        
        Examples:
        | Select Listview Row By Index  <XPath>  <INDEX>      |

        """
        element = self._module.cast_element_to_type(self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                                                    InterfaceType.LISTVIEW)
        self._module.action(ListView.Action.SELECT_LIST_VIEW_ROW_BY_NAME, [element, index, name], msg)

    @keyword
    def get_listview_rows_count(self, identifier, msg=None):
        """Return count of rows in listview.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get Listview Rows Count  <XPATH> |
        | Should Be Equal  ${COUNT}  <VALUE_TO_COMPARE> |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        return self._module.action(ListView.Action.GET_LIST_VIEW_ROW_COUNT,
                                   [self._module.cast_element_to_type(element, InterfaceType.LISTVIEW)],
                                   msg)
