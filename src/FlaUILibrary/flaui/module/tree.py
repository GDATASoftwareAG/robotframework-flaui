from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
from FlaUILibrary.flaui.util.treeitems import TreeItems
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.enum.treeitemaction import TreeItemAction


class Tree(ModuleInterface):
    """
    Tree control wrapper for FlaUI usage.
    Wrapper module executes methods from Tree.cs implementation.
    """

    def __init__(self):
        self._seperator = "->"

    class Container(ValueContainer):
        """
        Value container from tree module.
        """
        element: Optional[Any]
        item: Optional[str]
        seperator: Optional[str]

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
        SET_SEPERATOR = "SET_SEPERATOR"

    @staticmethod
    def create_value_container(element=None, item=None, seperator=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): Tree element to execute action
            item (String): Value from item to use
            seperator (String): Seperator to split up tree items.
        """
        return Tree.Container(element=element,
                              item=Converter.cast_to_string(item),
                              seperator=seperator)

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

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
                lambda: TreeItems.expand_all_tree_nodes(values["element"].Items),
            self.Action.COLLAPSE_ALL:
                lambda: TreeItems.collapse(values["element"].Items),
            self.Action.GET_VISIBLE_ITEMS_NAMES:
                lambda: TreeItems.get_all_names_from_tree_nodes(values["element"].Items),
            self.Action.GET_VISIBLE_ITEMS_COUNT:
                lambda: TreeItems.get_visible_leaf_count(values["element"].Items),
            self.Action.ITEM_SHOULD_BE_VISIBLE:
                lambda: self._should_be_visible(values["element"], values["item"]),
            self.Action.SELECT_ITEM_BY_NAME:
                lambda: TreeItems.select_visible_node_by_name(values["element"].Items, values["item"]),
            self.Action.SELECT_ITEM:
                lambda: TreeItems.execute_by_location(values["element"].Items,
                                                      values["item"],
                                                      self._seperator,
                                                      TreeItemAction.SELECT),
            self.Action.EXPAND_ITEM:
                lambda: TreeItems.execute_by_location(values["element"].Items,
                                                      values["item"],
                                                      self._seperator,
                                                      TreeItemAction.EXPAND),
            self.Action.COLLAPSE_ITEM:
                lambda: TreeItems.execute_by_location(values["element"].Items,
                                                      values["item"],
                                                      self._seperator,
                                                      TreeItemAction.COLLAPSE),
            self.Action.SELECTED_ITEM_SHOULD_BE:
                lambda: self._selected_item_should_be(values["element"], values["item"]),
            self.Action.GET_SELECTED_ITEMS_NAME:
                lambda: self._get_selected_items_name(values["element"]),
            self.Action.SET_SEPERATOR:
                lambda: self._set_seperator(values["seperator"]),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _set_seperator(self, seperator):
        """
        Sets specific seperator to split up tree items.

        Args:
            seperator (Object): Seperator to split items.

        Raises:
            FlaUiError: If seperator is invalid to set
        """
        if seperator is None:
            raise FlaUiError(FlaUiError.InvalidSeparator)

        self._seperator = seperator


    @staticmethod
    def _should_be_visible(control: Any, name: str):
        """
        Checks if Tree contains a given item by name.

        Args:
            control (Object): Tree control element from FlaUI.
            name (String): Name from combobox item which should exist.

        Returns:
            True if name from combobox item exists otherwise False.
        """
        if name not in TreeItems.get_all_names_from_tree_nodes(control.Items):
            raise FlaUiError(FlaUiError.ElementNotVisible.format(name))

    @staticmethod
    def _get_selected_items_name(control: Any):
        """
        Returns the name of selected item if specific items are selected.

        Args:
            control (Object): Tree control UI object.
        """
        selected = control.SelectedTreeItem
        if not selected:
            raise FlaUiError(FlaUiError.NoItemSelected)

        return selected.Name

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
