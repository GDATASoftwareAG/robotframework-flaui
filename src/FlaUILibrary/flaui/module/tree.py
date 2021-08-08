from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
from FlaUILibrary.flaui.util.treeitems import TreeItems
from FlaUILibrary.flaui.util.converter import Converter


class Tree(ModuleInterface):
    """
    Tree control wrapper for FlaUI usage.
    Wrapper module executes methods from Tree.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from tree module.
        """
        element: Optional[Any]
        item: Optional[str]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        GET_ROOT_ITEMS_COUNT = "GET_ROOT_ITEMS_COUNT"
        GET_VISIBLE_ITEMS_COUNT = "GET_VISIBLE_ITEMS_COUNT"
        GET_VISIBLE_ITEMS_NAMES = "GET_VISIBLE_ITEMS_NAMES"
        ITEM_SHOULD_BE_VISIBLE = "ITEM_SHOULD_BE_VISIBLE"
        EXPAND_ALL = "EXPAND_ALL"
        COLLAPSE_ALL = "COLLAPSE_ALL"
        SELECT_ITEM_BY_NAME = "SELECT_ITEM_BY_NAME"
        SELECT_ITEM = "SELECT_ITEM"
        EXPAND_ITEM = "EXPAND_ITEM"
        COLLAPSE_ITEM = "COLLAPSE_ITEM"
        SELECTED_ITEM_SHOULD_BE = "SELECTED_ITEM_SHOULD_BE"
        GET_SELECTED_ITEMS_NAME = "GET_SELECTED_ITEMS_NAME"

    @staticmethod
    def create_value_container(element=None, item=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): Tree element to execute action
            item (String): Value from item to use
        """
        return Tree.Container(element=element,
                              item=Converter.cast_to_string(item))

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported actions for checkbox usages are:

          *  Action.GET_ROOT_ITEMS_COUNT
            * values ["element"]
            * Returns : (integer) count of tree items in the root level

          *  Action.GET_VISIBLE_ITEMS_COUNT
            * values ["element"]
            * Returns : (integer) count of every visible tree item.

          *  Action.GET_VISIBLE_ITEMS_NAME
            * values ["element"]
            * Returns : (Array) names of every visible tree item.

        *  Action.ITEM_SHOULD_BE_VISIBLE
            * values ["element", "item"]
            * Returns : None

          *  Action.EXPAND_ALL
            * values ["element"]
            * Returns : None

          *  Action.COLLAPSE_ALL
            * values ["element"]
            * Returns : None

          *  Action.SELECT_ITEM_BY_NAME
            * values ["element", "item"]
            * Returns : None

          *  Action.SELECT_ITEM
            * values ["element", "item"]
            * Returns : None

        *  Action.SELECTED_ITEM_SHOULD_BE
            * values ["element", "item"]
            * Returns : None

        *  Action.GET_SELECTED_ITEMS_NAME
            * values ["element"]
            * Returns : String the name of selected items.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """
        switcher = {
            self.Action.GET_ROOT_ITEMS_COUNT:
                lambda: values["element"].Items.Length,
            self.Action.EXPAND_ALL:
                lambda: self._expand_all_treetems(values["element"]),
            self.Action.COLLAPSE_ALL:
                lambda: self._collapse_all_treetems(values["element"]),
            self.Action.GET_VISIBLE_ITEMS_NAMES:
                lambda: self._get_every_visible_treeitems_name(values["element"]),
            self.Action.GET_VISIBLE_ITEMS_COUNT:
                lambda: self._get_every_visible_treeitems_count(values["element"]),
            self.Action.ITEM_SHOULD_BE_VISIBLE:
                lambda: self._should_be_visible(values["element"], values["item"]),
            self.Action.SELECT_ITEM_BY_NAME:
                lambda: self._select_by_name(values["element"], values["item"]),
            self.Action.SELECT_ITEM:
                lambda: self._select(values["element"], values["item"]),
            self.Action.EXPAND_ITEM:
                lambda: self._expand(values["element"], values["item"]),
            self.Action.COLLAPSE_ITEM:
                lambda: self._collapse(values["element"], values["item"]),
            self.Action.SELECTED_ITEM_SHOULD_BE:
                lambda: self._selected_item_should_be(values["element"], values["item"]),
            self.Action.GET_SELECTED_ITEMS_NAME:
                lambda: self._get_selected_items_name(values["element"]),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_every_visible_treeitems_name(control: Any):
        """
        Counts every visible tree item.

        Args:
            control (Object): Tree control element from FlaUI.

        Returns:
            None.
        """
        obj = TreeItems(control)
        return obj.get_every_visible_treeitems_name()

    @staticmethod
    def _get_every_visible_treeitems_count(control: Any):
        """
        Counts every visible tree item.

        Args:
            control (Object): Tree control element from FlaUI.

        Returns:
            None.
        """

        obj = TreeItems(control)
        obj.get_every_visible_treeitems_name()
        return obj.treeitems_count

    @staticmethod
    def _get_selected_item(control: Any):
        """
        Try to get all selected items as a list.

        Args:
            control (Object): Treeview control to select item from.

        Returns:
            The selected Tree Item object.
        """
        obj = TreeItems(control)
        selected = obj.selected_treeitem
        if not selected:
            raise FlaUiError(FlaUiError.NoItemSelected)
        return selected

    @staticmethod
    def _should_be_visible(control: Any, name: str):
        """
        Checks if Tree contains an given item by name.

        Args:
            control (Object): Tree control element from FlaUI.
            name (String): Name from combobox item which should exist.

        Returns:
            True if name from combobox item exists otherwise False.
        """
        names = Tree._get_every_visible_treeitems_name(control)
        if name not in names:
            raise FlaUiError(FlaUiError.ElementNotVisible.format(name))

    @staticmethod
    def _expand_all_treetems(control: Any):
        """
        Expand all tree items.

        Args:
            control (Object): Tree control element from FlaUI.

        Returns:
            None.
        """
        obj = TreeItems(control)
        obj.expand_all_treeitems()

    @staticmethod
    def _collapse_all_treetems(control: Any):
        """
        Collapse all tree items.

        Args:
            control (Object): Tree control element from FlaUI.

        Returns:
            None.
        """
        TreeItems(control).collapse()

    @staticmethod
    def _select_by_name(control: Any, name: str):
        """
        Try to select element from given name.

        Args:
            control (Object): Tree control UI object.
            name    (String): Name from item to select

        Raises:
            FlaUiError: If value can not be found by element.
        """
        obj = TreeItems(control)
        obj.select_visible_treeitem_by_name(name)

    @staticmethod
    def _select(control: Any, location: str):
        """
        Try to select element from given parameter.

        Args:
            control (Object): Tree control UI object.
            location (String): series of pointers, which shows the item's location.
        Example:
            Location = "N:nameofitem1->N:nameofitem2->I:indexofitem2

        Raises:
            FlaUiError: If value can not be found by control.
        """
        obj = TreeItems(control)
        obj.execute_by_location(location, "Select")

    @staticmethod
    def _expand(control: Any, location: str):
        """
        Try to expand element from given parameter.

        Args:
            control (Object): Tree control UI object.
            location (String): series of pointers, which shows the item's location.

        Raises:
            FlaUiError: If value can not be found by control.
        """
        obj = TreeItems(control)
        obj.execute_by_location(location, "Expand")

    @staticmethod
    def _collapse(control: Any, location: str):
        """
        Try to collapse element from given parameter.

        Args:
            control (Object): Tree control UI object.
            location (String): series of pointers, which shows the item's location.

        Raises:
            FlaUiError: If value can not be found by control.
        """
        obj = TreeItems(control)
        obj.execute_by_location(location, "Collapse")

    @staticmethod
    def _get_selected_items_name(control: Any):
        """
        Returns the name of selected item if specific items are selected.

        Args:
            control (Object): Tree control UI object.
        """
        name = Tree._get_selected_item(control).Name
        return name

    @staticmethod
    def _selected_item_should_be(control: Any, item: str):
        """
        Verification if specific items are selected.

        Args:
            control (Object): Tree control UI object.
            item    (String): Item name which should be selected.

        Raises:
            FlaUiError: By an array out of bound exception
            FlaUiError: If value is not a number.
        """
        name = Tree._get_selected_items_name(control)
        if item != name:
            raise FlaUiError(FlaUiError.ItemNotSelected.format(item))
