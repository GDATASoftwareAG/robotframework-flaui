from enum import Enum
from typing import Optional, Any
import FlaUI.Core.Input  # pylint: disable=import-error
from FlaUI.Core.Exceptions import NoClickablePointException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


class Mouse(ModuleInterface):
    """
    Mouse module wrapper for FlaUI usage.
    Wrapper module executes methods from Mouse.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from mouse module.
        """
        element: Optional[Any]
        second_element: Optional[Any]

    class Action(Enum):
        """Supported actions for execute action implementation."""
        LEFT_CLICK = "LEFT_CLICK"
        RIGHT_CLICK = "RIGHT_CLICK"
        DOUBLE_CLICK = "DOUBLE_CLICK"
        MOVE_TO = "MOVE_TO"
        DRAG_AND_DROP = "DRAG_AND_DROP"

    @staticmethod
    def create_value_container(element=None, second_element=None):
        """
        Helper to create container object.

        Args:
            element (Object): Element to click
            second_element (Object): To Element from drag and drop
        """
        return Mouse.Container(element=element, second_element=second_element)

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.LEFT_CLICK, RIGHT_CLICK, DOUBLE_CLICK, MOVE_TO
            * Values ["element"] : UIA3 Element from FlaUI to interact
            * Returns : None

         *  Action.DRAG_AND_DROP
            * Values ["element", "second_element"] : UIA3 Elements from FlaUI to drag and drop
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.LEFT_CLICK: lambda: self._click(values["element"]),
            self.Action.RIGHT_CLICK: lambda: self._right_click(values["element"]),
            self.Action.DOUBLE_CLICK: lambda: self._double_click(values["element"]),
            self.Action.MOVE_TO: lambda: self._move_to(values["element"]),
            self.Action.DRAG_AND_DROP: lambda: self._drag_and_drop(values["element"], values["second_element"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _click(element: Any):
        try:
            return element.Click()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _right_click(element: Any):
        try:
            return element.RightClick()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _double_click(element: Any):
        try:
            return element.DoubleClick()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _move_to(element: Any):
        try:
            FlaUI.Core.Input.Mouse.MoveTo(element.GetClickablePoint())
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _drag_and_drop(element_from: Any, element_to: Any):
        try:
            FlaUI.Core.Input.Mouse.Drag(element_from.GetClickablePoint(), element_to.GetClickablePoint())
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None
