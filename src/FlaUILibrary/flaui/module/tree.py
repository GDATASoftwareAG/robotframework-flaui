from enum import Enum
from typing import Optional, Any, List
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
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
        GET_ROOT_ITEMS_COUNT = "TREE_GET_ROOT_ITEMS_COUNT"
        GET_VISIBLE_ITEMS_COUNT = "TREE_GET_VISIBLE_ITEMS_COUNT"
        GET_VISIBLE_ITEMS_NAMES = "TREE_GET_VISIBLE_ITEMS_NAMES"
        ITEM_SHOULD_BE_VISIBLE = "TREE_ITEM_SHOULD_BE_VISIBLE"
        EXPAND_ALL = "TREE_EXPAND_ALL"
        COLLAPSE_ALL = "TREE_COLLAPSE_ALL"
        SELECT_ITEM_BY_NAME = "TREE_SELECT_ITEM_BY_NAME"
        SELECT_ITEM = "TREE_SELECT_ITEM"
        EXPAND_ITEM = "TREE_EXPAND_ITEM"
        COLLAPSE_ITEM = "TREE_COLLAPSE_ITEM"
        SELECTED_ITEM_SHOULD_BE = "TREE_SELECTED_ITEM_SHOULD_BE"
        GET_SELECTED_ITEMS_NAME = "TREE_GET_SELECTED_ITEMS_NAME"
        SET_SEPERATOR = "TREE_SET_SEPERATOR"

    @staticmethod
    def create_value_container(element=None, item=None, seperator=None) -> Container:
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
                              seperator=Converter.cast_to_string(seperator))

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """
        switcher = {
            self.Action.GET_ROOT_ITEMS_COUNT:
                lambda: self._get_root_items_count(values),
            self.Action.EXPAND_ALL:
                lambda: self._expand_all_tree_nodes(values),
            self.Action.COLLAPSE_ALL:
                lambda: self._collapse_all(values),
            self.Action.GET_VISIBLE_ITEMS_NAMES:
                lambda: self._get_visible_item_names(values),
            self.Action.GET_VISIBLE_ITEMS_COUNT:
                lambda: self._get_visible_leaf_count(values),
            self.Action.ITEM_SHOULD_BE_VISIBLE:
                lambda: self._should_be_visible(values),
            self.Action.SELECT_ITEM_BY_NAME:
                lambda: self._select_item_by_name(values),
            self.Action.SELECT_ITEM:
                lambda: self._select_item(values),
            self.Action.EXPAND_ITEM:
                lambda: self._expand_item(values),
            self.Action.COLLAPSE_ITEM:
                lambda: self._collapse_item(values),
            self.Action.SELECTED_ITEM_SHOULD_BE:
                lambda: self._selected_item_should_be(values),
            self.Action.GET_SELECTED_ITEMS_NAME:
                lambda: self._get_selected_items_name(values),
            self.Action.SET_SEPERATOR:
                lambda: self._set_seperator(values),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _select_item(self, container: Container) -> None:
        """
        Select the tree item specified by a location string.

        Args:
            container (Tree.Container): Container holding the UI element and item locator.
                - container['element']: FlaUI tree control instance (root node/container).
                - container['item']: Locator string describing the path to the node (split by the current separator).

        Raises:
            FlaUiError: Propagated when the element or item is invalid or when selection fails.
        """
        element = container["element"]
        item = container["item"]
        TreeItems.execute_by_location(element.Items, item, self._seperator, TreeItemAction.SELECT)

    def _expand_item(self, container: Container) -> None:
        """
        Expand a single tree node identified by a location string.

        Args:
            container (Tree.Container): Container holding the UI element and item locator.
                - container['element']: FlaUI tree control instance.
                - container['item']: Locator string describing the path to the node (split by the current separator).

        Raises:
            FlaUiError: Propagated when the element or item is invalid or when expansion fails.
        """
        element = container["element"]
        item = container["item"]
        TreeItems.execute_by_location(element.Items, item, self._seperator, TreeItemAction.EXPAND)

    def _collapse_item(self, container: Container) -> None:
        """
        Collapse a single tree node identified by a location string.

        Args:
            container (Tree.Container): Container holding the UI element and item locator.
                - container['element']: FlaUI tree control instance.
                - container['item']: Locator string describing the path to the node (split by the current separator).

        Raises:
            FlaUiError: Propagated when the element or item is invalid or when collapse fails.
        """
        element = container["element"]
        item = container["item"]
        TreeItems.execute_by_location(element.Items, item, self._seperator, TreeItemAction.COLLAPSE)

    def _set_seperator(self, container: Container) -> None:
        """
        Sets specific seperator to split up tree items.

        Args:
            container (Tree.Container): Container holding the seperator value.
                - container['seperator']: Seperator to split up tree items.
        Raises:
            FlaUiError: If invalid seperator is try to set
        """
        seperator = container["seperator"]

        if seperator is None:
            raise FlaUiError(FlaUiError.InvalidSeparator)

        self._seperator = seperator

    @staticmethod
    def _should_be_visible(container: Container) -> None:
        """
        Checks if Tree contains a given item by name.

        Args:
            container (Tree.Container): Container holding the UI element and the node name.
                - container['element']: FlaUI tree control instance.
                - container['item']: Display name of the visible node.

       Raises:
            FlaUiError: If element does not exists with searched name.
        """
        control = container["element"]
        name = container["item"]

        if name not in TreeItems.get_all_names_from_tree_nodes(control.Items):
            raise FlaUiError(FlaUiError.ElementNotVisible.format(name))

    @staticmethod
    def _get_selected_items_name(container: Container) -> str:
        """
        Returns the name of selected item if specific items are selected.

        Args:
            container (Tree.Container): Container holding the UI element.
                - container['element']: FlaUI tree control instance.

        Returns:
            Name of selected item if specific items are selected.
        """
        control = container["element"]
        selected = control.SelectedTreeItem

        if not selected:
            raise FlaUiError(FlaUiError.NoItemSelected)

        return str(selected.Name)

    @staticmethod
    def _selected_item_should_be(container: Container) -> None:
        """
        Verification if specific items are selected.

        Args:
            container (Tree.Container): Container which contain the selected item by name.
                - container['item']: Tee control name which should be selected.

        Raises:
            FlaUiError: By an array out of bound exception
            FlaUiError: If value is not a number.
        """
        item = container["item"]

        name = Tree._get_selected_items_name(container)
        if item != name:
            raise FlaUiError(FlaUiError.ItemNotSelected.format(item))

    @staticmethod
    def _expand_all_tree_nodes(container: Container) -> None:
        """
        Expand all tree nodes from an element node.

        Args:
            container (Tree.Container): Container holding the UI element.
                - container['element']: FlaUI tree control instance.
        """
        element = container["element"]
        TreeItems.expand_all_tree_nodes(element.Items)

    @staticmethod
    def _get_root_items_count(container: Container) -> int:
        """
        Get count from all nodes by a given tree node.

        Args:
            container (Tree.Container): Container holding the UI element.
                - container['element']: FlaUI tree control instance.
        """
        element = container["element"]
        return int(element.Items.Length)

    @staticmethod
    def _collapse_all(container: Container) -> None:
        """
        Collapse all nodes from a tree items.

        Args:
            container (Tree.Container): Container holding the UI element.
                - container['element']: FlaUI tree control instance.
        """
        element = container["element"]
        TreeItems.collapse(element.Items)

    @staticmethod
    def _select_item_by_name(container: Container) -> None:
        """
        Select a visible tree node by its display name.

        Args:
            container (Tree.Container): Container holding the UI element and the node name.
                - container['element']: FlaUI tree control instance.
                - container['item']: Display name of the visible node to select.

        Raises:
            FlaUiError: If the node with the given name is not found or selection fails.
        """
        element = container["element"]
        item = container["item"]
        TreeItems.select_visible_node_by_name(element.Items, item)

    @staticmethod
    def _get_visible_leaf_count(container: Container) -> int:
        """
        Get the number of visible leaf nodes for the provided tree element.

        Args:
            container (Tree.Container): Container holding the UI element.
                - container['element']: FlaUI tree control instance.

        Returns:
            int: Count of visible leaf nodes.

        Raises:
            FlaUiError: If the element is invalid or counting fails.
        """
        element = container["element"]
        return TreeItems.get_visible_leaf_count(element.Items)

    @staticmethod
    def _get_visible_item_names(container: Container) -> List[str]:
        """
        Retrieve the display names of all visible nodes in the given tree element.

        Args:
            container (Tree.Container): Container holding the UI element.
                - container['element']: FlaUI tree control instance.

        Returns:
            List[str]: List of visible node names.

        Raises:
            FlaUiError: If the element is invalid or retrieval fails.
        """
        element = container["element"]
        return TreeItems.get_all_names_from_tree_nodes(element.Items)
