from enum import Enum
from typing import Optional, Any
from FlaUI.UIA2.Identifiers import TextAttributes as AttributesUia2  # pylint: disable=import-error
from FlaUI.UIA3.Identifiers import TextAttributes as AttributesUia3  # pylint: disable=import-error
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
    def _int_to_rgba(argb_int: int) -> (int, int, int, int):
        blue = argb_int & 255
        green = (argb_int >> 8) & 255
        red = (argb_int >> 16) & 255
        alpha = (argb_int >> 24) & 255
        return red, green, blue, alpha
