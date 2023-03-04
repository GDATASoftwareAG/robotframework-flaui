from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
from FlaUILibrary.flaui.util.converter import Converter


class Checkbox(ModuleInterface):
    """
    Checkbox module wrapper for FlaUI usage.
    Wrapper module executes methods from Radiobutton.cs and Checkbox.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from checkbox module.
        """
        element: Optional[Any]
        state: Optional[bool]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        GET_CHECKBOX_BUTTON_STATE = "GET_CHECKBOX_BUTTON_STATE"
        SET_CHECKBOX_BUTTON_STATE = "SET_CHECKBOX_BUTTON_STATE"

    @staticmethod
    def create_value_container(element=None, state=None):
        """
        Helper to create container object.

        Args:
            element (Object): Checkbox or Radiobutton element
            state (bool): Value to set True or False
        """
        return Checkbox.Container(element=element,
                                  state=Converter.cast_to_bool(state))

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.GET_TOGGLE_BUTTON_STATE
            * Values  : ["element"]
            * Returns : True/False from given checkbox element.

          *  Action.SET_TOGGLE_BUTTON_STATE
            * Values  : ["element", "state"]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action: Action to use.
            values: See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_CHECKBOX_BUTTON_STATE: lambda: values["element"].IsChecked,
            self.Action.SET_CHECKBOX_BUTTON_STATE: lambda: self._set_state(values["element"], values["state"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _set_state(element: Any, state: bool):
        """
        Set toggle button state from element.

        Args:
            element : Toggle button element from FlaUI.
            state   : True/False to set checkbox state.
        """
        element.IsChecked = state
