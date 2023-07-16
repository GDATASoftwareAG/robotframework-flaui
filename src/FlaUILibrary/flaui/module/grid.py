from enum import Enum
from typing import Optional, Any
from System import ArgumentOutOfRangeException  # pylint: disable=import-error
from System import NullReferenceException  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


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

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        SELECT_ROW_BY_INDEX = "SELECT_ROW_BY_INDEX"
        GET_ROW_COUNT = "GET_ROW_COUNT"
        SELECT_ROW_BY_NAME = "SELECT_ROW_BY_NAME"
        GET_SELECTED_ROWS = "GET_SELECTED_ROWS"
        GET_ALL_DATA = "GET_ALL_DATA"

    @staticmethod
    def create_value_container(element=None, index=None, name=None, msg=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): Grid element to access
            index (Number): Index value to select from grid data
            name (String): Name from grid element
            msg (String): Optional error message
        """
        return Grid.Container(element=element,
                              index=Converter.cast_to_int(index, msg),
                              name=Converter.cast_to_string(name))

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported actions for mouse usages are:
          *  Action.SELECT_ROW_BY_INDEX
            * values ["element", "index"]
            * Returns : None

          *  Action.GET_ROW_COUNT
            * values ["element"]
            * Returns : None

         *  Action.SELECT_ROW_BY_NAME
            * values ["element", "index"]
            * Returns : None

         *  Action.GET_SELECTED_ROWS
            * values ["element"]
            * Returns : String from all selected rows split up by pipe.

         *  Action.GET_ALL_DATA_FROM_GRID
            * values ["element"]
            * Returns : Array from all elements by grid.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): Specific value for action if needed.

        """

        switcher = {
            self.Action.GET_ROW_COUNT: lambda: values["element"].Rows.Length,
            self.Action.SELECT_ROW_BY_INDEX: lambda: self._select_row_by_index(values["element"], values["index"]),
            self.Action.SELECT_ROW_BY_NAME: lambda: self._select_row_by_name(values["element"],
                                                                             values["index"],
                                                                             values["name"]),
            self.Action.GET_SELECTED_ROWS: lambda: self._get_selected_rows(values["element"]),
            self.Action.GET_ALL_DATA: lambda: self._get_all_data(values["element"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_all_data(control: Any):
        """
        Try to get all selected rows as string.

        Args:
            control (Object): List view to select items.

        Returns:
            String from all selected items separated as pipe for example | Value_1 | Value_2 |
        """
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
    def _get_selected_rows(control: Any):
        """
        Try to get all selected rows as string.

        Args:
            control (Object): List view to select items.

        Returns:
            String from all selected items separated as pipe for example | Value_1 | Value_2 |
        """

        values = ""

        for row in control.SelectedItems:
            values += "| "
            for cell in row.Cells:
                values += cell.Value + " | "
            values += "\n"

        return values

    @staticmethod
    def _select_row_by_index(control: Any, index: int):
        """
        Try to select element from given index.

        Args:
            control (Object): List view to select items.
            index   (Number): Index number to select.

        Raises:
            FlaUiError: By an array out of bound exception
            FlaUiError: If value is not a number.
        """
        try:
            if control.Rows.Length > 0:
                control.AddToSelection(index)
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ArgumentOutOfRangeException:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except NullReferenceException:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None

    @staticmethod
    def _select_row_by_name(control: Any, index: int, name: str):
        """
        Try to select element from given name from given column index

        Args:
            control (Object): List view to select items.
            index   (Number): Index number to select.
            name    (String): Expected row name.
        Raises:
            FlaUiError: By an array out of bound exception
            FlaUiError: If value is not a number.
            FlaUIError: If Name Could not be found in the given Index.
        """
        try:
            if control.Rows.Length > 0:
                control.AddToSelection(index, name)
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ArgumentOutOfRangeException:
            raise FlaUiError(FlaUiError.ListviewItemNotFound.format(name, index)) from None
        except NullReferenceException:
            raise FlaUiError(FlaUiError.ListviewItemNotFound.format(name, index)) from None
