from enum import Enum
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface


class Textbox(ModuleInterface):
    """
    Textbox module wrapper for FlaUI usage.
    Wrapper module executes methods from Textbox.cs implementation.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        SET_TEXT_TO_TEXTBOX = "SET_TEXT_TO_TEXTBOX"
        GET_TEXT_FROM_TEXTBOX = "GET_TEXT_FROM_TEXTBOX"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.GET_TEXT_FROM_TEXTBOX
            * Values (Array) : [Element]
            * Returns (String) : Text from textbox.

          *  Action.SET_TEXT_TO_TEXTBOX
            * Values (Array): [Element, String]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_TEXT_FROM_TEXTBOX: lambda: values.Text,
            self.Action.SET_TEXT_TO_TEXTBOX: lambda: Textbox._set_textbox_text(values[0], values[1])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _set_textbox_text(element, value):
        """Set textbox text.

        Args:
            element (Object): Textbox element from FlaUI.
            value (String): String value to set to textbox.
        """
        element.Text = value
