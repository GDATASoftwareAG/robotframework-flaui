from enum import Enum
from typing import Optional, Any
from FlaUI.Core.Exceptions import PatternNotSupportedException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


class Button(ModuleInterface):
    """
    Button control module wrapper for FlaUI usage.
    Wrapper module executes methods from Application class implementation by Button.cs.
    """

    class Container(ValueContainer):
        """
        Value container from selector module.
        """
        element: Optional[Any]
        xpath: Optional[str]

    class Action(Enum):
        """Supported actions for execute action implementation."""
        INVOKE_BUTTON = "INVOKE_BUTTON"

    @staticmethod
    def create_value_container(xpath=None, element=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): Invokable element.
        """
        return Button.Container(xpath=xpath, element=element)

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action: Action to use.
            values: See supported action definitions for value usage and value container definition.
        """

        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.INVOKE_BUTTON: lambda: self._invoke(values["xpath"],values["element"]),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _invoke(xpath, element):
        try:
            element.Invoke()
        except PatternNotSupportedException:
            raise FlaUiError(FlaUiError.ElementNotInvokable.format(xpath)) from None
