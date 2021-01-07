from enum import Enum
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface


class ToggleButton(ModuleInterface):
    """
    ToggleButton module wrapper for FlaUI usage.
    Wrapper module executes methods from ToggleButton.cs implementation.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        GET_TOGGLE_BUTTON_STATE = "GET_TOGGLE_BUTTON_STATE"
        SET_TOGGLE_BUTTON_STATE = "SET_TOGGLE_BUTTON_STATE"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.GET_CHECKBOX_STATE
            * Values (Array): [Element]
            * Returns : True/False from given checkbox element.

          *  Action.SET_CHECKBOX_STATE
            * Values (Array): [Element, True/False]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_TOGGLE_BUTTON_STATE: lambda: values[0].IsChecked,
            self.Action.SET_TOGGLE_BUTTON_STATE: lambda: ToggleButton._set_toggle_button_state(values[0], values[1])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _set_toggle_button_state(element, value):
        """Set toggle button state from element.

        Args:
            element (Object): Toggle button element from FlaUI.
            value (Object): True/False to set checkbox state.
        """
        element.IsChecked = value
