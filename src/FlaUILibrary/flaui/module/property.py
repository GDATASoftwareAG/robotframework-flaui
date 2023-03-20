from enum import Enum
from typing import Optional, Any
from FlaUI.UIA2.Identifiers import TextAttributes as AttributesUia2  # pylint: disable=import-error
from FlaUI.UIA3.Identifiers import TextAttributes as AttributesUia3  # pylint: disable=import-error
from FlaUI.Core.Definitions import WindowVisualState  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


class Property(ModuleInterface):
    """
    Property module wrapper for FlaUI usage to get property values from elements.
    """

    class Container(ValueContainer):
        """
        Value container from property module.
        """
        element: Optional[Any]
        uia: str

    class Action(Enum):
        """Supported actions for execute action implementation."""
        FOREGROUND_COLOR = "FOREGROUND_COLOR"
        BACKGROUND_COLOR = "BACKGROUND_COLOR"
        FONT_SIZE = "FONT_SIZE"
        FONT_NAME = "FONT_NAME"
        FONT_WEIGHT = "FONT_WEIGHT"
        CULTURE = "CULTURE"
        IS_HIDDEN = "IS_HIDDEN"
        WINDOW_VISUAL_STATE = "WINDOW_VISUAL_STATE"
        WINDOW_INTERACTION_STATE = "WINDOW_INTERACTION_STATE"
        TOGGLE_STATE = "TOGGLE_STATE"
        MAXIMIZE_WINDOW = "MAXIMIZE_WINDOW"
        MINIMIZE_WINDOW = "MINIMIZE_WINDOW"
        NORMALIZE_WINDOW = "NORMALIZE_WINDOW"
        CAN_WINDOW_MINIMIZE = "CAN_WINDOW_MINIMIZE"
        CAN_WINDOW_MAXIMIZE = "CAN_WINDOW_MAXIMIZE"

    @staticmethod
    def create_value_container(element: Any = None, uia: str = None) -> Container:
        """
        Helper to create container object.

        Args:
            element (Object): Element to grab property.
            uia (string): User interface identifier
        """
        return Property.Container(element=element, uia=uia)

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.FOREGROUND_COLOR
            * Values ["element", "uia"] : Element to get foreground color property from uia2 or uia3.
            * Returns : Foreground color as (a,r,g,b) tuple.

         *  Action.BACKGROUND_COLOR
            * Values ["element", "uia"] : Element to get background color property from uia2 or uia3.
            * Returns : Foreground color as (a,r,g,b) tuple.

         *  Action.FONT_SIZE
            * Values ["element", "uia"] : Element to get font size property from uia2 or uia3.
            * Returns : Font size as floating point value

         *  Action.FONT_NAME
            * Values ["element", "uia"] : Element to get font name property from uia2 or uia3.
            * Returns : String name from font

         *  Action.FONT_WEIGHT
            * Values ["element", "uia"] : Element to get font weight property from uia2 or uia3.
            * Returns : Font weight as floating point value

         *  Action.CULTURE
            * Values ["element", "uia"] : Element to get culture property from uia2 or uia3.
            * Returns : Culture property as string

         *  Action.IS_HIDDEN
            * Values ["element", "uia"] : Element to get culture property from uia2 or uia3.
            * Returns : Bool if element is hidden.

         *  Action.WINDOW_VISUAL_STATE
            * Values ["element"] : Element to get window visual state property from window.
            * Returns : String from visual state.

         *  Action.WINDOW_INTERACTION_STATE
            * Values ["element"] : Element to get window visual state property from window.
            * Returns : String from window interaction state.

         *  Action.TOGGLE_STATE
            * Values ["element", "uia"] : Element to get toggle state property from uia2 or uia3 element.
            * Returns : String from toggle state like ON, OFF, Intermediate as string.

         *  Action.MAXIMIZE_WINDOW
            * Values ["element"] : Maximize window
            * Returns : None

         *  Action.MINIMIZE_WINDOW
            * Values ["element"] : Minimize window
            * Returns : None

         *  Action.NORMALIZE_WINDOW
            * Values ["element"] : Normalize window
            * Returns : None

         *  Action.CAN_WINDOW_MINIMIZE
            * Values ["element"] : Verification if window can be minimized.
            * Returns : Return True if supported otherwise False

         *  Action.CAN_WINDOW_MAXIMIZE
            * Values ["element"] : Verification if window can be maximized.
            * Returns : Return True if supported otherwise False

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.FOREGROUND_COLOR: lambda: self._get_foreground_color(values["element"], values["uia"]),
            self.Action.BACKGROUND_COLOR: lambda: self._get_background_color(values["element"], values["uia"]),
            self.Action.FONT_SIZE: lambda: self._get_font_size(values["element"], values["uia"]),
            self.Action.FONT_NAME: lambda: self._get_font_name(values["element"], values["uia"]),
            self.Action.FONT_WEIGHT: lambda: self._get_font_weight(values["element"], values["uia"]),
            self.Action.CULTURE: lambda: self._get_culture(values["element"], values["uia"]),
            self.Action.IS_HIDDEN: lambda: self._is_hidden(values["element"], values["uia"]),
            self.Action.WINDOW_VISUAL_STATE: lambda: self._get_window_visual_state(values["element"]),
            self.Action.WINDOW_INTERACTION_STATE: lambda : self._get_window_interaction_state(values["element"]),
            self.Action.TOGGLE_STATE: lambda: self._get_toggle_state(values["element"]),
            self.Action.MAXIMIZE_WINDOW: lambda: self._set_window_visual_state(values["element"],
                                                                               WindowVisualState.Maximized),
            self.Action.MINIMIZE_WINDOW: lambda: self._set_window_visual_state(values["element"],
                                                                               WindowVisualState.Minimized),
            self.Action.NORMALIZE_WINDOW: lambda: self._set_window_visual_state(values["element"],
                                                                                WindowVisualState.Normal),
            self.Action.CAN_WINDOW_MAXIMIZE: lambda: self._can_window_maximize(values["element"]),
            self.Action.CAN_WINDOW_MINIMIZE: lambda: self._can_window_minimize(values["element"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_window_visual_state(element: Any) -> str:
        pattern = Property._get_window_pattern_from_element(element)
        return str(pattern.WindowVisualState.Value.ToString())

    @staticmethod
    def _get_foreground_color(element: Any, uia: str) -> int:
        pattern = Property._get_text_pattern_from_element(element)
        if uia == "UIA2":
            return Property._int_to_rgba(pattern.DocumentRange.GetAttributeValue(AttributesUia2.ForegroundColor))

        return Property._int_to_rgba(pattern.DocumentRange.GetAttributeValue(AttributesUia3.ForegroundColor))

    @staticmethod
    def _get_background_color(element: Any, uia: str) -> (int, int, int, int):
        pattern = Property._get_text_pattern_from_element(element)
        if uia == "UIA2":
            return Property._int_to_rgba(pattern.DocumentRange.GetAttributeValue(AttributesUia2.BackgroundColor))

        return Property._int_to_rgba(pattern.DocumentRange.GetAttributeValue(AttributesUia3.BackgroundColor))

    @staticmethod
    def _get_font_size(element: Any, uia: str) -> (int, int, int, int):
        pattern = Property._get_text_pattern_from_element(element)
        if uia == "UIA2":
            return float(pattern.DocumentRange.GetAttributeValue(AttributesUia2.FontSize))

        return float(pattern.DocumentRange.GetAttributeValue(AttributesUia3.FontSize))

    @staticmethod
    def _get_font_name(element: Any, uia: str) -> str:
        pattern = Property._get_text_pattern_from_element(element)
        if uia == "UIA2":
            return str(pattern.DocumentRange.GetAttributeValue(AttributesUia2.FontName))

        return str(pattern.DocumentRange.GetAttributeValue(AttributesUia3.FontName))

    @staticmethod
    def _get_font_weight(element: Any, uia: str) -> float:
        pattern = Property._get_text_pattern_from_element(element)
        if uia == "UIA2":
            return float(pattern.DocumentRange.GetAttributeValue(AttributesUia2.FontWeight))

        return float(pattern.DocumentRange.GetAttributeValue(AttributesUia3.FontWeight))

    @staticmethod
    def _get_culture(element: Any, uia: str) -> str:
        pattern = Property._get_text_pattern_from_element(element)
        if uia == "UIA2":
            # See --> https://github.com/FlaUI/FlaUI/issues/554
            raise FlaUiError(FlaUiError.PropertyNotSupported)

        return str(pattern.DocumentRange.GetAttributeValue(AttributesUia3.Culture).ToString())

    @staticmethod
    def _is_hidden(element: Any, uia: str) -> bool:
        pattern = Property._get_text_pattern_from_element(element)
        if uia == "UIA2":
            return bool(pattern.DocumentRange.GetAttributeValue(AttributesUia2.IsHidden))

        return bool(pattern.DocumentRange.GetAttributeValue(AttributesUia3.IsHidden))

    @staticmethod
    def _get_toggle_state(element: Any) -> str:
        pattern = Property._get_toggle_pattern_from_element(element)
        return str(pattern.ToggleState.Value.ToString()).upper()

    @staticmethod
    def _get_window_interaction_state(element: Any):
        pattern = Property._get_window_pattern_from_element(element)
        return str(pattern.WindowInteractionState.Value.ToString())

    @staticmethod
    def _get_text_pattern_from_element(element) -> Any:
        if element.Patterns.Text.IsSupported:
            pattern = element.Patterns.Text.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PropertyNotSupported)

    @staticmethod
    def _get_window_pattern_from_element(element) -> Any:
        if element.Patterns.Window.IsSupported:
            pattern = element.Patterns.Window.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PropertyNotSupported)

    @staticmethod
    def _get_toggle_pattern_from_element(element) -> Any:
        if element.Patterns.Toggle.IsSupported:
            pattern = element.Patterns.Toggle.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PropertyNotSupported)

    @staticmethod
    def _can_window_minimize(element: Any) -> bool:
        pattern = Property._get_window_pattern_from_element(element)
        return bool(pattern.CanMinimize)

    @staticmethod
    def _can_window_maximize(element: Any) -> bool:
        pattern = Property._get_window_pattern_from_element(element)
        return bool(pattern.CanMaximize)

    @staticmethod
    def _set_window_visual_state(element: Any, window_visual_state: Any) -> None:
        pattern = Property._get_window_pattern_from_element(element)
        pattern.SetWindowVisualState(window_visual_state)

    @staticmethod
    def _int_to_rgba(argb_int: int) -> (int, int, int, int):
        blue = argb_int & 255
        green = (argb_int >> 8) & 255
        red = (argb_int >> 16) & 255
        alpha = (argb_int >> 24) & 255
        return red, green, blue, alpha
