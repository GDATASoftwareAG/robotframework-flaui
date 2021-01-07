from enum import Enum
from System import Exception as CSharpException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface


class Tab(ModuleInterface):
    """
    Tab module wrapper for FlaUI usage.
    Wrapper module executes methods from Tab.cs implementation.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        GET_TAB_ITEMS_NAMES = "GET_TAB_ITEMS_NAMES"
        SELECT_TAB_ITEM_BY_NAME = "SELECT_TAB_ITEM_BY_NAME"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.GET_TAB_ITEMS_NAMES
            * Values (Array): [Element]
            * Returns : List from all names in tab

          *  Action.SELECT_TAB_ITEM_BY_NAME
            * Values (Array): [Element, String]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_TAB_ITEMS_NAMES: lambda: Tab._get_tab_items_names(values[0]),
            self.Action.SELECT_TAB_ITEM_BY_NAME: lambda: Tab._select_tab_item(values[0], values[1])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_tab_items_names(element):
        """Get all TabItems from Tab element.

        Args:
            element (Object): Tab element from FlaUI.

        Returns:
            List of all TabItem elements names from Tab control if exists otherwise empty list.
        """
        child_tab_items_names = []

        for tab_items in element.TabItems:
            child_tab_items_names.append(tab_items.Name)

        return child_tab_items_names

    @staticmethod
    def _select_tab_item(element, name):
        """Try to select from tab given name.

        Args:
            element (Object): Tab element from FlaUI.
            name (String): Name from tab to select.

        Raises:
            FlaUiError: If tab name could not be found.

        """

        try:
            element.SelectTabItem(name)
        except CSharpException as exception:
            raise FlaUiError(FlaUiError.GenericError.format(exception.Message)) from None
