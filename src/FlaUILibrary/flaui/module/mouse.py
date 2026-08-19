from __future__ import annotations
from enum import Enum
from typing import Optional, Any
import time
import FlaUI.Core.Input  # pylint: disable=import-error
from FlaUI.Core.Input import Mouse as FlaUIMouse # pylint: disable=import-error
from FlaUI.Core.Input import MouseButton # pylint: disable=import-error
from FlaUI.Core.Exceptions import NoClickablePointException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.module.element import Element
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.util.point import Point


class Mouse(ModuleInterface):
    """
    Mouse module wrapper for FlaUI usage.
    Wrapper module executes methods from Mouse.cs implementation.
    """

    def __init__(self, uia: "UIA"):
        """
        Mouse module wrapper for FlaUI usage.

        Args:
            uia (UIA): Automation interface to use
        """
        self._uia = uia

    class Container(ValueContainer):
        """
        Value container from mouse module.
        """
        element: Optional[Any]
        second_element: Optional[Any]
        timeout_in_ms: Optional[int]
        hold_time_in_ms: Optional[int]
        max_repeat: Optional[int]
        click_element_xpath: Optional[str]
        goal_element_xpath: Optional[str]
        focus_element_xpath_before: Optional[str]
        focus_element_xpath_after: Optional[str]
        ignore_if: Optional[bool]
        scroll_amount: Optional[float]
        x: Optional[int]
        y: Optional[int]
        second_x: Optional[int]
        second_y: Optional[int]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        LEFT_CLICK = "MOUSE_LEFT_CLICK"
        LEFT_CLICK_OPEN = "MOUSE_LEFT_CLICK_OPEN"
        LEFT_CLICK_CLOSE = "MOUSE_LEFT_CLICK_CLOSE"
        MIDDLE_CLICK = "MOUSE_MIDDLE_CLICK"
        MIDDLE_CLICK_OPEN = "MOUSE_MIDDLE_CLICK_OPEN"
        MIDDLE_CLICK_CLOSE = "MOUSE_MIDDLE_CLICK_CLOSE"
        RIGHT_CLICK = "MOUSE_RIGHT_CLICK"
        RIGHT_CLICK_OPEN = "MOUSE_RIGHT_CLICK_OPEN"
        RIGHT_CLICK_CLOSE = "MOUSE_RIGHT_CLICK_CLOSE"
        DOUBLE_CLICK = "MOUSE_DOUBLE_CLICK"
        DOUBLE_CLICK_OPEN = "MOUSE_DOUBLE_CLICK_OPEN"
        DOUBLE_CLICK_CLOSE = "MOUSE_DOUBLE_CLICK_CLOSE"
        LEFT_CLICK_HOLD = "MOUSE_LEFT_CLICK_HOLD"
        RIGHT_CLICK_HOLD = "MOUSE_RIGHT_CLICK_HOLD"
        DOUBLE_CLICK_HOLD = "MOUSE_DOUBLE_CLICK_HOLD"
        MIDDLE_CLICK_HOLD = "MOUSE_MIDDLE_CLICK_HOLD"
        MOVE_TO = "MOUSE_MOVE_TO"
        DRAG_AND_DROP = "MOUSE_DRAG_AND_DROP"
        SCROLL_UP = "MOUSE_SCROLL_UP"
        SCROLL_DOWN = "MOUSE_SCROLL_DOWN"
        LEFT_CLICK_HOLD_OPEN = "MOUSE_LEFT_CLICK_HOLD_OPEN"
        LEFT_CLICK_HOLD_CLOSE= "MOUSE_LEFT_CLICK_HOLD_CLOSE"

    @staticmethod
    def create_value_container(element=None,
                               second_element=None,
                               timeout_in_ms=1000,
                               max_repeat=5,
                               hold_time_in_ms=1000,
                               click_element_xpath=None,
                               goal_element_xpath=None,
                               focus_element_xpath_before=None,
                               focus_element_xpath_after=None,
                               ignore_if=True,
                               scroll_amount=None,
                               x=None,
                               y=None,
                               second_x=None,
                               second_y=None) -> Container:
        # pylint: disable=C0301
        """
        Helper to create container object.

        Args:
            element (Object): Element to click
            second_element (Object): To Element from drag and drop
            timeout_in_ms: Timeout in between waiting loops between clicking and existance profing of Click Open/ Click Close
            hold_time_in_ms: Total time of hold in Click Hold
            max_repeat: Maximum number of repeats of clicking and wating in Click Open/ Click Close
            click_element_xpath: The element to be clicked in Click Open/ Click Close
            goal_element_xpath: Close element from Click Close/ open element from Click Open
            focus_element_xpath_before: Focus element before clicking in Click Open/ Click Close
            focus_element_xpath_after: Focus element after clicking in Click Open/ Click Close
            ignore_if: The execution will be ignored if the clicking element exist in Click Open / does not exist in Click Close
            scroll_amount: The amount of scrolls to be made by mouse
            x (Number): Absolute screen X coordinate or X offset from element's clickable point
            y (Number): Absolute screen Y coordinate or Y offset from element's clickable point
            second_x (Number): Absolute screen X coordinate or X offset for drag and drop target
            second_y (Number): Absolute screen Y coordinate or Y offset for drag and drop target
        """
        # pylint: enable=C0301
        return Mouse.Container(element=element,
                               second_element=second_element,
                               timeout_in_ms=timeout_in_ms,
                               max_repeat=max_repeat,
                               hold_time_in_ms=hold_time_in_ms,
                               click_element_xpath=click_element_xpath,
                               goal_element_xpath=goal_element_xpath,
                               focus_element_xpath_before=focus_element_xpath_before,
                               focus_element_xpath_after=focus_element_xpath_after,
                               ignore_if=ignore_if,
                               scroll_amount=scroll_amount,
                               x=Converter.cast_to_int(x),
                               y=Converter.cast_to_int(y),
                               second_x=Converter.cast_to_int(second_x),
                               second_y=Converter.cast_to_int(second_y))

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.LEFT_CLICK:
                lambda: self._click(values),
            self.Action.LEFT_CLICK_OPEN:
                lambda: self._click_open(Mouse._click, values),
            self.Action.RIGHT_CLICK_OPEN:
                lambda: self._click_open(Mouse._right_click, values),
            self.Action.DOUBLE_CLICK_OPEN:
                lambda: self._click_open(Mouse._double_click, values),
            self.Action.MIDDLE_CLICK_OPEN:
                lambda: self._click_open(Mouse._middle_click, values),
            self.Action.LEFT_CLICK_HOLD_OPEN:
                lambda: self._click_open(Mouse._click_hold, values),
            self.Action.LEFT_CLICK_CLOSE:
                lambda: self._click_close(Mouse._click, values),
            self.Action.RIGHT_CLICK_CLOSE:
                lambda: self._click_close(Mouse._right_click, values),
            self.Action.DOUBLE_CLICK_CLOSE:
                lambda: self._click_close(Mouse._double_click, values),
            self.Action.MIDDLE_CLICK_CLOSE:
                lambda: self._click_close(Mouse._middle_click, values),
            self.Action.LEFT_CLICK_HOLD_CLOSE:
                lambda: self._click_close(Mouse._click_hold, values),
            self.Action.RIGHT_CLICK:
                lambda: self._right_click(values),
            self.Action.MIDDLE_CLICK:
                lambda: self._middle_click(values),
            self.Action.DOUBLE_CLICK:
                lambda: self._double_click(values),
            self.Action.LEFT_CLICK_HOLD:
                lambda: self._click_hold(values),
            self.Action.RIGHT_CLICK_HOLD:
                lambda: self._right_click_hold(values),
            self.Action.DOUBLE_CLICK_HOLD:
                lambda: self._double_click_hold(values),
            self.Action.MIDDLE_CLICK_HOLD:
                lambda: self._middle_click_hold(values),
            self.Action.MOVE_TO:
                lambda: self._move_to(values),
            self.Action.DRAG_AND_DROP:
                lambda: self._drag_and_drop(values),
            self.Action.SCROLL_UP:
                lambda: self._scroll(values),
            self.Action.SCROLL_DOWN:
                lambda: self._scroll(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _resolve_point(container: Container,
                       element_key: str = "element",
                       x_key: str = "x",
                       y_key: str = "y") -> Point:
        """
        Resolve a mouse point from an element locator and/or x/y coordinates.

        If an element is provided, the element's clickable point is used and x/y are applied as offsets.
        If no element is provided, both x and y are required as absolute screen coordinates.

        Args:
            container (Container): Mouse value container.
            element_key (str): Container key for the element.
            x_key (str): Container key for the x coordinate.
            y_key (str): Container key for the y coordinate.

        Returns:
            Point: Screen point to use for the mouse operation.

        Raises:
            FlaUiError: If neither an element nor both coordinates are provided, or if the element is not clickable.
        """
        element = container[element_key]
        x = container[x_key]
        y = container[y_key]

        if element is not None:
            try:
                point = Point.from_clickable_point(element.GetClickablePoint())
            except NoClickablePointException:
                raise FlaUiError(FlaUiError.ElementNotClickable) from None

            offset_x = x if x is not None else 0
            offset_y = y if y is not None else 0
            return point.offset(offset_x, offset_y)

        if x is None or y is None:
            if x is not None or y is not None:
                raise FlaUiError(FlaUiError.BothCoordinatesRequired)
            raise FlaUiError(FlaUiError.IdentifierOrCoordinatesRequired)

        return Point(x, y)

    @staticmethod
    def _move_to_point(point: Point) -> None:
        """
        Move the mouse cursor to the given Python point.

        Args:
            point (Point): Target screen coordinates.
        """
        FlaUI.Core.Input.Mouse.MoveTo(point.x, point.y)

    def _click_open(self, click_type: Any, container: Container) -> bool:
        """
        Clicks the `click_element_xpath` and expects `goal_element_xpath` (open element) to appear.
        Uses `max_repeat` and `timeout_in_ms` from the container to retry the click/open sequence.
        Container fields used:
          - click_element_xpath (str): element to click
          - goal_element_xpath (str): element expected to open
          - focus_element_xpath_before (str|None): optional focus element before clicking
          - focus_element_xpath_after (str|None): optional focus element after open
          - max_repeat (int): retry count
          - timeout_in_ms (int): wait between retries (milliseconds)
          - hold_time_in_ms (int): hold time forwarded to the click action
          - ignore_if (bool): skip if open element already present
        Returns:
          - True on success.
        Raises:
          - FlaUiError(ElementNotExists|ElementNotOpened|ElementNotClickable)
        """
        try:
            click_element_xpath = container["click_element_xpath"]
            open_element_xpath = container["goal_element_xpath"]
            focus_element_xpath_before_click = container["focus_element_xpath_before"]
            focus_element_xpath_after_open = container["focus_element_xpath_after"]
            max_repeat = container["max_repeat"]
            timeout_between_repeats = container["timeout_in_ms"]
            ignore_if_already_open = container["ignore_if"]

            if ignore_if_already_open:
                element_container = Element.create_value_container(xpath=open_element_xpath)
                if self._uia.action(action=Element.Action.GET_ELEMENT_BY_XPATH, values=element_container):
                    return True

            if focus_element_xpath_before_click:
                element_container = Element.create_value_container(xpath=focus_element_xpath_before_click,
                                                                   retry_timeout_in_milliseconds=0)
                self._uia.action(action=Element.Action.FOCUS_ELEMENT, values=element_container)

            _open_element_found = False
            _click_element_found = False

            for _ in range(max_repeat):
                element_container = Element.create_value_container(xpath=click_element_xpath)
                click_element = self._uia.action(action=Element.Action.GET_ELEMENT_BY_XPATH, values=element_container)

                if click_element:
                    _click_element_found = True
                    click_type(self.create_value_container(
                        element=click_element,
                        hold_time_in_ms=container["hold_time_in_ms"]
                    ))

                if _click_element_found:
                    element_container = Element.create_value_container(xpath=open_element_xpath)
                    open_element = self._uia.action(action=Element.Action.GET_ELEMENT_BY_XPATH,
                                                    values=element_container)

                    if open_element:
                        _open_element_found = True
                        if focus_element_xpath_after_open:
                            element_container = Element.create_value_container(xpath=focus_element_xpath_after_open,
                                                                       retry_timeout_in_milliseconds=0)
                            self._uia.action(action=Element.Action.FOCUS_ELEMENT, values=element_container)
                        return True

                if timeout_between_repeats > 0:
                    time.sleep(float(timeout_between_repeats) / 1000)

            if not _click_element_found and not _open_element_found:
                raise FlaUiError(FlaUiError.ElementNotExists.format(click_element_xpath))
            raise FlaUiError(FlaUiError.ElementNotOpened.format(open_element_xpath, click_element_xpath))
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    def _click_close(self, click_type: Any, container: Container) -> bool:
        """
        Clicks the `click_element_xpath` and expects `goal_element_xpath` (close element) to disappear.
        Uses `max_repeat` and `timeout_in_ms` from the container to retry the click/close sequence.
        Container fields used:
          - click_element_xpath (str): element to click
          - goal_element_xpath (str): element expected to close (be absent)
          - focus_element_xpath_before (str|None): optional focus element before clicking
          - focus_element_xpath_after (str|None): optional focus element after close
          - max_repeat (int): retry count
          - timeout_in_ms (int): wait between retries (milliseconds)
          - hold_time_in_ms (int): hold time forwarded to the click action
          - ignore_if (bool): skip if close element already absent
        Returns:
          - True on success.
        Raises:
          - FlaUiError(ElementNotExists|ElementNotClosed|ElementNotClickable)
        """
        click_element_xpath = container["click_element_xpath"]
        close_element_xpath = container["goal_element_xpath"]
        focus_element_xpath_before_click = container["focus_element_xpath_before"]
        focus_element_xpath_after_close = container["focus_element_xpath_after"]
        max_repeat = container["max_repeat"]
        timeout_between_repeats = container["timeout_in_ms"]
        ignore_if_already_close = container["ignore_if"]

        try:
            if ignore_if_already_close:
                element_container = Element.create_value_container(xpath=close_element_xpath)
                if not self._uia.action(action=Element.Action.GET_ELEMENT_BY_XPATH, values=element_container):
                    return True

            if focus_element_xpath_before_click:
                element_container = Element.create_value_container(xpath=focus_element_xpath_before_click,
                                                                   retry_timeout_in_milliseconds=0)
                self._uia.action(action=Element.Action.FOCUS_ELEMENT, values=element_container)

            _click_element_found = False
            for _ in range(max_repeat):
                element_container = Element.create_value_container(xpath=click_element_xpath)
                click_element = self._uia.action(action=Element.Action.GET_ELEMENT_BY_XPATH, values=element_container)

                if click_element:
                    _click_element_found = True
                    click_type(self.create_value_container(
                        element=click_element,
                        hold_time_in_ms= container["hold_time_in_ms"]
                    ))

                if _click_element_found:
                    element_container = Element.create_value_container(xpath=close_element_xpath)
                    close_element = self._uia.action(action=Element.Action.GET_ELEMENT_BY_XPATH,
                                                     values=element_container)

                    if not close_element and _click_element_found:
                        if focus_element_xpath_after_close:
                            element_container = Element.create_value_container(
                                xpath=focus_element_xpath_after_close,
                                retry_timeout_in_milliseconds=0)
                            self._uia.action(action=Element.Action.FOCUS_ELEMENT, values=element_container)
                        return True

                if timeout_between_repeats > 0:
                    time.sleep(float(timeout_between_repeats) / 1000)

            if not _click_element_found:
                raise FlaUiError(FlaUiError.ElementNotExists.format(click_element_xpath))
            raise FlaUiError(FlaUiError.ElementNotClosed.format(close_element_xpath, click_element_xpath))
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    @staticmethod
    def _click(container: Container) -> None:
        """
        Performs a simple left-click on the provided element or coordinates.
        Container fields used:
          - element: optional element object exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
          - FlaUiError(IdentifierOrCoordinatesRequired) if neither element nor coordinates are provided.
        """
        point = Mouse._resolve_point(container)
        Mouse._move_to_point(point)
        FlaUIMouse.LeftClick()

    @staticmethod
    def _click_hold(container: Container) -> None:
        """
        Moves the mouse to the element's clickable point or coordinates, presses and holds, then releases.
        Container fields used:
          - element: optional element object exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
          - hold_time_in_ms (int): how long to hold (milliseconds)
        Behavior:
          - Move mouse to resolved point.
          - Mouse.Down(), sleep(hold_time_in_ms), Mouse.Up()
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        hold_time_in_ms = container["hold_time_in_ms"]
        Mouse._move_to_point(point)
        FlaUI.Core.Input.Mouse.Down()
        if hold_time_in_ms > 0:
            time.sleep(float(hold_time_in_ms) / 1000)
        FlaUI.Core.Input.Mouse.Up()

    @staticmethod
    def _scroll(container: Container) -> None:
        """
        Moves the mouse to the element's clickable point or coordinates and performs a scroll.
        Container fields used:
          - element: optional element object exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
          - scroll_amount (float): amount to scroll (positive/negative)
        Behavior:
          - Move mouse to resolved point and call Mouse.Scroll(scroll_amount).
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        scroll_amount = container["scroll_amount"]
        Mouse._move_to_point(point)
        FlaUI.Core.Input.Mouse.Scroll(float(scroll_amount))

    @staticmethod
    def _middle_click(container: Container) -> None:
        """
        Performs a middle mouse button click at the element's clickable point or coordinates.
        Container fields used:
          - element: optional element object exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        Mouse._move_to_point(point)
        FlaUIMouse.Click(MouseButton.Middle)

    @staticmethod
    def _middle_click_hold(container: Container) -> None:
        """
        Performs a middle-button press-and-hold on the element's clickable point or coordinates.
        Container fields used:
          - element: optional element object exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
          - hold_time_in_ms (int): how long to hold (milliseconds)
        Behavior:
          - Move to resolved point, Mouse.Down(Middle), sleep(hold_time), Mouse.Up(Middle).
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        hold_time_in_ms = container["hold_time_in_ms"]
        Mouse._move_to_point(point)
        FlaUI.Core.Input.Mouse.Down(FlaUI.Core.Input.MouseButton.Middle)
        if hold_time_in_ms > 0:
            time.sleep(float(hold_time_in_ms) / 1000)
        FlaUI.Core.Input.Mouse.Up(FlaUI.Core.Input.MouseButton.Middle)

    @staticmethod
    def _right_click(container: Container) -> None:
        """
        Performs a right-click on the provided element or coordinates.
        Container fields used:
          - element: optional element object exposing `RightClick()` or `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        Mouse._move_to_point(point)
        FlaUIMouse.RightClick()

    @staticmethod
    def _right_click_hold(container: Container) -> None:
        """
        Performs a right-button press-and-hold on the element's clickable point or coordinates.
        Container fields used:
          - element: optional element object exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
          - hold_time_in_ms (int): how long to hold (milliseconds)
        Behavior:
          - Move to resolved point, Mouse.Down(Right), sleep(hold_time), Mouse.Up(Right).
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        hold_time_in_ms = container["hold_time_in_ms"]
        Mouse._move_to_point(point)
        FlaUI.Core.Input.Mouse.Down(FlaUI.Core.Input.MouseButton.Right)
        if hold_time_in_ms > 0:
            time.sleep(float(hold_time_in_ms) / 1000)
        FlaUI.Core.Input.Mouse.Up(FlaUI.Core.Input.MouseButton.Right)

    @staticmethod
    def _double_click(container: Container) -> None:
        """
        Performs a double-click on the provided element or coordinates.
        Container fields used:
          - element: optional element object exposing `DoubleClick()` or `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        Mouse._move_to_point(point)
        FlaUIMouse.LeftDoubleClick()

    @staticmethod
    def _double_click_hold(container: Container) -> None:
        """
        Performs a double-click sequence with an optional hold after the second press.
        Container fields used:
          - element: optional element object exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
          - hold_time_in_ms (int): how long to hold after the second down (milliseconds)
        Behavior:
          - Move to resolved point, emulate double-click (Down/Up, Down, optional sleep, Up).
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        hold_time_in_ms = container["hold_time_in_ms"]
        Mouse._move_to_point(point)
        FlaUI.Core.Input.Mouse.Down()
        FlaUI.Core.Input.Mouse.Up()
        FlaUI.Core.Input.Mouse.Down()
        if hold_time_in_ms > 0:
            time.sleep(float(hold_time_in_ms) / 1000)
        FlaUI.Core.Input.Mouse.Up()

    @staticmethod
    def _move_to(container: Container) -> None:
        """
        Moves the mouse cursor to the element's clickable point or coordinates.
        Container fields used:
          - element: optional element object exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets from the element's clickable point
        Behavior:
          - Mouse.MoveTo(x, y).
        Raises:
          - FlaUiError(ElementNotClickable) if element has no clickable point.
        """
        point = Mouse._resolve_point(container)
        Mouse._move_to_point(point)

    @staticmethod
    def _drag_and_drop(container: Container) -> None:
        """
        Drags from `element` to `second_element` using their clickable points or coordinates.
        Container fields used:
          - element: optional source element exposing `GetClickablePoint()`
          - second_element: optional target element exposing `GetClickablePoint()`
          - x, y: absolute screen coordinates or offsets for the drag start
          - second_x, second_y: absolute screen coordinates or offsets for the drag target
        Behavior:
          - Move to start point, Mouse.Down(), move to target point, Mouse.Up()
        Raises:
          - FlaUiError(ElementNotClickable) if either element has no clickable point.
        """
        element_from = Mouse._resolve_point(container)
        element_to = Mouse._resolve_point(container,
                                          element_key="second_element",
                                          x_key="second_x",
                                          y_key="second_y")
        Mouse._move_to_point(element_from)
        FlaUI.Core.Input.Mouse.Down()
        Mouse._move_to_point(element_to)
        FlaUI.Core.Input.Mouse.Up()
