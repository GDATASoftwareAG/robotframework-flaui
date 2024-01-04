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
        SHOULD_NOT_CONTAIN = "SHOULD_NOT_CONTAIN"
        GET_ITEMS_COUNT = "GET_ITEMS_COUNT"
        GET_ALL_NAMES_FROM_SELECTION = "GET_ALL_NAMES_FROM_SELECTION"
        SHOULD_HAVE_SELECTED_ITEM = "SHOULD_HAVE_SELECTED_ITEM"
        GET_ALL_TEXTS_FROM_SELECTION = "GET_ALL_TEXTS_FROM_SELECTION"
        GET_ALL_NAMES = "GET_ALL_NAMES"
        GET_ALL_TEXTS = "GET_ALL_TEXTS"

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
            self.Action.SHOULD_NOT_CONTAIN:
                lambda: self._should_not_contain(values["element"], values["name"]),
            self.Action.SHOULD_HAVE_SELECTED_ITEM:
                lambda: self._should_have_selected_item(values["element"], values["name"]),
            self.Action.GET_ITEMS_COUNT:
                lambda: self._get_items_count(values["element"]),
            self.Action.GET_ALL_NAMES_FROM_SELECTION:
                lambda: self._get_all_selected_names(values["element"]),
            self.Action.GET_ALL_TEXTS_FROM_SELECTION:
                lambda: self._get_all_selected_texts(values["element"]),
            self.Action.GET_ALL_NAMES:
                lambda: self._get_all_names(values["element"]),
            self.Action.GET_ALL_TEXTS:
                lambda: self._get_all_texts(values["element"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _select_by_index(element: Any, index: int):
        """
        Try to select element from a given index.

        Args:
            element (Object): Selector object to use (Combobox, Listbox).
            index   (Number): Index number to select

        Raises:
            FlaUiError: By an array out of bound exception
            FlaUiError: If value is not a number.
        """
        try:
            element.Items[index].Select()
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ValueError:
            raise FlaUiError(FlaUiError.ValueShouldBeANumber.format(index)) from None

    @staticmethod
    def _select_by_name(element: Any, name: str):
        """
        Try to select element from given name.

        Args:
            element (Object): Selector object to use (Combobox, Listbox).
            name    (String): Name to select

        Raises:
            FlaUiError: If value can not be found by element.
        """
        try:
            element.Select(name)
        except InvalidOperationException:
            raise FlaUiError(FlaUiError.ElementNameNotFound.format(name)) from None

    @staticmethod
    def _should_contain(control: Any, name: str):
        """
        Checks if selector contains a given item by name or text.

        Args:
            control (Object): Selector object to use (Combobox, Listbox).
            name (String): Name or Text from selector item which should exist.

        Returns:
            True if name from combobox item exists otherwise False.
        """
        is_contain = False
        
        for item in control.Items:
            if name in (item.Name, item.Text):
                is_contain = True
                
        Selector._restore_for_expand_collapse_pattern(control)
            
        if not is_contain:
            raise FlaUiError(FlaUiError.ControlDoesNotContainItem.format(name))

    @staticmethod
    def _should_not_contain(control: Any, name: str):
        """
        Checks if selector does not contain a given item by name or text.

        Args:
            control (Object): Selector object to use (Combobox, Listbox).
            name (String): Name or Text from selector item which should exist.

        Returns:
            True if name from combobox item does not exist otherwise False.
        """
        is_contain = False
        
        for item in control.Items:
            if name in (item.Name, item.Text):
                is_contain = True
                
        Selector._restore_for_expand_collapse_pattern(control)
            
        if is_contain:
            raise FlaUiError(FlaUiError.ControlContainsItem.format(name))

    @staticmethod
    def _should_have_selected_item(control: Any, item: Any):
        """
        Verification if specific items are selected.

        Args:
            control (Object): Selector object to use (Combobox, Listbox).
            item    (String): Item name which should be selected.

        Raises:
            FlaUiError: If value is not selected
        """
        names = Selector._get_all_selected_names(control)
        if item not in names:
            raise FlaUiError(FlaUiError.ItemNotSelected.format(item))

    @staticmethod
    def _get_items_count(control: Any):
        count = control.Items.Length
        Selector._restore_for_expand_collapse_pattern(control)
        return count
        
    @staticmethod
    def _get_all_selected_names(control: Any):
        """
        Get all selected names.

        Args:
            control (Object): Selector object to use (Combobox, Listbox).

        Returns:
            List from all names from a selector if exists otherwise empty list.
        """
        names = []

        for selected_item in control.SelectedItems:
            names.append(selected_item.Name)

        return names

    @staticmethod
    def _get_all_selected_texts(control: Any):
        """
        Try to get all selected items as list.

        Args:
            control (Object): Selector object to use (Combobox, Listbox).

        Returns:
            An list from all selected items.
        """

        texts = []

        for item in control.SelectedItems:
            texts.append(item.Text)

        return texts

    @staticmethod
    def _get_all_names(control: Any):
        """
        Get all names from selector.

        Args:
            control (Object): Selector object to use (Combobox, Listbox).

        Returns:
            List from all names from list control if exists otherwise empty list.
        """
        names = []
        for item in control.Items:
            names.append(item.Name)

        Selector._restore_for_expand_collapse_pattern(control)
        
        return names

    @staticmethod
    def _get_all_texts(control: Any):
        """
        Get all texts from selector.

        Args:
            control (Object): Selector object to use (Combobox, Listbox).

        Returns:
            List from all texts from a selector if exists otherwise empty list.
        """
        texts = []

        for item in control.Items:
            texts.append(item.Text)

        Selector._restore_for_expand_collapse_pattern(control)
        
        return texts

    @staticmethod
    def _restore_for_expand_collapse_pattern(control: Any):
        is_supported = control.Patterns.ExpandCollapse.IsSupported
        is_supported = bool(is_supported) if isinstance(is_supported, bool) else bool(is_supported.Value)
        if is_supported:
            pattern = control.Patterns.ExpandCollapse.Pattern
            state = str(pattern.ExpandCollapseState)
            if state == "Expanded":
                control.Collapse() 
