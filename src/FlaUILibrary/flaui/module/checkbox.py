from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
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
        GET_CHECKBOX_BUTTON_STATE = "CHECKBOX_GET_BUTTON_STATE"
        SET_CHECKBOX_BUTTON_STATE = "CHECKBOX_SET_BUTTON_STATE"

    @staticmethod
    def create_value_container(element=None, state=None) -> Container:
        """
        Helper to create container object.

        Args:
            element (Object): Checkbox or Radiobutton element
            state (bool): Value to set True or False
        """
        return Checkbox.Container(element=element,
                                  state=Converter.cast_to_bool(state))

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action: Action to use.
            values: See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_CHECKBOX_BUTTON_STATE:
                lambda: self._is_checked(values),
            self.Action.SET_CHECKBOX_BUTTON_STATE:
                lambda: self._set_state(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _is_checked(container: Container) -> bool:
        """
        Return whether the checkbox or radiobutton element is currently checked.

        Args:
            container (Checkbox.Container): Container holding:
                - container['element']: FlaUI Toggle/Checkbox element exposing `IsChecked`.

        Returns:
            bool: True if the element is checked, False otherwise.

        Raises:
            FlaUiError: If the element is missing or does not expose `IsChecked`.
        """
        return container["element"].IsChecked

    @staticmethod
    def _set_state(container: Container) -> None:
        """
        Set the checked state of a checkbox or radiobutton element.

        Args:
            element (Any): FlaUI Toggle/Checkbox element to update.
            state (Optional[bool]): Desired state; will be cast to a boolean.

        Raises:
            FlaUiError: If the element is missing or the assignment fails.
        """
        element = container["element"]
        state = container["state"]
        element.IsChecked = state
