from robotlibcore import keyword
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.module import Grid
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class GridKeywords:
    """
    Interface implementation from robotframework usage for grid keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for list view keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def get_all_data_from_grid(self, identifier, msg=None):
        """
        Get all data from a grid as an array collection.

        Includes all header values as first element from list.

        For example data grid:
        [
          [ "Value_1", "Value_2", "Value_3" ],
          [ "Data_1", "Data_2", "Data_3" ],
        ]

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${data}  Get All Data From Grid  <XPath>   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTVIEW, msg)
        return module.action(Grid.Action.GET_ALL_DATA, Grid.create_value_container(element=element),
                             msg)

    @keyword
    def get_header_from_grid(self, identifier, msg=None):
        """
        Get header from a grid as an array collection.

        Includes all header values as first element from list.

        For example data grid:
        [
          [ "Value_1", "Value_2", "Value_3" ],
          [ "Data_1", "Data_2", "Data_3" ],
        ]

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${data}  Get Header From Grid  <XPath>   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTVIEW, msg)
        return module.action(Grid.Action.GET_HEADER, Grid.create_value_container(element=element),
                             msg)

    @keyword
    def get_selected_grid_rows(self, identifier, msg=None):
        """
        Get all selected rows as string. Representation for each cell is a pipe. If nothing is selected empty string
        will be returned.

        For example:
          | Value_1 | Value_2 | Value_3 |

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${data}  Get Selected Grid Rows  <XPath>   |
        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTVIEW, msg)
        return module.action(Grid.Action.GET_SELECTED_ROWS, Grid.create_value_container(element=element),
                             msg)

    @keyword
    def select_grid_row_by_index(self, identifier, index, multiselect=True, msg=None):
        """
        Select rows from data grid with the given index.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | IndexNumber                   |
        | multiselect | bool   | Multiselect availble or not  |
        | msg        | string | Custom error message          |

        Examples:
        | Select Grid Row By Index  <XPath>  <INDEX>      |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTVIEW, msg)
        module.action(Grid.Action.SELECT_ROW_BY_INDEX,
                      Grid.create_value_container(element=element, index=index, multiselect=multiselect),
                      msg)

    @keyword
    def select_grid_row_by_name(self, identifier, index, name, multiselect=True, msg=None):
        """
        Select specific row by name from data grid.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | index      | string | Column IndexNumber            |
        | name       | string | Column items Name             |
        | multiselect | bool   | Multiselect availble or not  |
        | msg        | string | Custom error message          |

        Examples:
        | Select Grid Row By Name  <XPath>  <INDEX>      |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTVIEW, msg)
        module.action(Grid.Action.SELECT_ROW_BY_NAME,
                      Grid.create_value_container(element=element, index=index, name=name, multiselect=multiselect),
                      msg)

    @keyword
    def get_grid_rows_count(self, identifier, msg=None):
        """
        Return count of rows from data grid.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${COUNT}  Get Grid Rows Count  <XPATH> |
        | Should Be Equal  ${COUNT}  <VALUE_TO_COMPARE> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, InterfaceType.LISTVIEW, msg)
        return module.action(Grid.Action.GET_ROW_COUNT,
                             Grid.create_value_container(element=element, msg=msg),
                             msg)
