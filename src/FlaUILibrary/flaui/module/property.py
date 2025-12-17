from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any, Tuple
from FlaUI.UIA2.Identifiers import TextAttributes as AttributesUia2  # pylint: disable=import-error
from FlaUI.UIA3.Identifiers import TextAttributes as AttributesUia3  # pylint: disable=import-error
from FlaUI.Core.Definitions import WindowVisualState as NetWidowVisualState  # pylint: disable=import-error
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.exception.flauierror import FlaUiError


class Property(ModuleInterface):
    """
    Property module wrapper for FlaUI usage to get property values from elements
    """
    class WindowVisualState(Enum):
        """
        Window visual state mapping
        """
        NORMAL = NetWidowVisualState.Normal
        MINIMIZED = NetWidowVisualState.Minimized
        MAXIMIZED = NetWidowVisualState.Maximized

    @dataclass
    class Container(ValueContainer):
        """
        Value container from property module.
        """
        element: Optional[Any]
        uia: str
        visual_state: Optional["Property.WindowVisualState"]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        FOREGROUND_COLOR = "PROPERTY_FOREGROUND_COLOR"
        BACKGROUND_COLOR = "PROPERTY_BACKGROUND_COLOR"
        FONT_SIZE = "PROPERTY_FONT_SIZE"
        FONT_NAME = "PROPERTY_FONT_NAME"
        FONT_WEIGHT = "PROPERTY_FONT_WEIGHT"
        CULTURE = "PROPERTY_CULTURE"
        IS_HIDDEN = "PROPERTY_IS_HIDDEN"
        WINDOW_VISUAL_STATE = "PROPERTY_WINDOW_VISUAL_STATE"
        WINDOW_INTERACTION_STATE = "PROPERTY_WINDOW_INTERACTION_STATE"
        TOGGLE_STATE = "PROPERTY_TOGGLE_STATE"
        MAXIMIZE_WINDOW = "PROPERTY_MAXIMIZE_WINDOW"
        MINIMIZE_WINDOW = "PROPERTY_MINIMIZE_WINDOW"
        NORMALIZE_WINDOW = "PROPERTY_NORMALIZE_WINDOW"
        CAN_WINDOW_MINIMIZE = "PROPERTY_CAN_WINDOW_MINIMIZE"
        CAN_WINDOW_MAXIMIZE = "PROPERTY_CAN_WINDOW_MAXIMIZE"
        IS_READ_ONLY = "PROPERTY_IS_READ_ONLY"
        IS_WINDOW_PATTERN_SUPPORTED = "PROPERTY_IS_WINDOW_PATTERN_SUPPORTED"
        IS_TEXT_PATTERN_SUPPORTED = "PROPERTY_IS_TEXT_PATTERN_SUPPORTED"
        IS_TOGGLE_PATTERN_SUPPORTED = "PROPERTY_IS_TOGGLE_PATTERN_SUPPORTED"
        IS_VALUE_PATTERN_SUPPORTED = "PROPERTY_IS_VALUE_PATTERN_SUPPORTED"
        IS_RANGEVALUE_PATTERN_SUPPORTED = "PROPERTY_IS_RANGEVALUE_PATTERN_SUPPORTED"
        VALUE = "PROPERTY_VALUE"
        RANGEVALUE = "PROPERTY_RANGEVALUE"
        RANGEMINIMUM = "PROPERTY_RANGEMINIMUM"
        RANGEMAXIMUM = "PROPERTY_RANGEMAXIMUM"
        IS_EXPAND_COLLAPSE_PATTERN_SUPPORTED = "PROPERTY_IS_EXPAND_COLLAPSE_PATTERN_SUPPORTED"
        EXPAND_COLLAPSE_STATE = "PROPERTY_EXPAND_COLLAPSE_STATE"
        IS_SELECTION_ITEM_PATTERN_SUPPORTED = "PROPERTY_IS_SELECTION_ITEM_PATTERN_SUPPORTED"
        IS_SELECTED = "PROPERTY_IS_SELECTED"
        STAGE_FOR_COMBOBOX_SELECTIONITEM = "PROPERTY_STAGE_FOR_COMBOBOX_SELECTIONITEM"
        HELP_TEXT = "PROPERTY_HELP_TEXT"

    @staticmethod
    def create_value_container(element: Any = None,
                               uia: str = None,
                               visual_state: WindowVisualState = WindowVisualState.NORMAL) -> Container:
        """
        Helper to create container object.

        Args:
            element (Object): Element to grab property.
            uia (string): User interface identifier
            visual_state (WindowVisualState): Window visual state enum value.
        """
        return Property.Container(element=element,
                                  uia=uia,
                                  visual_state=visual_state)

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
            self.Action.FOREGROUND_COLOR:
                lambda: self._get_foreground_color(values),
            self.Action.BACKGROUND_COLOR:
                lambda: self._get_background_color(values),
            self.Action.FONT_SIZE:
                lambda: self._get_font_size(values),
            self.Action.FONT_NAME:
                lambda: self._get_font_name(values),
            self.Action.FONT_WEIGHT:
                lambda: self._get_font_weight(values),
            self.Action.CULTURE:
                lambda: self._get_culture(values),
            self.Action.IS_HIDDEN:
                lambda: self._is_hidden(values),
            self.Action.WINDOW_VISUAL_STATE:
                lambda: self._get_window_visual_state(values),
            self.Action.WINDOW_INTERACTION_STATE:
                lambda: self._get_window_interaction_state(values),
            self.Action.TOGGLE_STATE:
                lambda: self._get_toggle_state(values),
            self.Action.MAXIMIZE_WINDOW:
                lambda: self._set_window_visual_state(values),
            self.Action.MINIMIZE_WINDOW:
                lambda: self._set_window_visual_state(values),
            self.Action.NORMALIZE_WINDOW:
                lambda: self._set_window_visual_state(values),
            self.Action.CAN_WINDOW_MAXIMIZE:
                lambda: self._can_window_maximize(values),
            self.Action.CAN_WINDOW_MINIMIZE:
                lambda: self._can_window_minimize(values),
            self.Action.IS_READ_ONLY:
                lambda: self._is_read_only(values),
            self.Action.IS_WINDOW_PATTERN_SUPPORTED:
                lambda: self._is_window_pattern_supported(values),
            self.Action.IS_TEXT_PATTERN_SUPPORTED:
                lambda: self._is_text_pattern_supported(values),
            self.Action.IS_TOGGLE_PATTERN_SUPPORTED:
                lambda: self._is_toggle_pattern_supported(values),
            self.Action.IS_VALUE_PATTERN_SUPPORTED:
                lambda: self._is_value_pattern_supported(values),
            self.Action.IS_RANGEVALUE_PATTERN_SUPPORTED:
                lambda: self._is_rangevalue_pattern_supported(values),
            self.Action.VALUE:
                lambda: self._get_value_from_value_pattern(values),
            self.Action.RANGEVALUE:
                lambda: self._get_value_from_rangevalue_pattern(values),
            self.Action.RANGEMINIMUM:
                lambda: self._get_minimum_from_rangevalue_pattern(values),
            self.Action.RANGEMAXIMUM:
                lambda: self._get_maximum_from_rangevalue_pattern(values),
            self.Action.IS_EXPAND_COLLAPSE_PATTERN_SUPPORTED:
                lambda: self._is_expand_collapse_pattern_supported(values),
            self.Action.EXPAND_COLLAPSE_STATE:
                lambda: self._get_expand_collapse_pattern_state(values),
            self.Action.IS_SELECTION_ITEM_PATTERN_SUPPORTED:
                lambda: self._is_selection_item_pattern_supported(values),
            self.Action.IS_SELECTED:
                lambda: self._is_selected(values),
            self.Action.STAGE_FOR_COMBOBOX_SELECTIONITEM:
                lambda: self._stage_for_combobox_selectionitem(values),
            self.Action.HELP_TEXT:
                lambda: self._get_help_text(values),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_window_visual_state(container: Container) -> str:
        """
        Return the window visual state of the element as a string.

        Args:
            container (Container): Container holding:
                - container['element']: Window element supporting Window pattern.

        Returns:
            str: Window visual state (e.g., 'Normal', 'Minimized', 'Maximized').
        """
        pattern = Property._get_window_pattern_from_element(container)
        return str(pattern.WindowVisualState.Value.ToString())

    @staticmethod
    def _get_foreground_color(container: Container) -> Tuple[int, int, int, int]:
        """
        Return the foreground color of text as an (R, G, B, A) tuple.

        Args:
            container (Container): Container holding:
                - container['uia']: 'UIA2' or 'UIA3' string to select identifiers.
                - container['element']: Element supporting Text pattern.

        Returns:
            Tuple[int, int, int, int]: Foreground color components.
        """
        uia = container["uia"]
        pattern = Property._get_text_pattern_from_element(container)
        if uia == "UIA2":
            return Property._int_to_rgba(pattern.DocumentRange.GetAttributeValue(AttributesUia2.ForegroundColor))

        return Property._int_to_rgba(pattern.DocumentRange.GetAttributeValue(AttributesUia3.ForegroundColor))

    @staticmethod
    def _get_background_color(container: Container) -> Tuple[int, int, int, int]:
        """
        Return the background color of text as an (R, G, B, A) tuple.

        Args:
            container (Container): Container holding:
                - container['uia']: 'UIA2' or 'UIA3' string to select identifiers.
                - container['element']: Element supporting Text pattern.

        Returns:
            Tuple[int, int, int, int]: Background color components.
        """
        uia = container["uia"]
        pattern = Property._get_text_pattern_from_element(container)
        if uia == "UIA2":
            return Property._int_to_rgba(pattern.DocumentRange.GetAttributeValue(AttributesUia2.BackgroundColor))

        return Property._int_to_rgba(pattern.DocumentRange.GetAttributeValue(AttributesUia3.BackgroundColor))

    @staticmethod
    def _get_font_size(container: Container) -> float:
        """
        Return the font size from the Text DocumentRange.

        Args:
            container (Container): Container holding:
                - container['uia']: 'UIA2' or 'UIA3' string to select identifiers.
                - container['element']: Element supporting Text pattern.

        Returns:
            float: Font size as a float.
        """
        uia = container["uia"]
        pattern = Property._get_text_pattern_from_element(container)
        if uia == "UIA2":
            return float(pattern.DocumentRange.GetAttributeValue(AttributesUia2.FontSize))

        return float(pattern.DocumentRange.GetAttributeValue(AttributesUia3.FontSize))

    @staticmethod
    def _get_font_name(container: Container) -> str:
        """
        Return the font name from the Text DocumentRange.

        Args:
            container (Container): Container holding:
                - container['uia']: 'UIA2' or 'UIA3' string to select identifiers.
                - container['element']: Element supporting Text pattern.

        Returns:
            str: Font family/name string.
        """
        uia = container["uia"]
        pattern = Property._get_text_pattern_from_element(container)
        if uia == "UIA2":
            return str(pattern.DocumentRange.GetAttributeValue(AttributesUia2.FontName))

        return str(pattern.DocumentRange.GetAttributeValue(AttributesUia3.FontName))

    @staticmethod
    def _get_font_weight(container: Container) -> float:
        """
        Return the font weight value from the Text DocumentRange.

        Args:
            container (Container): Container holding:
                - container['uia']: 'UIA2' or 'UIA3' string to select identifiers.
                - container['element']: Element supporting Text pattern.

        Returns:
            float: Font weight as a float.
        """
        uia = container["uia"]
        pattern = Property._get_text_pattern_from_element(container)
        if uia == "UIA2":
            return float(pattern.DocumentRange.GetAttributeValue(AttributesUia2.FontWeight))

        return float(pattern.DocumentRange.GetAttributeValue(AttributesUia3.FontWeight))

    @staticmethod
    def _get_culture(container: Container) -> str:
        """
        Return the culture/locale associated with the text DocumentRange.

        Args:
            container (Container): Container holding:
                - container['uia']: 'UIA2' or 'UIA3' string to select identifiers.
                - container['element']: Element supporting Text pattern.

        Returns:
            str: Culture identifier string.

        Raises:
            FlaUiError: When culture is not supported for the UIA version (UIA2).
        """
        uia = container["uia"]
        pattern = Property._get_text_pattern_from_element(container)
        if uia == "UIA2":
            # See --> https://github.com/FlaUI/FlaUI/issues/554
            raise FlaUiError(FlaUiError.PropertyNotSupported)

        return str(pattern.DocumentRange.GetAttributeValue(AttributesUia3.Culture).ToString())

    @staticmethod
    def _is_hidden(container: Container) -> bool:
        """
        Return whether the text element is marked as hidden.

        Args:
            container (Container): Container holding:
                - container['uia']: 'UIA2' or 'UIA3' string to select identifiers.
                - container['element']: Element supporting Text pattern.

        Returns:
            bool: True if the element is hidden according to the Text pattern.
        """
        uia = container["uia"]
        pattern = Property._get_text_pattern_from_element(container)
        if uia == "UIA2":
            return Property._prop_to_bool(pattern.DocumentRange.GetAttributeValue(AttributesUia2.IsHidden))

        return Property._prop_to_bool(pattern.DocumentRange.GetAttributeValue(AttributesUia3.IsHidden))

    @staticmethod
    def _get_toggle_state(container: Container) -> str:
        """
        Return the toggle state of an element as an uppercase string.

        Args:
            container (Container): Container holding:
                - container['element']: Element supporting Toggle pattern.

        Returns:
            str: Toggle state string in uppercase.
        """
        pattern = Property._get_toggle_pattern_from_element(container)
        return str(pattern.ToggleState.Value.ToString()).upper()

    @staticmethod
    def _get_window_interaction_state(container: Container) -> str:
        """
        Return the window interaction state as a string.

        Args:
            container (Container): Container holding:
                - container['element']: Window element supporting Window pattern.

        Returns:
            str: Window interaction state string.
        """
        pattern = Property._get_window_pattern_from_element(container)
        return str(pattern.WindowInteractionState.Value.ToString())

    @staticmethod
    def _get_text_pattern_from_element(container: Container) -> Any:
        """
        Retrieve the Text pattern instance from the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            Any: Text pattern object.

        Raises:
            FlaUiError: If the Text pattern is not supported or not present.
        """
        element = container["element"]
        if Property._is_text_pattern_supported(container):
            pattern = element.Patterns.Text.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PropertyNotSupported)

    @staticmethod
    def _get_window_pattern_from_element(container: Container) -> Any:
        """
        Retrieve the Window pattern instance from the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            Any: Window pattern object.

        Raises:
            FlaUiError: If the Window pattern is not supported or not present.
        """
        element = container["element"]
        if Property._is_window_pattern_supported(container):
            pattern = element.Patterns.Window.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PropertyNotSupported)

    @staticmethod
    def _get_toggle_pattern_from_element(container: Container) -> Any:
        """
        Retrieve the Toggle pattern instance from the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            Any: Toggle pattern object.

        Raises:
            FlaUiError: If the Toggle pattern is not supported or not present.
        """
        element = container["element"]
        if Property._is_toggle_pattern_supported(container):
            pattern = element.Patterns.Toggle.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PropertyNotSupported)

    @staticmethod
    def _can_window_minimize(container: Container) -> bool:
        """
        Return whether the window can be minimized.

        Args:
            container (Container): Container holding:
                - container['element']: Window element supporting Window pattern.

        Returns:
            bool: True if the window can be minimized.
        """
        pattern = Property._get_window_pattern_from_element(container)
        return Property._prop_to_bool(pattern.CanMinimize)

    @staticmethod
    def _can_window_maximize(container: Container) -> bool:
        """
        Return whether the window can be maximized.

        Args:
            container (Container): Container holding:
                - container['element']: Window element supporting Window pattern.

        Returns:
            bool: True if the window can be maximized.
        """
        pattern = Property._get_window_pattern_from_element(container)
        return Property._prop_to_bool(pattern.CanMaximize)

    @staticmethod
    def _set_window_visual_state(container: Container) -> None:
        """
        Set the window visual state (Normal, Minimized, Maximized) for a window element.

        Args:
            container (Container): Container holding:
                - container['visual_state']: Property.WindowVisualState enum instance.
                - container['element']: Window element supporting Window pattern.
        """
        state = container["visual_state"].value
        pattern = Property._get_window_pattern_from_element(container)
        pattern.SetWindowVisualState(state)

    @staticmethod
    def _is_read_only(container: Container) -> bool:
        """
        Return whether the element's Value pattern reports it as read-only.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            bool: True when the element is read-only.

        Raises:
            FlaUiError: If the Value pattern is not supported.
        """
        element = container["element"]
        if Property._is_value_pattern_supported(container):
            pattern = element.Patterns.Value.Pattern
            if pattern is not None:
                return Property._prop_to_bool(pattern.IsReadOnly)

        raise FlaUiError(FlaUiError.PropertyNotSupported)

    @staticmethod
    def _is_window_pattern_supported(container: Container) -> bool:
        """
        Check whether the Window pattern is supported by the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            bool: True if Window pattern is supported, False otherwise.
        """
        element = container["element"]
        return Property._prop_to_bool(element.Patterns.Window.IsSupported)

    @staticmethod
    def _is_text_pattern_supported(container: Container) -> bool:
        """
        Check whether the Text pattern is supported by the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            bool: True if Text pattern is supported, False otherwise.
        """
        element = container["element"]
        return Property._prop_to_bool(element.Patterns.Text.IsSupported)

    @staticmethod
    def _is_toggle_pattern_supported(container: Container) -> bool:
        """
        Check whether the Toggle pattern is supported by the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            bool: True if Toggle pattern is supported, False otherwise.
        """
        element = container["element"]
        return Property._prop_to_bool(element.Patterns.Toggle.IsSupported)

    @staticmethod
    def _is_value_pattern_supported(container: Container) -> bool:
        """
        Check whether the Value pattern is supported by the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            bool: True if Value pattern is supported, False otherwise.
        """
        element = container["element"]
        return Property._prop_to_bool(element.Patterns.Value.IsSupported)

    @staticmethod
    def _is_rangevalue_pattern_supported(container: Container) -> bool:
        """
        Check whether the RangeValue pattern is supported by the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            bool: True if RangeValue pattern is supported, False otherwise.
        """
        element = container["element"]
        return Property._prop_to_bool(element.Patterns.RangeValue.IsSupported)

    @staticmethod
    def _is_expand_collapse_pattern_supported(container: Container) -> bool:
        """
        Check whether the ExpandCollapse pattern is supported by the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            bool: True if ExpandCollapse pattern is supported, False otherwise.
        """
        element = container["element"]
        return Property._prop_to_bool(element.Patterns.ExpandCollapse.IsSupported)

    @staticmethod
    def _is_selection_item_pattern_supported(container: Container) -> bool:
        """
        Check whether the SelectionItem pattern is supported by the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            bool: True if SelectionItem pattern is supported, False otherwise.
        """
        element = container["element"]
        return Property._prop_to_bool(element.Patterns.SelectionItem.IsSupported)

    @staticmethod
    def _get_expand_collapse_pattern_from_element(container: Container) -> Any:
        """
        Retrieve the ExpandCollapse pattern instance from the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            Any: ExpandCollapse pattern object.

        Raises:
            FlaUiError: If the ExpandCollapse pattern is not supported or not present.
        """
        element = container["element"]
        if Property._is_expand_collapse_pattern_supported(container):
            pattern = element.Patterns.ExpandCollapse.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PatternNotSupported.format("ExpandCollapse"))

    @staticmethod
    def _get_expand_collapse_pattern_state(container: Container) -> str:
        """
        Return the string representation of the control's ExpandCollapse state.

        Args:
            container (Container): Container holding:
                - container['element']: Element supporting ExpandCollapse pattern.

        Returns:
            str: ExpandCollapse state (e.g., 'Expanded' or 'Collapsed').

        Raises:
            FlaUiError: If the ExpandCollapse pattern is not supported.
        """
        pattern = Property._get_expand_collapse_pattern_from_element(container)
        return str(pattern.ExpandCollapseState)

    @staticmethod
    def _get_value_pattern_from_element(container: Container) -> Any:
        """
        Retrieve the Value pattern instance from the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            Any: Value pattern object.

        Raises:
            FlaUiError: If the Value pattern is not supported or not present.
        """
        element = container["element"]
        if Property._is_value_pattern_supported(container):
            pattern = element.Patterns.Value.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PatternNotSupported.format("Value"))

    @staticmethod
    def _get_value_from_value_pattern(container: Container) -> str:
        """
        Read the Value property from a Value pattern.

        Args:
            container (Container): Container holding:
                - container['element']: Element supporting Value pattern.

        Returns:
            str: Value as a string.

        Raises:
            FlaUiError: If the Value pattern is not supported.
        """
        pattern = Property._get_value_pattern_from_element(container)
        return str(pattern.Value)

    @staticmethod
    def _get_rangevalue_pattern_from_element(container: Container) -> Any:
        """
        Retrieve the RangeValue pattern instance from the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            Any: RangeValue pattern object.

        Raises:
            FlaUiError: If the RangeValue pattern is not supported or not present.
        """
        element = container["element"]

        if Property._is_rangevalue_pattern_supported(container):
            pattern = element.Patterns.RangeValue.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PatternNotSupported.format("RangeValue"))

    @staticmethod
    def _get_value_from_rangevalue_pattern(container: Container) -> str:
        """
        Read the current Value from a RangeValue pattern.

        Args:
            container (Container): Container holding:
                - container['element']: Element supporting RangeValue pattern.

        Returns:
            str: Current range value as a string.

        Raises:
            FlaUiError: If the RangeValue pattern is not supported.
        """
        pattern = Property._get_rangevalue_pattern_from_element(container)
        return str(pattern.Value)

    @staticmethod
    def _get_minimum_from_rangevalue_pattern(container: Container) -> str:
        """
        Read the Minimum value from a RangeValue pattern.

        Args:
            container (Container): Container holding:
                - container['element']: Element supporting RangeValue pattern.

        Returns:
            str: Minimum value as a string.

        Raises:
            FlaUiError: If the RangeValue pattern is not supported.
        """
        pattern = Property._get_rangevalue_pattern_from_element(container)
        return str(pattern.Minimum)

    @staticmethod
    def _get_maximum_from_rangevalue_pattern(container: Container) -> str:
        """
        Read the Maximum value from a RangeValue pattern.

        Args:
            container (Container): Container holding:
                - container['element']: Element supporting RangeValue pattern.

        Returns:
            str: Maximum value as a string.

        Raises:
            FlaUiError: If the RangeValue pattern is not supported.
        """
        pattern = Property._get_rangevalue_pattern_from_element(container)
        return str(pattern.Maximum)

    @staticmethod
    def _get_selection_item_pattern_from_element(container: Container) -> Any:
        """
        Retrieve the SelectionItem pattern instance from the element.

        Args:
            container (Container): Container holding:
                - container['element']: Element to query.

        Returns:
            Any: SelectionItem pattern object.

        Raises:
            FlaUiError: If the SelectionItem pattern is not supported or not present.
        """
        element = container["element"]

        if Property._is_selection_item_pattern_supported(container):
            pattern = element.Patterns.SelectionItem.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PatternNotSupported.format("SelectionItem"))

    @staticmethod
    def _is_selected(container: Container) -> bool:
        """
        Return whether the element is currently selected.

        Args:
            container (Container): Container holding:
                - container['element']: Element supporting SelectionItem pattern.

        Returns:
            bool: True when selected, False otherwise.

        Raises:
            FlaUiError: If the SelectionItem pattern is not supported.
        """
        pattern = Property._get_selection_item_pattern_from_element(container)
        return Property._prop_to_bool(pattern.IsSelected)

    @staticmethod
    def _stage_for_combobox_selectionitem(container: Container) -> None:
        """
        Temporarily change a combobox's expand/collapse state to allow selection.

        If the control is Expanded it will be Collapsed, and if Collapsed it will
        be Expanded. This prepares the control for selection actions.

        Args:
            container (Container): Container holding:
                - container['element']: The combobox control instance.
        """
        element = container["element"]
        state = Property._get_expand_collapse_pattern_state(container)
        if state == "Expanded":
            element.Collapse()
        if state == "Collapsed":
            element.Expand()

    @staticmethod
    def _get_help_text(container: Container) -> str:
        """
        Return the HelpText property of the given element.

        Args:
            container (Container): Container holding:
                - container['element']: Element with a `Properties.HelpText` property.

        Returns:
            str: The element's help text as a string. Returns an empty string when
                 the property exists but is `None`.

        Raises:
            FlaUiError: Raised with `FlaUiError.PropertyNotSupported` when the
                        help text cannot be retrieved or the property is unsupported.
        """
        try:
            element = container["element"]
            help_text = element.Properties.HelpText.Value
            if help_text is not None:
                return str(help_text)
            return ""
        except Exception:
            raise FlaUiError(FlaUiError.PropertyNotSupported) from None

    @staticmethod
    def _int_to_rgba(argb_int: int) -> Tuple[int, int, int, int]:
        """
        Convert a 32-bit ARGB integer to an (R, G, B, A) tuple.

        Args:
            argb_int (int): 32-bit integer containing ARGB channels.

        Returns:
            Tuple[int, int, int, int]: Red, green, blue, alpha components (0-255).
        """
        blue = argb_int & 255
        green = (argb_int >> 8) & 255
        red = (argb_int >> 16) & 255
        alpha = (argb_int >> 24) & 255
        return red, green, blue, alpha

    @staticmethod
    def _prop_to_bool(prop: Any) -> bool:
        """
        Convert a provided automation property value to a Python boolean.

        Args:
            prop (Any): Value returned from a FlaUI property. May be a native
                Python bool or a FlaUI AutomationProperty wrapper with a
                Valueattribute.

        Returns:
            bool: Converted boolean value.
        """

        if isinstance(prop, bool):
            return bool(prop)

        # Should be from type FlaUI.Core.AutomationProperty[Boolean]
        return bool(prop.Value)
