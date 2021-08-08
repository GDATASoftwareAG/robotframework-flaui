from enum import Enum
from typing import Optional, Any
from System import Exception as CSharpException  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


class Tab(ModuleInterface):
    """
    Tab module wrapper for FlaUI usage.
    Wrapper module executes methods from Tab.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from tab module.
        """
        element: Optional[Any]
        name: Optional[str]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        GET_TAB_ITEMS_NAMES = "GET_TAB_ITEMS_NAMES"
        SELECT_TAB_ITEM_BY_NAME = "SELECT_TAB_ITEM_BY_NAME"

    @staticmethod
    def create_value_container(element=None, name=None):
        """
        Helper to create container object.

        Args:
            element (Object): Tab element to use
            name (String): Name from tab item to search
        """
        return Tab.Container(element=element,
                             name=Converter.cast_to_string(name))

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.GET_TAB_ITEMS_NAMES
            * Values ["element"]
            * Returns : List from all names in tab

          *  Action.SELECT_TAB_ITEM_BY_NAME
            * Values ["element"]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_TAB_ITEMS_NAMES: lambda: self._get_tab_items_names(values["element"]),
            self.Action.SELECT_TAB_ITEM_BY_NAME: lambda: self._select_tab_item(values["element"], values["name"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_tab_items_names(element: Any):
        """
        Get all TabItems from Tab element.

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
    def _select_tab_item(element: Any, name: str):
        """
        Try to select from tab given name.

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
