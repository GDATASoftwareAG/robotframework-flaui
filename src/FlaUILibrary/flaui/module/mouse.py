from enum import Enum
import FlaUI.Core.Input  # pylint: disable=import-error
from FlaUI.Core.Exceptions import NoClickablePointException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface


class Mouse(ModuleInterface):
    """
    Mouse module wrapper for FlaUI usage.
    Wrapper module executes methods from Mouse.cs implementation.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        LEFT_CLICK = "LEFT_CLICK"
        RIGHT_CLICK = "RIGHT_CLICK"
        DOUBLE_CLICK = "DOUBLE_CLICK"
        MOVE_TO = "MOVE_TO"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.LEFT_CLICK, RIGHT_CLICK, DOUBLE_CLICK, MOVE_TO
            * Values (Object): UIA3 Element from FlaUI to interact
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.LEFT_CLICK: lambda: Mouse._click(values),
            self.Action.RIGHT_CLICK: lambda: Mouse._right_click(values),
            self.Action.DOUBLE_CLICK: lambda: Mouse._double_click(values),
            self.Action.MOVE_TO: lambda: Mouse._move_to(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _click(element):
        try:
            return element.Click()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _right_click(element):
        try:
            return element.RightClick()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _double_click(element):
        try:
            return element.DoubleClick()
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _move_to(element):
        try:
            FlaUI.Core.Input.Mouse.MoveTo(element.GetClickablePoint())
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None
