from enum import Enum
from typing import Optional, Any
import time
import FlaUI.Core.Input  # pylint: disable=import-error
from FlaUI.Core.Exceptions import NoClickablePointException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
from FlaUILibrary.flaui.module.element import Element


class Mouse(ModuleInterface):
    """
    Mouse module wrapper for FlaUI usage.
    Wrapper module executes methods from Mouse.cs implementation.
    """

    def __init__(self, automation: Any):
        """
        Mouse module wrapper for FlaUI usage.

        Args:
            automation (Object): UIA3/UIA2 automation object from FlaUI.
        """
        self._automation = automation
        self._element_module = Element(self._automation, timeout=0)

    class Container(ValueContainer):
        """
        Value container from mouse module.
        """
        element: Optional[Any]
        second_element: Optional[Any]
        timeout_in_ms: Optional[int]
        max_repeat: Optional[int]
        click_element_xpath: Optional[str]
        goal_element_xpath: Optional[str]
        focus_element_xpath_before: Optional[str]
        focus_element_xpath_after: Optional[str]
        ignore_if: Optional[bool]

    class Action(Enum):
        """Supported actions for execute action implementation."""
        LEFT_CLICK = "LEFT_CLICK"
        LEFT_CLICK_OPEN = "LEFT_CLICK_OPEN"
        LEFT_CLICK_CLOSE = "LEFT_CLICK_CLOSE"
        RIGHT_CLICK = "RIGHT_CLICK"
        RIGHT_CLICK_OPEN = "RIGHT_CLICK_OPEN"
        RIGHT_CLICK_CLOSE = "RIGHT_CLICK_CLOSE"
        DOUBLE_CLICK = "DOUBLE_CLICK"
        DOUBLE_CLICK_OPEN = "DOUBLE_CLICK_OPEN"
        DOUBLE_CLICK_CLOSE = "DOUBLE_CLICK_CLOSE"
        LEFT_CLICK_HOLD = "LEFT_CLICK_HOLD"
        RIGHT_CLICK_HOLD = "RIGHT_CLICK_HOLD"
        DOUBLE_CLICK_HOLD = "DOUBLE_CLICK_HOLD"
        MOVE_TO = "MOVE_TO"
        DRAG_AND_DROP = "DRAG_AND_DROP"

    @staticmethod
    def create_value_container(element=None, second_element=None, timeout_in_ms=None, max_repeat=None,
                               click_element_xpath=None, goal_element_xpath=None,
                               focus_element_xpath_before=None, focus_element_xpath_after=None,
                               ignore_if=None):
        """
        Helper to create container object.

        Args:
            element (Object): Element to click
            second_element (Object): To Element from drag and drop
            timeout_in_ms: Total time of hold in Click Hold, Timeout in between waiting loops between clicking and existance profing of Click Open/ Click Close
            max_repeat: Maximum number of repeats of clicking and wating in Click Open/ Click Close
            click_element_xpath: The element to be clicked in Click Open/ Click Close
            goal_element_xpath: Close element from Click Close/ open element from Click Open
            focus_element_xpath_before: Focus element before clicking in Click Open/ Click Close
            focus_element_xpath_after: Focus element after clicking in Click Open/ Click Close
            ignore_if: The execution will be ignored if the clicking element exist in Click Open / does not exist in Click Close
        """
        return Mouse.Container(element=element, second_element=second_element, timeout_in_ms=timeout_in_ms,
                               max_repeat=max_repeat,
                               click_element_xpath=click_element_xpath, goal_element_xpath=goal_element_xpath,
                               focus_element_xpath_before=focus_element_xpath_before,
                               focus_element_xpath_after=focus_element_xpath_after,
                               ignore_if=ignore_if)

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.LEFT_CLICK: lambda: self._click(values["element"]),
            self.Action.LEFT_CLICK_OPEN: lambda: self._click_open(Mouse._click, values["click_element_xpath"],
                                                                  values["goal_element_xpath"],
                                                                  values["focus_element_xpath_before"],
                                                                  values["focus_element_xpath_after"],
                                                                  values["max_repeat"], values["timeout_in_ms"],
                                                                  values["ignore_if"]),
            self.Action.RIGHT_CLICK_OPEN: lambda: self._click_open(Mouse._right_click, values["click_element_xpath"],
                                                                   values["goal_element_xpath"],
                                                                   values["focus_element_xpath_before"],
                                                                   values["focus_element_xpath_after"],
                                                                   values["max_repeat"], values["timeout_in_ms"],
                                                                   values["ignore_if"]),
            self.Action.DOUBLE_CLICK_OPEN: lambda: self._click_open(Mouse._double_click, values["click_element_xpath"],
                                                                    values["goal_element_xpath"],
                                                                    values["focus_element_xpath_before"],
                                                                    values["focus_element_xpath_after"],
                                                                    values["max_repeat"], values["timeout_in_ms"],
                                                                    values["ignore_if"]),
            self.Action.LEFT_CLICK_CLOSE: lambda: self._click_close(Mouse._click, values["click_element_xpath"],
                                                                    values["goal_element_xpath"],
                                                                    values["focus_element_xpath_before"],
                                                                    values["focus_element_xpath_after"],
                                                                    values["max_repeat"], values["timeout_in_ms"],
                                                                    values["ignore_if"]),
            self.Action.RIGHT_CLICK_CLOSE: lambda: self._click_close(Mouse._right_click, values["click_element_xpath"],
                                                                     values["goal_element_xpath"],
                                                                     values["focus_element_xpath_before"],
                                                                     values["focus_element_xpath_after"],
                                                                     values["max_repeat"], values["timeout_in_ms"],
                                                                     values["ignore_if"]),
            self.Action.DOUBLE_CLICK_CLOSE: lambda: self._click_close(Mouse._double_click,
                                                                      values["click_element_xpath"],
                                                                      values["goal_element_xpath"],
                                                                      values["focus_element_xpath_before"],
                                                                      values["focus_element_xpath_after"],
                                                                      values["max_repeat"], values["timeout_in_ms"],
                                                                      values["ignore_if"]),
            self.Action.RIGHT_CLICK: lambda: self._right_click(values["element"]),
            self.Action.DOUBLE_CLICK: lambda: self._double_click(values["element"]),
            self.Action.LEFT_CLICK_HOLD: lambda: self._click_hold(values["element"], values["timeout_in_ms"]),
            self.Action.RIGHT_CLICK_HOLD: lambda: self._right_click_hold(values["element"], values["timeout_in_ms"]),
            self.Action.DOUBLE_CLICK_HOLD: lambda: self._double_click_hold(values["element"], values["timeout_in_ms"]),
            self.Action.MOVE_TO: lambda: self._move_to(values["element"]),
            self.Action.DRAG_AND_DROP: lambda: self._drag_and_drop(values["element"], values["second_element"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _click_open(self, click_type, click_element_xpath: str, open_element_xpath: str,
                    focus_element_xpath_before_click: str = None, focus_element_xpath_after_open: str = None,
                    max_repeat: int = 5, timeout_between_repeats: int = 1000, ignore_if_already_open: bool = True):
        """
        Clicks on click element and expects the open element to be opened.
        Trys for max_repeat times and sleeps between every try for timeout_between_repeats.
        
        Raises:
            FlaUiError: If Click Element is not available.
            FlaUiError: If Open Element is not available after clicking for maximal times on Click Element.
        """
        try:
            if ignore_if_already_open:
                container = Element.create_value_container(xpath=open_element_xpath)
                if self._element_module.execute_action(Element.Action.GET_ELEMENT_BY_XPATH, container):
                    return True

            if focus_element_xpath_before_click:
                container = Element.create_value_container(xpath=focus_element_xpath_before_click)
                self._element_module.execute_action(Element.Action.FOCUS_ELEMENT, container)
            _click_element_found = False
            for i in range(max_repeat):
                container = Element.create_value_container(xpath=click_element_xpath)
                click_element = self._element_module.execute_action(Element.Action.GET_ELEMENT_BY_XPATH, container)

                if click_element:
                    _click_element_found = True
                    click_type(click_element)
                    container = Element.create_value_container(xpath=open_element_xpath)
                    open_element = self._element_module.execute_action(Element.Action.GET_ELEMENT_BY_XPATH, container)

                    if open_element:
                        if focus_element_xpath_after_open:
                            container = Element.create_value_container(xpath=focus_element_xpath_after_open)
                            self._element_module.execute_action(Element.Action.FOCUS_ELEMENT, container)
                        return True

                time.sleep(float(timeout_between_repeats) / 1000)
            
            if not _click_element_found:
                raise FlaUiError(FlaUiError.ElementNotExists.format(click_element_xpath))
            raise FlaUiError(FlaUiError.ElementNotOpened.format(open_element_xpath, click_element_xpath))
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

    def _click_close(self, click_type, click_element_xpath: str, close_element_xpath: str,
                     focus_element_xpath_before_click: str = None, focus_element_xpath_after_close: str = None,
                     max_repeat: int = 5, timeout_between_repeats: int = 1000, ignore_if_already_close: bool = True):
        """
        Clicks on click element and expects the close element to be closed.
        Trys for max_repeat time and sleeps between every try for timeout_between_repeats.
        
        Raises:
            FlaUiError: If Click Element is not available and ignore_if_already_close set to False.
            FlaUiError: If Close Element is still available after clicking for maximal times on Click Element.
        """
        try:
            if ignore_if_already_close:
                container = Element.create_value_container(xpath=close_element_xpath)
                if not self._element_module.execute_action(Element.Action.GET_ELEMENT_BY_XPATH, container):
                    return True

            if focus_element_xpath_before_click:
                container = Element.create_value_container(xpath=focus_element_xpath_before_click)
                self._element_module.execute_action(Element.Action.FOCUS_ELEMENT, container)
            
            _click_element_found = False
            for i in range(max_repeat):
                container = Element.create_value_container(xpath=click_element_xpath)
                click_element = self._element_module.execute_action(Element.Action.GET_ELEMENT_BY_XPATH, container)

                if click_element:
                    _click_element_found = True
                    click_type(click_element)

                    container = Element.create_value_container(xpath=close_element_xpath)
                    open_element = self._element_module.execute_action(Element.Action.GET_ELEMENT_BY_XPATH, container)

                    if not open_element:
                        if focus_element_xpath_after_close:
                            container = Element.create_value_container(xpath=focus_element_xpath_after_close)
                            self._element_module.execute_action(Element.Action.FOCUS_ELEMENT, container)
                        return True

                time.sleep(float(timeout_between_repeats) / 1000)
                
            if not _click_element_found:
                raise FlaUiError(FlaUiError.ElementNotExists.format(click_element_xpath))
            raise FlaUiError(FlaUiError.ElementNotClosed.format(close_element_xpath, click_element_xpath))
        except NoClickablePointException:
            raise FlaUiError(FlaUiError.ElementNotClickable) from None

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
        time.sleep(float(timeout_in_ms) / 1000)
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
        time.sleep(float(timeout_in_ms) / 1000)
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
        time.sleep(float(timeout_in_ms) / 1000)
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
