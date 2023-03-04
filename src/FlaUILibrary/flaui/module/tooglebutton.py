from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


class ToggleButton(ModuleInterface):
    """
    ToggleButton module wrapper for FlaUI usage.
    Wrapper module executes methods from ToggleButton.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from toggle button module.
        """
        element: Optional[Any]
        state: Optional[bool]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        TOGGLE = "TOGGLE"

    @staticmethod
    def create_value_container(element=None):
        """
        Helper to create container object.

        Args:
            element (Object): ToggleButton element
        """
        return ToggleButton.Container(element=element)

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.TOGGLE
            * Values  : ["element"]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action: Action to use.
            values: See action definitions for value usage.
        """

        switcher = {
            self.Action.TOGGLE: lambda: self._toggle(values["element"]),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _toggle(element: Any) -> None:
        element.Toggle()
