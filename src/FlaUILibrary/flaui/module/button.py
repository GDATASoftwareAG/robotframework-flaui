from enum import Enum
from typing import Optional, Any
from FlaUI.Core.Exceptions import PatternNotSupportedException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer


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
        """
        Supported actions for execute action implementation.
        """
        INVOKE_BUTTON = "BUTTON_INVOKE"

    @staticmethod
    def create_value_container(xpath=None, element=None) -> Container:
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            xpath (str): Xpath from element to invoke.
            element (Object): Invokable element.
        """
        return Button.Container(xpath=xpath, element=element)

    def execute_action(self, action: Action, values: Container) -> Any:
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
            self.Action.INVOKE_BUTTON: lambda: self._invoke(values),
        }
        # pylint: enable=unnecessary-lambda

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _invoke(container: Container) -> None:
        """
        Invoke (activate) the button element.

        Args:
            container (Button.Container): Container holding:
                - container['element']: The invokable button element (must implement `Invoke()`).
                - container['xpath']: Optional xpath used in error messages.

        Raises:
            FlaUiError: If the element does not support the Invoke pattern or invocation fails.
        """
        try:
            element = container["element"]
            element.Invoke()
        except PatternNotSupportedException:
            xpath = container["xpath"]
            raise FlaUiError(FlaUiError.ElementNotInvokable.format(xpath)) from None
