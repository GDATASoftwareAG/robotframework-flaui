from enum import Enum
from typing import Optional, Any, List
from System import ArgumentOutOfRangeException  # pylint: disable=import-error
from System import NullReferenceException  # pylint: disable=import-error
from System import InvalidOperationException  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer


class Grid(ModuleInterface):
    """
    List view module wrapper for FlaUI usage.
    Wrapper module executes methods from Grid.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from grid module.
        """
        element: Optional[Any]
        index: Optional[int]
        name: Optional[str]
        multiselect: Optional[bool]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        SELECT_ROW_BY_INDEX = "GRID_SELECT_ROW_BY_INDEX"
        GET_ROW_COUNT = "GRID_GET_ROW_COUNT"
        SELECT_ROW_BY_NAME = "GRID_SELECT_ROW_BY_NAME"
        GET_SELECTED_ROWS = "GRID_GET_SELECTED_ROWS"
        GET_ALL_DATA = "GRID_GET_ALL_DATA"
        GET_HEADER = "GRID_GET_HEADER"
        GET_COLUMN_COUNT = "GRID_GET_COLUMN_COUNT"

    @staticmethod
    def create_value_container(element=None,
                               index=None,
                               name=None,
                               multiselect=None,
                               msg=None) -> Container:
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): Grid element to access
            index (Number): Index value to select from grid data
            name (String): Name from grid element
            multiselect (Boolean): If grid supports multiselect
            msg (String): Optional error message
        """
        return Grid.Container(element=element,
                              index=Converter.cast_to_int(index, msg),
                              multiselect=Converter.cast_to_bool(multiselect),
                              name=Converter.cast_to_string(name))

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): Specific value for action if needed.

        """

        switcher = {
            self.Action.GET_ROW_COUNT:
                lambda: self._get_row_count(values),
            self.Action.GET_COLUMN_COUNT:
                lambda: self._get_column_count(values),
            self.Action.SELECT_ROW_BY_INDEX:
                lambda: self._select_row_by_index(values),
            self.Action.SELECT_ROW_BY_NAME:
                lambda: self._select_row_by_name(values),
            self.Action.GET_SELECTED_ROWS:
                lambda: self._get_selected_rows(values),
            self.Action.GET_ALL_DATA:
                lambda: self._get_all_data(values),
            self.Action.GET_HEADER:
                lambda: self._get_header(values),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_row_count(container: Container) -> int:
        """
        Return the number of rows available in the grid control.

        Args:
            container (Grid.Container): Container holding:
                - container['element']: Grid/ListView control instance.

        Returns:
            int: Number of rows reported by the control.
        """
        return int(container["element"].RowCount)

    @staticmethod
    def _get_column_count(container: Container) -> int:
        """
        Return the number of columns available in the grid control.

        Args:
            container (Grid.Container): Container holding:
                - container['element']: Grid/ListView control instance.

        Returns:
            int: Number of columns reported by the control.
        """
        return int(container["element"].ColumnCount)

    @staticmethod
    def _get_all_data(container: Container) -> List[List[str]]:
        """
        Return all header and row cell values from the grid as nested lists.

        Args:
            container (Grid.Container): Container holding:
                - container['element']: Grid/ListView control instance.

        Returns:
            List[List[str]]: First element is the header row (column texts),
                             following elements are row cell value lists.
                             Empty lists or placeholder rows are excluded.
        """
        control = container["element"]
        values = []
        data = []

        for column in control.Header.Columns:
            data.append(column.Text)

        values.append(data)

        for row in control.Rows:
            data = []
            for cell in row.Cells:
                if "NewItemPlaceholder" not in cell.Value:
                    data.append(cell.Value)

            if data:
                values.append(data)

        return values

    @staticmethod
    def _get_header(container: Container) -> List[str]:
        """
        Return the header column texts from the grid.

        Args:
            container (Grid.Container): Container holding:
                - container['element']: Grid/ListView control instance.

        Returns:
            List[str]: Header column texts in order.
        """
        control = container["element"]
        data = []

        for column in control.Header.Columns:
            data.append(column.Text)

        return data

    @staticmethod
    def _get_selected_rows(container: Container) -> str:
        """
        Return a textual representation of all currently selected rows.

        Args:
            container (Grid.Container): Container holding:
                - container['element']: Grid/ListView control instance.

        Returns:
            str: Multi-line string where each selected row is represented as
                 \"| cell1 | cell2 | ... |\" followed by a newline.
        """
        control = container["element"]
        values = ""

        for row in control.SelectedItems:
            values += "| "
            for cell in row.Cells:
                values += cell.Value + " | "
            values += "\n"

        return values

    @staticmethod
    def _select_row_by_index(container: Container) -> None:
        """
        Select a row by its numeric index, supporting optional multiselect.

        Args:
            container (Grid.Container): Container holding:
                - container['element']: Grid/ListView control instance.
                - container['index']: Integer row index to select.
                - container['multiselect']: Boolean; if True, AddToSelection is used.

        Raises:
            FlaUiError: If the index is out of range (array out of bounds).
            FlaUiError: If the control is single-select but multiselect was requested.
            FlaUiError: If the provided index value cannot be interpreted as a number.
        """
        control = container["element"]
        index = container["index"]
        multiselect = container["multiselect"]

        try:
            if control.RowCount > 0:
                if multiselect:
                    try:
                        control.AddToSelection(index)
                    except InvalidOperationException:
                        raise FlaUiError(FlaUiError.GridIsSingleSelect) from None
                else:
                    control.Select(index)
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ArgumentOutOfRangeException:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except NullReferenceException:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None

    @staticmethod
    def _select_row_by_name(container: Container) -> None:
        """
        Select a row by providing a column index and expected cell text for that column.

        Args:
            container (Grid.Container): Container holding:
                - container['element']: Grid/ListView control instance.
                - container['index']: Integer column index to compare.
                - container['name']: Expected cell text in the specified column.
                - container['multiselect']: Boolean; if True, AddToSelection is used.

        Raises:
            FlaUiError: If the specified index/column is out of range or the item is not found.
            FlaUiError: If the control is single-select but multiselect was requested.
        """
        control = container["element"]
        index = container["index"]
        name = container["name"]
        multiselect = container["multiselect"]

        try:
            if control.RowCount > 0:
                if multiselect:
                    try:
                        control.AddToSelection(index, name)
                    except InvalidOperationException:
                        raise FlaUiError(FlaUiError.GridIsSingleSelect) from None
                else:
                    control.Select(index, name)
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ArgumentOutOfRangeException:
            raise FlaUiError(FlaUiError.ListviewItemNotFound.format(name, index)) from None
        except NullReferenceException:
            raise FlaUiError(FlaUiError.ListviewItemNotFound.format(name, index)) from None
