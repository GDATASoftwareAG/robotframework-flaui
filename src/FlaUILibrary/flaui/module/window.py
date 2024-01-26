from enum import Enum
from typing import Optional, Any
from FlaUI.Core.Exceptions import MethodNotSupportedException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


class Window(ModuleInterface):
    """
    Window module wrapper for FlaUI usage.
    Wrapper module executes methods from Window.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from window module.
        """
        element: Optional[Any]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        CLOSE_WINDOW = "CLOSE_WINDOW"

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.CLOSE_WINDOW
            * Values ["element"]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.CLOSE_WINDOW: lambda: self._close_window(values["element"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _close_window(window: Any):
        """
        Try to close window element.

        Args:
            window (Object): Window element to close.

        Raises:
            FlaUiError: If window could not be closed.
        """
        try:
            window.Close()
        except MethodNotSupportedException:
            raise FlaUiError(FlaUiError.WindowCloseNotSupported) from None
