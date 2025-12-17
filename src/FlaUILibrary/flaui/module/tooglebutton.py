from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.exception.flauierror import FlaUiError


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

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        TOGGLE = "TOGGLE_BUTTON_TOGGLE"

    @staticmethod
    def create_value_container(element:Any=None) -> Container:
        """
        Helper to create container object.

        Args:
            element (Object): FlaUi ToggleButton element
        """
        return ToggleButton.Container(element=element)

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
            self.Action.TOGGLE: lambda: self._toggle(values),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _toggle(container: Container) -> None:
        """
        Toggle the state of the provided ToggleButton element.

        Args:
            container (ToggleButton.Container): Container holding the target element.
                - container['element']: FlaUI ToggleButton element to toggle.

        Raises:
            FlaUiError: If the container does not contain a valid toggle element,
                if the element does not support the toggle operation, or if the
                underlying call fails.
        """
        element = container["element"]
        element.Toggle()
