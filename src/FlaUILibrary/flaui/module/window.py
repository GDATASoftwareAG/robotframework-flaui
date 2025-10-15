import time
from enum import Enum
from typing import Optional, Any
from FlaUI.Core.Exceptions import MethodNotSupportedException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


class Window(ModuleInterface):
    """
    Window module wrapper for FlaUI usage.
    Wrapper module executes methods from Window.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from window module.
        """
        element: Optional[Any]
        width: Optional[int]
        height: Optional[int]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        CLOSE_WINDOW = "CLOSE_WINDOW"
        RESIZE_WINDOW = "RESIZE_WINDOW"

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.CLOSE_WINDOW
            * Values ["element"]

          *  Action.RESIZE_WINDOW
            * Values ["element", "width", "height"]

        Raises:
            FlaUiError: If action is not supported.
        """

        switcher = {
            self.Action.CLOSE_WINDOW: lambda: self._close_window(values["element"]),
            self.Action.RESIZE_WINDOW: lambda: self._resize_window(
                values["element"], values["width"], values["height"]
            ),
        }
        return switcher.get(
            action,
            lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported)
        )()

    @staticmethod
    def _close_window(window: Any):
        """
        Try to close window element.

        Args:
            window (Object): Window element to close.

        Raises:
            FlaUiError: If window could not be closed.
        """
        try:
            window.Close()
        except MethodNotSupportedException:
            raise FlaUiError(FlaUiError.WindowCloseNotSupported) from None

    @staticmethod
    def _resize_window(window: Any, width: int, height: int):
        """
        Resize the window using the UIAutomation Transform pattern.
        """
        if width <= 0 or height <= 0:
            raise FlaUiError(FlaUiError.WindowResizeFailed.format("width/height must be > 0"))

        transform = window.Patterns.Transform
        if not getattr(transform, "IsSupported", False):
            raise FlaUiError(FlaUiError.WindowResizeNotSupported)

        try:
            transform.Pattern.Resize(float(width), float(height))
        except Exception as e:
            raise FlaUiError(FlaUiError.WindowResizeFailed.format(e)) from None

        start = time.time()
        timeout = 5 # seconds
        while time.time() - start < timeout:
            rect = window.BoundingRectangle
            if abs(rect.Width - width) < 1 and abs(rect.Height - height) < 1:
                return
            time.sleep(0.1)

        raise FlaUiError(FlaUiError.WindowResizeFailed.format(
            f"Window did not reach target size within {timeout:.1f}s")
        )
