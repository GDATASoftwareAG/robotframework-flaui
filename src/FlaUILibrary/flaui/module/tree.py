from enum import Enum
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface
from FlaUILibrary.flaui.util.treeitems import TreeItems


class Tree(ModuleInterface):
    """
    Tree control wrapper for FlaUI usage.
    Wrapper module executes methods from Tree.cs implementation.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
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

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported actions for checkbox usages are:

          *  Action.GET_ROOT_ITEMS_COUNT
            * values (Array): [Element]
            * Returns : (integer) count of tree items in the root level

          *  Action.GET_VISIBLE_ITEMS_COUNT
            * values (Array): [Element]
            * Returns : (integer) count of every visible tree item.

          *  Action.GET_VISIBLE_ITEMS_NAME
            * values (Array): [Element]
            * Returns : (Array) names of every visible tree item.

        *  Action.ITEM_SHOULD_BE_VISIBLE
            * values (Array): [Element, String]
            * Returns : None

          *  Action.EXPAND_ALL
            * values (Array): [Element]
            * Returns : None

          *  Action.COLLAPSE_ALL
            * values (Array): [Element]
            * Returns : None

          *  Action.SELECT_ITEM_BY_NAME
            * values (Array): [Element, String]
            * Returns : None

          *  Action.SELECT_ITEM
            * values (Array): [Element, String]
            * Returns : None

        *  Action.SELECTED_ITEM_SHOULD_BE
            * values (Array): [Element, String]
            * Returns : None

        *  Action.GET_SELECTED_ITEMS_NAME
            * values (Array): [Element]
            * Returns : String the name of selected items.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """
        switcher = {
            self.Action.GET_ROOT_ITEMS_COUNT:
                lambda: values[0].Items.Length,
            self.Action.EXPAND_ALL:
                lambda: Tree._expand_all_treetems(values[0]),
            self.Action.COLLAPSE_ALL:
                lambda: Tree._collapse_all_treetems(values[0]),
            self.Action.GET_VISIBLE_ITEMS_NAMES:
                lambda: Tree._get_every_visible_treeitems_name(values[0]),
            self.Action.GET_VISIBLE_ITEMS_COUNT:
                lambda: Tree._get_every_visible_treeitems_count(values[0]),
            self.Action.ITEM_SHOULD_BE_VISIBLE:
                lambda: Tree._should_be_visible(values[0], values[1]),
            self.Action.SELECT_ITEM_BY_NAME:
                lambda: Tree._select_by_name(values[0], values[1]),
            self.Action.SELECT_ITEM:
                lambda: Tree._select(values[0], values[1]),
            self.Action.EXPAND_ITEM:
                lambda: Tree._expand(values[0], values[1]),
            self.Action.COLLAPSE_ITEM:
                lambda: Tree._collapse(values[0], values[1]),
            self.Action.SELECTED_ITEM_SHOULD_BE:
                lambda: Tree._selected_item_should_be(values[0], values[1]),
            self.Action.GET_SELECTED_ITEMS_NAME:
                lambda: Tree._get_selected_items_name(values[0]),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_every_visible_treeitems_name(control):
        """Counts every visible tree item.

        Args:
            control (Object): Tree control element from FlaUI.

        Returns:
            None.
        """
        obj = TreeItems(control)
        return obj.get_every_visible_treeitems_name()


    @staticmethod
    def _get_every_visible_treeitems_count(control):
        """Counts every visible tree item.

        Args:
            control (Object): Tree control element from FlaUI.

        Returns:
            None.
        """

        obj = TreeItems(control)
        obj.get_every_visible_treeitems_name()
        return obj.treeitems_count

    @staticmethod
    def _get_selected_item(control):
        """Try to get all selected items as a list.

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
    def _should_be_visible(control, name):
        """Checks if Tree contains an given item by name.

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
    def _expand_all_treetems(control):
        """Expand all tree items.

        Args:
            control (Object): Tree control element from FlaUI.

        Returns:
            None.
        """
        obj = TreeItems(control)
        obj.expand_all_treeitems()

    @staticmethod
    def _collapse_all_treetems(control):
        """collapse all tree items.

        Args:
            control (Object): Tree control element from FlaUI.

        Returns:
            None.
        """
        TreeItems(control).collapse()

    @staticmethod
    def _select_by_name(control, name):
        """Try to select element from given name.

        Args:
            control (Object): Tree control UI object.
            name    (String): Name from item to select

        Raises:
            FlaUiError: If value can not be found by element.
        """
        obj = TreeItems(control)
        obj.select_visible_treeitem_by_name(name)

    @staticmethod
    def _select(control, location):
        """Try to select element from given parameter.

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
    def _expand(control, location):
        """Try to expand element from given parameter.

        Args:
            control (Object): Tree control UI object.
            location (String): series of pointers, which shows the item's location.

        Raises:
            FlaUiError: If value can not be found by control.
        """
        obj = TreeItems(control)
        obj.execute_by_location(location, "Expand")


    @staticmethod
    def _collapse(control, location):
        """Try to collapse element from given parameter.

        Args:
            control (Object): Tree control UI object.
            location (String): series of pointers, which shows the item's location.

        Raises:
            FlaUiError: If value can not be found by control.
        """
        obj = TreeItems(control)
        obj.execute_by_location(location, "Collapse")

    @staticmethod
    def _get_selected_items_name(control):
        """Retruns the name of selected item if specific items are selected.

        Args:
            control (Object): Tree control UI object.
        """
        name = Tree._get_selected_item(control).Name
        return name

    @staticmethod
    def _selected_item_should_be(control, item):
        """Verification if specific items are selected.

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
