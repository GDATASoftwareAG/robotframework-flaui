from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer


class Combobox(ModuleInterface):
    """
    Combobox control module wrapper for FlaUI usage.
    Wrapper module executes methods from Application class implementation by Combobox.cs.
    Wrapper module is split up by selector.py and combobox.py
    """

    class Container(ValueContainer):
        """
        Value container from selector module.
        """
        element: Optional[Any]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        COLLAPSE_COMBOBOX = "COMBOBOX_COLLAPSE"
        EXPAND_COMBOBOX = "COMBOBOX_EXPAND"

    @staticmethod
    def create_value_container(element=None) -> Container:
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): Combobox element.
        """
        return Combobox.Container(element=None if not element else element)

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
            self.Action.EXPAND_COMBOBOX:
                lambda: self._expand(values),
            self.Action.COLLAPSE_COMBOBOX:
                lambda: self._collapse(values),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _expand(container: Container) -> None:
        """
        Expand the combobox control.

        Args:
            container (Combobox.Container): Container holding:
                - container['element']: The combobox control instance to expand.

        Raises:
            FlaUiError: If the element is missing or the expand operation fails.
        """
        container["element"].Expand()

    @staticmethod
    def _collapse(container: Container) -> None:
        """
        Collapse the combobox control.

        Args:
            container (Combobox.Container): Container holding:
                - container['element']: The combobox control instance to collapse.

        Raises:
            FlaUiError: If the element is missing or the collapse operation fails.
        """
        container["element"].Collapse()
