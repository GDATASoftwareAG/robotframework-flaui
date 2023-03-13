from enum import Enum
from typing import Optional, Any
import time
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
        timeout_in_ms: Optional[int]

    class Action(Enum):
        """Supported actions for execute action implementation."""
        LEFT_CLICK = "LEFT_CLICK"
        RIGHT_CLICK = "RIGHT_CLICK"
        DOUBLE_CLICK = "DOUBLE_CLICK"
        LEFT_CLICK_HOLD = "LEFT_CLICK_HOLD"
        RIGHT_CLICK_HOLD = "RIGHT_CLICK_HOLD"
        DOUBLE_CLICK_HOLD = "DOUBLE_CLICK_HOLD"
        MOVE_TO = "MOVE_TO"
        DRAG_AND_DROP = "DRAG_AND_DROP"

    @staticmethod
    def create_value_container(element=None, second_element=None, timeout_in_ms=None):
        """
        Helper to create container object.

        Args:
            element (Object): Element to click
            second_element (Object): To Element from drag and drop
        """
        return Mouse.Container(element=element, second_element=second_element, timeout_in_ms=timeout_in_ms)

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.LEFT_CLICK, RIGHT_CLICK, DOUBLE_CLICK, MOVE_TO
            * Values ["element"] : UIA3 Element from FlaUI to interact
            * Returns : None

          *  Action.LEFT_CLICK_HOLD, RIGHT_CLICK_HOLD, DOUBLE_CLICK_HOLD,
            * Values ["element","timeout"] : UIA3 Element from FlaUI to interact
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
            self.Action.LEFT_CLICK_HOLD: lambda: self._click_hold(values["element"], values["timeout_in_ms"]),
            self.Action.RIGHT_CLICK_HOLD: lambda: self._right_click_hold(values["element"], values["timeout_in_ms"]),
            self.Action.DOUBLE_CLICK_HOLD: lambda: self._double_click_hold(values["element"], values["timeout_in_ms"]),
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
    def _click_hold(element: Any, timeout_in_ms: int):
        try:
            FlaUI.Core.Input.Mouse.Position = element.GetClickablePoint()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None
        FlaUI.Core.Input.Mouse.Down()
        time.sleep(float(timeout_in_ms)/1000)
        FlaUI.Core.Input.Mouse.Up()

    @staticmethod
    def _right_click(element: Any):
        try:
            return element.RightClick()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _right_click_hold(element: Any, timeout_in_ms: int):
        try:
            FlaUI.Core.Input.Mouse.Position = element.GetClickablePoint()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None
        FlaUI.Core.Input.Mouse.Down(FlaUI.Core.Input.MouseButton.Right)
        time.sleep(float(timeout_in_ms)/1000)
        FlaUI.Core.Input.Mouse.Up(FlaUI.Core.Input.MouseButton.Right)

    @staticmethod
    def _double_click(element: Any):
        try:
            return element.DoubleClick()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _double_click_hold(element: Any, timeout_in_ms: int):
        try:
            FlaUI.Core.Input.Mouse.Position = element.GetClickablePoint()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None
        FlaUI.Core.Input.Mouse.Down()
        FlaUI.Core.Input.Mouse.Up()
        FlaUI.Core.Input.Mouse.Down()
        time.sleep(float(timeout_in_ms)/1000)
        FlaUI.Core.Input.Mouse.Up()

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
