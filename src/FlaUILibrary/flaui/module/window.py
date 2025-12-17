import time
from enum import Enum
from typing import Optional, Any
from FlaUI.Core.Exceptions import MethodNotSupportedException  # pylint: disable=import-error
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.util.converter import Converter


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
        CLOSE_WINDOW = "WINDOW_CLOSE_WINDOW"
        RESIZE_WINDOW = "WINDOW_RESIZE_WINDOW"

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Args:
            action: Method action to use.
            values: See supported action definitions for value usage and value container definition.

        Raises:
            FlaUiError: If action is not supported.
        """

        switcher = {
            self.Action.CLOSE_WINDOW: lambda: self._close_window(values),
            self.Action.RESIZE_WINDOW: lambda: self._resize_window(values),
        }

        return switcher.get(
            action,
            lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported)
        )()

    @staticmethod
    def create_value_container(element=None, width=None, height=None) -> Container:
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            element (Object): Tree element to execute action
            width (Number): Width in pixels of the window
            height (Number): Height in pixels of the window
        """
        return Window.Container(element=element,
                                width=Converter.cast_to_int(width),
                                height=Converter.cast_to_int(height))

    @staticmethod
    def _close_window(container: Container) -> None:
        """
        Close the provided window element.

        Args:
            container (Window.Container): Container holding the window under `container['element']`.

        Raises:
            FlaUiError: If closing is not supported by the element (converted from
                `MethodNotSupportedException`) or if the close operation fails for any other reason.
        """
        try:
            window = container["element"]
            window.Close()
        except MethodNotSupportedException:
            raise FlaUiError(FlaUiError.WindowCloseNotSupported) from None

    @staticmethod
    def _resize_window(container: Container) -> None:
        """
        Resize the provided window element using the UI Automation Transform pattern.

        The method validates the requested width/height (> 0), verifies the Transform
        pattern is supported, invokes the resize operation, and waits up to a short
        timeout for the window to reach the target size.

        Args:
            container (Window.Container): Container holding the target window in
                `container['element']` and the desired `container['width']` and
                `container['height']` (integers or numeric strings).

        Raises:
            FlaUiError: If the requested width or height is non-positive.
            FlaUiError: If the Transform pattern is not supported by the window.
            FlaUiError: If the resize operation fails or the window does not reach
                the target size within the configured timeout.
        """
        window = container["element"]
        width = container["width"]
        height = container["height"]

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
