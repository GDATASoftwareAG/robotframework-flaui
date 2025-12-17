from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
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
        SET_TEXT_TO_TEXTBOX = "TEXTBOX_SET_TEXT"
        GET_TEXT_FROM_TEXTBOX = "TEXTBOX_GET_TEXT"

    @staticmethod
    def create_value_container(element=None, value=None) -> Container:
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

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_TEXT_FROM_TEXTBOX:
                lambda: self._get_textbox_text(values),
            self.Action.SET_TEXT_TO_TEXTBOX:
                lambda: self._set_textbox_text(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _set_textbox_text(container: Container) -> None:
        """
        Set the text of a FlaUI textbox element.

        Args:
            container (Textbox.Container): Container holding:
                - container['element']: FlaUI textbox element whose `Text` property will be set.
                - container['value']: String value to assign to the textbox.

        Raises:
            FlaUiError: If the container does not provide a valid textbox element
                or if setting the `Text` property fails.
        """
        element = container["element"]
        value = container["value"]
        element.Text = value

    @staticmethod
    def _get_textbox_text(container: Container) -> str:
        """
        Retrieve the text value from a FlaUI textbox element.

        Args:
            container (Textbox.Container): Container holding:
                - container['element']: FlaUI textbox element whose `Text` property will be read.

        Returns:
            str: The current text value of the textbox (converted to `str`).

        Raises:
            FlaUiError: If the container does not provide a valid textbox element
                or if reading the `Text` property fails.
        """
        element = container["element"]
        return str(element.Text)
