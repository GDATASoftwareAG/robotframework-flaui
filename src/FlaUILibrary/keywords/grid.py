from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.module import (Element, Grid)


class GridKeywords:
    """
    Interface implementation from robotframework usage for grid keywords.
    """

    def __init__(self, module):
        """Constructor for list view keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def get_selected_grid_rows(self, identifier, msg=None):
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
        | ${data}  Get Selected Grid Rows  <XPath>   |
        """
        element = self._module.cast_element_to_type(self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                                                    InterfaceType.LISTVIEW)
        return self._module.action(Grid.Action.GET_SELECTED_ROWS, [element], msg)

    @keyword
    def select_grid_row_by_index(self, identifier, index, msg=None):
        """Select rows from data grid with the given index.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | IndexNumber                   |
        | msg        | string | Custom error message          |

        Examples:
        | Select Grid Row By Index  <XPath>  <INDEX>      |

        """
        element = self._module.cast_element_to_type(self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                                                    InterfaceType.LISTVIEW)
        self._module.action(Grid.Action.SELECT_ROW_BY_INDEX, [element, index], msg)

    @keyword
    def select_grid_row_by_name(self, identifier, index, name, msg=None):
        """Select specific row by name from data grid.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | Column IndexNumber            |
        | name       | string | Column items Name             |
        | msg        | string | Custom error message          |

        Examples:
        | Select Grid Row By Name  <XPath>  <INDEX>      |

        """
        element = self._module.cast_element_to_type(self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                                                    InterfaceType.LISTVIEW)
        self._module.action(Grid.Action.SELECT_ROW_BY_NAME, [element, index, name], msg)

    @keyword
    def get_grid_rows_count(self, identifier, msg=None):
        """Return count of rows from data grid.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get Grid Rows Count  <XPATH> |
        | Should Be Equal  ${COUNT}  <VALUE_TO_COMPARE> |

        """
        element = self._module.action(Element.Action.GET_ELEMENT, identifier, msg)
        return self._module.action(Grid.Action.GET_ROW_COUNT,
                                   [self._module.cast_element_to_type(element, InterfaceType.LISTVIEW)],
                                   msg)
