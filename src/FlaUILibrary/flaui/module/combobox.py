from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


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
        """Supported actions for execute action implementation."""
        COLLAPSE_COMBOBOX = "COLLAPSE_COMBOBOX"
        EXPAND_COMBOBOX = "EXPAND_COMBOBOX"

    @staticmethod
    def create_value_container(element=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): Combobox element.
        """
        return Combobox.Container(element=None if not element else element)

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.COLLAPSE
            * Values ["element"] : Combobox element to collapse
            * Returns : None

          *  Action.EXPAND
            * Values ["element"] : Combobox element to expand
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action: Action to use.
            values: See supported action definitions for value usage and value container definition.
        """

        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.EXPAND_COMBOBOX: lambda: values["element"].Expand(),
            self.Action.COLLAPSE_COMBOBOX: lambda: values["element"].Collapse(),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()
