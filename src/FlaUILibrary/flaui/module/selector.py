from enum import Enum
from typing import Optional, Any, List
from System import InvalidOperationException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
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
        """
        Supported actions for execute action implementation.
        """
        SELECT_ITEM_BY_INDEX = "SELECTOR_SELECT_ITEM_BY_INDEX"
        SELECT_ITEM_BY_NAME = "SELECTOR_SELECT_ITEM_BY_NAME"
        SHOULD_CONTAIN = "SELECTOR_SHOULD_CONTAIN"
        SHOULD_NOT_CONTAIN = "SELECTOR_SHOULD_NOT_CONTAIN"
        GET_ITEMS_COUNT = "SELECTOR_GET_ITEMS_COUNT"
        GET_ALL_NAMES_FROM_SELECTION = "SELECTOR_GET_ALL_NAMES_FROM_SELECTION"
        SHOULD_HAVE_SELECTED_ITEM = "SELECTOR_SHOULD_HAVE_SELECTED_ITEM"
        GET_ALL_TEXTS_FROM_SELECTION = "SELECTOR_GET_ALL_TEXTS_FROM_SELECTION"
        GET_ALL_NAMES = "SELECTOR_GET_ALL_NAMES"
        GET_ALL_TEXTS = "SELECTOR_GET_ALL_TEXTS"

    @staticmethod
    def create_value_container(element=None, index=None, name=None, msg=None) -> Container:
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

    def execute_action(self, action: Action, values: Container) -> Any:
        """If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """
        switcher = {
            self.Action.SELECT_ITEM_BY_INDEX:
                lambda: self._select_by_index(values),
            self.Action.SELECT_ITEM_BY_NAME:
                lambda: self._select_by_name(values),
            self.Action.SHOULD_CONTAIN:
                lambda: self._should_contain(values),
            self.Action.SHOULD_NOT_CONTAIN:
                lambda: self._should_not_contain(values),
            self.Action.SHOULD_HAVE_SELECTED_ITEM:
                lambda: self._should_have_selected_item(values),
            self.Action.GET_ITEMS_COUNT:
                lambda: self._get_items_count(values),
            self.Action.GET_ALL_NAMES_FROM_SELECTION:
                lambda: self._get_all_selected_names(values),
            self.Action.GET_ALL_TEXTS_FROM_SELECTION:
                lambda: self._get_all_selected_texts(values),
            self.Action.GET_ALL_NAMES:
                lambda: self._get_all_names(values),
            self.Action.GET_ALL_TEXTS:
                lambda: self._get_all_texts(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _select_by_index(container: Container) -> None:
        """
        Select the item at the given index from a selector control.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.
                - container['index']: Integer index of the item to select.

        Raises:
            FlaUiError: If the index is out of range (array out of bounds).
            FlaUiError: If the provided index cannot be interpreted as a number.
        """
        element = container["element"]
        index = container["index"]

        try:
            element.Items[index].Select()
        except IndexError:
            raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(index)) from None
        except ValueError:
            raise FlaUiError(FlaUiError.ValueShouldBeANumber.format(index)) from None

    @staticmethod
    def _select_by_name(container: Container) -> None:
        """
        Select the item with the given display name from a selector control.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.
                - container['name']: String name of the item to select.

        Raises:
            FlaUiError: If no item with the specified name exists on the control.
        """
        element = container["element"]
        name = container["name"]

        try:
            element.Select(name)
        except InvalidOperationException:
            raise FlaUiError(FlaUiError.ElementNameNotFound.format(name)) from None

    @staticmethod
    def _should_contain(container: Container) -> None:
        """
        Assert that the selector contains an item matching the given name or text.

        The check compares the provided name against each item's `Name` and `Text`
        properties. After the check, the control's expand/collapse state is restored
        if required.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.
                - container['name']: Name or text to look for.

        Raises:
            FlaUiError: If the control does not contain an item matching the provided name.
        """
        control = container["element"]
        name = container["name"]
        is_contain = False

        for item in control.Items:
            if name in (item.Name, item.Text):
                is_contain = True

        Selector._restore_for_expand_collapse_pattern(container)

        if not is_contain:
            raise FlaUiError(FlaUiError.ControlDoesNotContainItem.format(name))

    @staticmethod
    def _should_not_contain(container: Container) -> None:
        """
        Assert that the selector does not contain an item matching the given name or text.

        The check compares the provided name against each item's `Name` and `Text`
        properties. After the check, the control's expand/collapse state is restored
        if required.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.
                - container['name']: Name or text that must not be present.

        Raises:
            FlaUiError: If the control contains an item matching the provided name.
        """
        control = container["element"]
        name = container["name"]
        is_contain = False

        for item in control.Items:
            if name in (item.Name, item.Text):
                is_contain = True

        Selector._restore_for_expand_collapse_pattern(container)

        if is_contain:
            raise FlaUiError(FlaUiError.ControlContainsItem.format(name))

    @staticmethod
    def _should_have_selected_item(container: Container) -> None:
        """
        Verify that a specific item is currently selected.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.
                - container['name']: The expected selected item name.

        Raises:
            FlaUiError: If the named item is not present in the current selection.
        """
        item = container["name"]
        names = Selector._get_all_selected_names(container)
        if item not in names:
            raise FlaUiError(FlaUiError.ItemNotSelected.format(item))

    @staticmethod
    def _get_items_count(container: Container) -> int:
        """
        Return the total number of items in the selector control.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.

        Returns:
            int: Number of items in the control.
        """
        control = container["element"]
        count = control.Items.Length
        Selector._restore_for_expand_collapse_pattern(container)
        return count

    @staticmethod
    def _get_all_selected_names(container: Container) -> List[str]:
        """
        Return the display names of all currently selected items.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.

        Returns:
            List[str]: List of `Name` values from selected items. Empty list if none selected.
        """
        control = container["element"]
        names = []

        for selected_item in control.SelectedItems:
            names.append(selected_item.Name)

        return names

    @staticmethod
    def _get_all_selected_texts(container: Container) -> List[str]:
        """
        Return the text values of all currently selected items.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.

        Returns:
            List[str]: List of `Text` values from selected items. Empty list if none selected.
        """
        control = container["element"]
        texts = []

        for item in control.SelectedItems:
            texts.append(item.Text)

        return texts

    @staticmethod
    def _get_all_names(container: Container) -> List[str]:
        """
        Return the display names of all items in the selector control.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.

        Returns:
            List[str]: List of `Name` values for all items. Empty list if no items.
        """
        control = container["element"]
        names = []

        for item in control.Items:
            names.append(item.Name)

        Selector._restore_for_expand_collapse_pattern(container)

        return names

    @staticmethod
    def _get_all_texts(container: Container) -> List[str]:
        """
        Return the text values of all items in the selector control.

        Args:
            container (Selector.Container): Container holding:
                - container['element']: The ComboBox/ListBox control instance.

        Returns:
            List[str]: List of Text values for all items. Empty list if no items.

        """
        control = container["element"]
        texts = []

        for item in control.Items:
            texts.append(item.Text)

        Selector._restore_for_expand_collapse_pattern(container)

        return texts

    @staticmethod
    def _restore_for_expand_collapse_pattern(container: Container) -> None:
        """
        Collapse the control if it is currently expanded and supports ExpandCollapse.

        Args:
            container (Selector.Container or control object): Either:
                - a Selector.Container with `container['element']` set to the control, or
                - the control object itself (as some call sites pass the control directly).
        """
        control = container["element"]
        is_supported = control.Patterns.ExpandCollapse.IsSupported
        is_supported = bool(is_supported) if isinstance(is_supported, bool) else bool(is_supported.Value)
        if is_supported:
            pattern = control.Patterns.ExpandCollapse.Pattern
            state = str(pattern.ExpandCollapseState)
            if state == "Expanded":
                control.Collapse()
