from enum import Enum
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface
from System import ArgumentOutOfRangeException


class ListView(ModuleInterface):
    """List view module wrapper for FlaUI UIA3 usage."""

    class Action(Enum):
        """Enum declaration."""
        SELECT_LIST_VIEW_ROW_BY_INDEX = "SELECT_LIST_VIEW_ROW_BY_INDEX"
        GET_LIST_VIEW_ROW_COUNT = "GET_LIST_VIEW_ROW_COUNT"
        SELECT_LIST_VIEW_ROW_BY_NAME = "SELECT_LIST_VIEW_ROW_BY_NAME"
        GET_SELECTED_LIST_VIEW_ROWS = "GET_SELECTED_LIST_VIEW_ROWS"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported actions for mouse usages are:
          *  Action.SELECT_LIST_VIEW_ROW_BY_INDEX
            * values (Array): [Element, Number]
            * Returns : None

          *  Action.GET_LIST_VIEW_ROW_COUNT
            * values (Array): [Element]
            * Returns : None

         *  Action.SELECT_LIST_VIEW_ROW_BY_NAME
            * values (Array): [Element, Index, String]
            * Returns : None

         *  Action.GET_SELECTED_LIST_VIEW_ROWS
            * values (Array): [Element]
            * Returns : String from all selected rows split up by pipe.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): List view action to use.
            values (Object): Specific value for action if needed.

        """

        switcher = {
            self.Action.GET_LIST_VIEW_ROW_COUNT: lambda: values[0].Rows.Length,
            self.Action.SELECT_LIST_VIEW_ROW_BY_INDEX: lambda: ListView._select_list_view_row_by_index(values[0], values[1]),
            self.Action.SELECT_LIST_VIEW_ROW_BY_NAME: lambda: ListView._select_list_view_row_by_name(values[0], values[1], values[2]),
            self.Action.GET_SELECTED_LIST_VIEW_ROWS: lambda: ListView._get_selected_rows(values[0])
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
    def _select_list_view_row_by_index(control, index):
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
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index))
        except ValueError:
            raise FlaUiError(FlaUiError.ValueShouldBeANumber.format(index))
        except ArgumentOutOfRangeException:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index))

    @staticmethod
    def _select_list_view_row_by_name(control, index, name):
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
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index))
        except ValueError:
            raise FlaUiError(FlaUiError.ValueShouldBeANumber.format(index))
        except ArgumentOutOfRangeException:
            raise FlaUiError(FlaUiError.ListviewItemNotFound.format(name, index))
