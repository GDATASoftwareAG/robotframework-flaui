from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
from FlaUILibrary.flaui.util.converter import Converter


class Textbox(ModuleInterface):
    """
    Textbox module wrapper for FlaUI usage.
    Wrapper module executes methods from Textbox.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from textbox module.
        """
        element: Optional[Any]
        value: Optional[str]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        SET_TEXT_TO_TEXTBOX = "SET_TEXT_TO_TEXTBOX"
        GET_TEXT_FROM_TEXTBOX = "GET_TEXT_FROM_TEXTBOX"

    @staticmethod
    def create_value_container(element=None, value=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (String): Textbox element to use
            value (String): Value to set to textbox
        """
        return Textbox.Container(element=element,
                                 value=Converter.cast_to_string(value))

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.GET_TEXT_FROM_TEXTBOX
            * Values ["element"]
            * Returns (String) : Text from textbox.

          *  Action.SET_TEXT_TO_TEXTBOX
            * Values ["element", "value"]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_TEXT_FROM_TEXTBOX: lambda: values["element"].Text,
            self.Action.SET_TEXT_TO_TEXTBOX: lambda: self._set_textbox_text(values["element"], values["value"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _set_textbox_text(element: Any, value: str):
        """
        Set textbox text.

        Args:
            element (Object): Textbox element from FlaUI.
            value (String): String value to set to textbox.
        """
        element.Text = value
