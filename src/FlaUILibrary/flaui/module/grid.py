from enum import Enum
from System import ArgumentOutOfRangeException  # pylint: disable=import-error
from System import NullReferenceException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface


class Grid(ModuleInterface):
    """
    List view module wrapper for FlaUI usage.
    Wrapper module executes methods from Grid.cs implementation.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        SELECT_ROW_BY_INDEX = "SELECT_ROW_BY_INDEX"
        GET_ROW_COUNT = "GET_ROW_COUNT"
        SELECT_ROW_BY_NAME = "SELECT_ROW_BY_NAME"
        GET_SELECTED_ROWS = "GET_SELECTED_ROWS"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported actions for mouse usages are:
          *  Action.SELECT_ROW_BY_INDEX
            * values (Array): [Element, Number]
            * Returns : None

          *  Action.GET_ROW_COUNT
            * values (Array): [Element]
            * Returns : None

         *  Action.SELECT_ROW_BY_NAME
            * values (Array): [Element, Index, String]
            * Returns : None

         *  Action.GET_SELECTED_ROWS
            * values (Array): [Element]
            * Returns : String from all selected rows split up by pipe.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): Specific value for action if needed.

        """

        switcher = {
            self.Action.GET_ROW_COUNT: lambda: values[0].Rows.Length,
            self.Action.SELECT_ROW_BY_INDEX: lambda: Grid._select_row_by_index(values[0], values[1]),
            self.Action.SELECT_ROW_BY_NAME: lambda: Grid._select_row_by_name(values[0], values[1], values[2]),
            self.Action.GET_SELECTED_ROWS: lambda: Grid._get_selected_rows(values[0])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_selected_rows(control):
        """Try to get all selected rows as string.

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
    def _select_row_by_index(control, index):
        """Try to select element from given index.

        Args:
            control (Object): List view to select items.
            index   (Number): Index number to select.

        Raises:
            FlaUiError: By an array out of bound exception
            FlaUiError: If value is not a number.
        """
        try:
            if control.Rows.Length > 0:
                control.AddToSelection(int(index))
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ValueError:
            raise FlaUiError(FlaUiError.ValueShouldBeANumber.format(index)) from None
        except ArgumentOutOfRangeException:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except NullReferenceException:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None

    @staticmethod
    def _select_row_by_name(control, index, name):
        """Try to select element from given name from given column index

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
                control.AddToSelection(int(index), str(name))
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ValueError:
            raise FlaUiError(FlaUiError.ValueShouldBeANumber.format(index)) from None
        except ArgumentOutOfRangeException:
            raise FlaUiError(FlaUiError.ListviewItemNotFound.format(name, index)) from None
        except NullReferenceException:
            raise FlaUiError(FlaUiError.ListviewItemNotFound.format(name, index)) from None
