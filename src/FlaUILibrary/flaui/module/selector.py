from enum import Enum
from typing import Optional, Any
from System import InvalidOperationException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
from FlaUILibrary.flaui.util.converter import Converter


class Selector(ModuleInterface):
    """
    List control module wrapper for FlaUI usage.
    Wrapper module executes methods from ComboBox.cs and ListBox.cs implementation.
    https://docs.microsoft.com/de-de/dotnet/api/system.windows.controls.primitives.selector?view=net-5.0
    """

    class Container(ValueContainer):
        """
        Value container from selector module.
        """
        index: Optional[int]
        name: Optional[str]
        element: Optional[Any]

    class Action(Enum):
        """Supported actions for execute action implementation."""
        SELECT_ITEM_BY_INDEX = "SELECT_ITEM_BY_INDEX"
        SELECT_ITEM_BY_NAME = "SELECT_ITEM_BY_NAME"
        SHOULD_CONTAIN = "SHOULD_CONTAIN"
        GET_ITEMS_COUNT = "GET_ITEMS_COUNT"
        GET_ALL_NAMES_FROM_SELECTION = "GET_ALL_NAMES_FROM_SELECTION"
        SHOULD_HAVE_SELECTED_ITEM = "SHOULD_HAVE_SELECTED_ITEM"
        GET_SELECTED_ITEMS = "GET_SELECTED_ITEMS"
        GET_ALL_NAMES = "GET_ALL_NAMES"

    @staticmethod
    def create_value_container(element=None, index=None, name=None, msg=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): ListBox or Combobox elements.
            index (Number): Number to select from element
            name (String): Name from element to select
            msg (String): Optional error message
        """
        return Selector.Container(name=Converter.cast_to_string(name),
                                  element=None if not element else element,
                                  index=Converter.cast_to_int(index, msg))

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported actions for checkbox usages are:

          *  Action.SELECT_ITEM_BY_INDEX
            * values ["element", "index"]
            * Returns : None

          *  Action.SELECT_ITEM_BY_NAME
            * values ["element", "name"]
            * Returns : None

          *  Action.SHOULD_CONTAIN
            * values ["element", "name"]
            * Returns : None

          *  Action.GET_ITEMS_COUNT
            * values ["element"]
            * Returns : None

        *  Action.GET_ALL_NAMES_FROM_SELECTION
            * values ["element"]
            * Returns : None

        *  Action.SHOULD_HAVE_SELECTED_ITEM
            * values ["element", "name"]
            * Returns : None

        *  Action.GET_SELECTED_ITEMS
            * values ["element"]
            * Returns : String from all selected items.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """
        switcher = {
            self.Action.SELECT_ITEM_BY_INDEX:
                lambda: self._select_by_index(values["element"], values["index"]),
            self.Action.SELECT_ITEM_BY_NAME:
                lambda: self._select_by_name(values["element"], values["name"]),
            self.Action.SHOULD_CONTAIN:
                lambda: self._should_contain(values["element"], values["name"]),
            self.Action.GET_ITEMS_COUNT:
                lambda: values["element"].Items.Length,
            self.Action.GET_ALL_NAMES_FROM_SELECTION:
                lambda: self._get_all_selected_names(values["element"]),
            self.Action.SHOULD_HAVE_SELECTED_ITEM:
                lambda: self._should_have_selected_item(values["element"], values["name"]),
            self.Action.GET_SELECTED_ITEMS:
                lambda: self._get_selected_items(values["element"]),
            self.Action.GET_ALL_NAMES:
                lambda: self._get_all_names(values["element"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_selected_items(element: Any):
        """
        Try to get all selected items as string.

        Args:
            element (Object): List view to select items.

        Returns:
            String from all selected items separated as pipe for example:
                Value 1
                Value 2
        """

        values = ""

        for selected_item in element.SelectedItems:
            values += selected_item.Text + "\n"

        return values

    @staticmethod
    def _select_by_index(element: Any, index: int):
        """
        Try to select element from given index.

        Args:
            element (Object): List control UI object.
            index   (Number): Index number to select

        Raises:
            FlaUiError: By an array out of bound exception
            FlaUiError: If value is not a number.
        """
        try:
            element.Items[int(index)].Select()
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ValueError:
            raise FlaUiError(FlaUiError.ValueShouldBeANumber.format(index)) from None

    @staticmethod
    def _select_by_name(element: Any, name: str):
        """
        Try to select element from given name.

        Args:
            element (Object): List control UI object.
            name    (String): Name from item to select

        Raises:
            FlaUiError: If value can not be found by element.
        """
        try:
            element.Select(name)
        except InvalidOperationException:
            raise FlaUiError(FlaUiError.ElementNameNotFound.format(name)) from None

    @staticmethod
    def _should_have_selected_item(control: Any, item: Any):
        """
        Verification if specific items are selected.

        Args:
            control (Object): List control UI object.
            item    (String): Item name which should be selected.

        Raises:
            FlaUiError: By an array out of bound exception
            FlaUiError: If value is not a number.
        """
        names = Selector._get_all_selected_names(control)
        if item not in names:
            raise FlaUiError(FlaUiError.ItemNotSelected.format(item))

    @staticmethod
    def _get_all_selected_names(control: Any):
        """
        Get all selected names.

        Args:
            control (Object): List control element from FlaUI.

        Returns:
            List from all names from list control if exists otherwise empty list.
        """
        names = []

        for selected_item in control.SelectedItems:
            names.append(selected_item.Name)

        return names

    @staticmethod
    def _get_all_names(control: Any):
        """
        Get all names from selector.

        Args:
            control (Object): List control element from FlaUI.

        Returns:
            List from all names from list control if exists otherwise empty list.
        """
        names = []
        for item in control.Items:
            names.append(item.Text)

        return names

    @staticmethod
    def _should_contain(control: Any, name: str):
        """
        Checks if Listbox contains an given item by name.

        Args:
            control (Object): List control element from FlaUI.
            name (String): Name from combobox item which should exist.

        Returns:
            True if name from combobox item exists otherwise False.
        """
        for item in control.Items:
            if item.Name == name:
                return

        raise FlaUiError(FlaUiError.ControlDoesNotContainItem.format(name))
