import time
from enum import Enum
from typing import Optional, Any
from System import Exception as CSharpException  # pylint: disable=import-error
from System import InvalidOperationException # pylint: disable=import-error
from FlaUI.Core import Debug as FlaUIDebug  # pylint: disable=import-error
from FlaUI.Core.Exceptions import PropertyNotSupportedException  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
from FlaUILibrary.flaui.util.automationelement import AutomationElement


class Element(ModuleInterface):
    """
    Element control module wrapper for FlaUI usage.
    Wrapper module executes methods from AutomationElement.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from element module.
        """
        xpath: Optional[str]
        name: Optional[str]
        use_exception: Optional[bool]
        retries: Optional[int]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        GET_ELEMENT = "GET_ELEMENT"
        GET_ELEMENT_NAME = "GET_ELEMENT_NAME"
        GET_ELEMENT_BY_XPATH = "GET_ELEMENT_BY_XPATH"
        GET_ELEMENT_RECTANGLE_BOUNDING = "GET_ELEMENT_RECTANGLE_BOUNDING"
        FOCUS_ELEMENT = "FOCUS_ELEMENT"
        FIND_ALL_ELEMENTS = "FIND_ALL_ELEMENTS"
        IS_ELEMENT_ENABLED = "IS_ELEMENT_ENABLED"
        IS_ELEMENT_OFFSCREEN = "IS_ELEMENT_OFFSCREEN"
        NAME_SHOULD_BE = "NAME_SHOULD_BE"
        NAME_SHOULD_CONTAINS = "NAME_SHOULD_CONTAINS"
        ELEMENT_SHOULD_EXIST = "ELEMENT_SHOULD_EXIST"
        ELEMENT_SHOULD_NOT_EXIST = "ELEMENT_SHOULD_NOT_EXIST"
        ELEMENT_SHOULD_BE_ENABLED = "ELEMENT_SHOULD_BE_ENABLED"
        ELEMENT_SHOULD_BE_DISABLED = "ELEMENT_SHOULD_BE_DISABLED"
        WAIT_UNTIL_ELEMENT_IS_OFFSCREEN = "WAIT_UNTIL_ELEMENT_IS_OFFSCREEN"
        WAIT_UNTIL_ELEMENT_IS_ENABLED = "WAIT_UNTIL_ELEMENT_IS_ENABLED"
        WAIT_UNTIl_ELEMENT_EXIST = "WAIT_UNTIl_ELEMENT_EXIST"
        WAIT_UNTIL_ELEMENT_DOES_NOT_EXIST = "WAIT_UNTIL_ELEMENT_DOES_NOT_EXIST"

    def __init__(self, automation: Any, timeout: int = 1000):
        """
        Element module wrapper for FlaUI usage.

        Args:
            automation (Object): UIA3/UIA2 automation object from FlaUI.
            timeout (Integer): Timeout handler for element wait if not found.
        """
        self._element = None
        self._automation = automation
        self._timeout = timeout

    @staticmethod
    def create_value_container(name=None, xpath=None, retries=None, use_exception=None, msg=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            name (String): Name from element
            xpath (String): Searched element as xpath
            retries (Number): Retry counter to repeat calls as number
            use_exception (Bool) : Indicator to ignore exception handling by Flaui
            msg (String): Optional error message
        """
        return Element.Container(name=Converter.cast_to_string(name),
                                 xpath=Converter.cast_to_string(xpath),
                                 use_exception=Converter.cast_to_bool(use_exception),
                                 retries=Converter.cast_to_int(retries, msg))

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.
        """

        switcher = {
            self.Action.FOCUS_ELEMENT:
                lambda: self._focus_element(values["xpath"]),
            self.Action.GET_ELEMENT:
                lambda: self._get_element(values["xpath"]),
            self.Action.GET_ELEMENT_BY_XPATH:
                lambda: self._get_element_by_xpath(values["xpath"]),
            self.Action.GET_ELEMENT_NAME:
                lambda: self._get_name_from_element(values["xpath"]),
            self.Action.GET_ELEMENT_RECTANGLE_BOUNDING:
                lambda: self._get_rectangle_bounding_from_element(
                    values["xpath"]),
            self.Action.IS_ELEMENT_ENABLED:
                lambda: self._get_element(values["xpath"]).IsEnabled,
            self.Action.NAME_SHOULD_BE:
                lambda: self._name_should_be(values["xpath"], values["name"]),
            self.Action.NAME_SHOULD_CONTAINS:
                lambda: self._name_should_contain(values["xpath"], values["name"]),
            self.Action.IS_ELEMENT_OFFSCREEN:
                lambda: self._element_is_offscreen(values["xpath"]),
            self.Action.ELEMENT_SHOULD_BE_ENABLED:
                lambda: self._element_should_be_enabled(values["xpath"]),
            self.Action.ELEMENT_SHOULD_BE_DISABLED:
                lambda: self._element_should_be_disabled(values["xpath"]),
            self.Action.ELEMENT_SHOULD_EXIST:
                lambda: self._element_should_exist(values["xpath"], values["use_exception"]),
            self.Action.ELEMENT_SHOULD_NOT_EXIST:
                lambda: self._element_should_not_exist(values["xpath"], values["use_exception"]),
            self.Action.WAIT_UNTIL_ELEMENT_IS_OFFSCREEN:
                lambda: self._wait_until_element_is_offscreen(values["xpath"], values["retries"]),
            self.Action.WAIT_UNTIL_ELEMENT_IS_ENABLED:
                lambda: self._wait_until_element_is_enabled(values["xpath"], values["retries"]),
            self.Action.FIND_ALL_ELEMENTS:
                lambda: self._find_all_elements(values["xpath"]),
            self.Action.WAIT_UNTIl_ELEMENT_EXIST:
                lambda: self._wait_until_element_exist(values["xpath"], values["retries"]),
            self.Action.WAIT_UNTIL_ELEMENT_DOES_NOT_EXIST:
                lambda: self._wait_until_element_does_not_exist(values["xpath"], values["retries"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _get_name_from_element(self, xpath: str):
        """
        Get name from element if exists.

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            COMException: If node don't exist.
        """
        return self._get_element(xpath).Name

    def _get_rectangle_bounding_from_element(self, xpath: str):
        """
        Get rectangle bounding from element if exists.

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            COMException: If node don't exist.
        """
        rect = self._get_element(xpath).BoundingRectangle
        return [Converter.cast_to_int(rect.X),
                Converter.cast_to_int(rect.Y),
                Converter.cast_to_int(rect.Width),
                Converter.cast_to_int(rect.Height)]

    def _name_should_be(self, xpath: str, name: str):
        """
        Verifies if name is equal.

        Args:
            xpath (String): Xpath from element to compare name.
            name (String): name from element which should be

        Raises:
            FlaUiError: If name not equal from element.
            FlaUiError: If element does not exist.
        """
        element_name = self._get_name_from_element(xpath)

        if element_name != name:
            raise FlaUiError(FlaUiError.ElementNameNotEquals.format(element_name, name))

    def _name_should_contain(self, xpath: str, name: str):
        """
        Verifies if expected value is part from name.

        Args:
            xpath (String): Xpath from element to compare name.
            name (String): name from element which should be

        Raises:
            FlaUiError: If expected value don't contain to name from element.
            FlaUiError: If element does not exist.
        """
        element_name = self._get_name_from_element(xpath)

        if name not in element_name:
            raise FlaUiError(FlaUiError.ElementNameDoesNotContainsFromValue.format(element_name, name))

    def _get_element(self, xpath: str):
        """
        Try to get element.

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could not be found by xpath.
        """
        try:
            component = self._get_element_by_xpath(xpath)
            if not component and self._timeout > 0:
                time.sleep(self._timeout / 1000)
                component = self._get_element_by_xpath(xpath)

            if component:
                return component

            raise FlaUiError(FlaUiError.XPathNotFound.format(xpath))

        except CSharpException:
            raise FlaUiError(FlaUiError.XPathNotFound.format(xpath)) from None

    def _get_element_by_xpath(self, xpath: str):
        """
        Try to get element from xpath by desktop.
        Different from self._get_element, it is abstracted from timeout and error handling.

        Args:
            xpath (string): XPath identifier from element.
        """
        return self._automation.GetDesktop().FindFirstByXPath(xpath)

    def _find_all_elements(self, xpath: str):
        values = []
        elements = self._get_all_elements_by_xpath(xpath)
        for element in elements:
            values.append(AutomationElement(
                self._try_get_automation_id_property(element),
                self._try_get_name_property(element),
                self._try_get_classname_property(element),
                FlaUIDebug.GetXPathToElement(element)
            ))

        return values

    def _get_all_elements_by_xpath(self, xpath: str):
        """
        Try to get all elements from xpath by desktop.

        Args:
            xpath (string): XPath identifier from element.
        """
        return self._automation.GetDesktop().FindAllByXPath(xpath)

    def _element_should_exist(self, xpath: str, use_exception: bool):
        """
        Checks if element exists.

        Args:
            xpath (string): XPath identifier from element.
            use_exception (bool): Indicator if to throw an FlaUI error

        Raises:
            FlaUiError: If element could not be found.
        """
        try:
            if self._get_element(xpath):
                return True
        except FlaUiError as ex:
            if use_exception:
                raise ex from None

        return False

    def _element_should_not_exist(self, xpath: str, use_exception: bool):
        """
        Try to get element from xpath.

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If element could be found.
        """
        try:
            component = self._get_element(xpath)
        except FlaUiError:
            return True

        if component and use_exception:
            raise FlaUiError(FlaUiError.ElementExists.format(xpath))

        return False

    def _element_is_offscreen(self, xpath: str):
        """
        Checks if the element with the given xpath is offscreen (true), otherwise false

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could not be found from xpath.
        """
        return self._get_element(xpath).IsOffscreen

    def _element_should_be_enabled(self, xpath: str):
        """
        Checks if the element with the given xpath is enabled

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could not be found from xpath.
            FlaUiError: If node by xpath is not enabled.
        """
        enabled = self._get_element(xpath).IsEnabled
        if not enabled:
            raise FlaUiError(FlaUiError.ElementNotEnabled.format(xpath))

    def _element_should_be_disabled(self, xpath: str):
        """
        Checks if the element with the given xpath is disabled

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could not be found from xpath.
            FlaUiError: If node by xpath is enabled.
        """
        enabled = self._get_element(xpath).IsEnabled

        if enabled:
            raise FlaUiError(FlaUiError.ElementNotDisabled.format(xpath))

    def _wait_until_element_is_offscreen(self, xpath: str, retries: int):
        """Waits until element is offscreen or timeout occurred.

        Args:
            xpath (String): XPath from element which should be hidden
            retries (Number): Maximum number from retries from wait until
        
        Raises:
            FlaUiError: If element could not be found from xpath.
        """

        timer = 0
        old_timeout = self._timeout
        self._set_timeout(0)

        while timer < retries:
            try:
                if self._element_is_offscreen(xpath):
                    self._set_timeout(old_timeout)
                    return
            except FlaUiError:
                return

            time.sleep(1)
            timer += 1

        self._set_timeout(old_timeout)
        raise FlaUiError(FlaUiError.ElementIsOffscreen.format(xpath))

    def _wait_until_element_exist(self, xpath: str, retries: int):
        """Wait until element exist or timeout occurs.

        Args:
            xpath (String): XPath from element which should be hidden
            retries (Number): Maximum number from retries from wait until

        Raises:
            FlaUiError: If element does not exist.
        """

        timer = 0
        old_timeout = self._timeout
        self._set_timeout(0)

        while timer < retries:

            try:
                self._get_element(xpath)
                self._set_timeout(old_timeout)
                return
            except FlaUiError:
                pass

            time.sleep(1)
            timer += 1

        self._set_timeout(old_timeout)
        raise FlaUiError(FlaUiError.ElementNotExists.format(xpath))

    def _wait_until_element_does_not_exist(self, xpath: str, retries: int):
        """
        Wait until element does not exist anymore or timeout occurs.

        Args:
            xpath (String): XPath from element which should be hidden
            retries (Number): Maximum number from retries from wait until

        Raises:
            FlaUiError: If element exists.
        """

        timer = 0
        old_timeout = self._timeout
        self._set_timeout(0)

        while timer < retries:

            try:
                self._get_element(xpath)
            except FlaUiError:
                self._set_timeout(old_timeout)
                return

            time.sleep(1)
            timer += 1

        self._set_timeout(old_timeout)
        raise FlaUiError(FlaUiError.ElementExists.format(xpath))

    def _wait_until_element_is_enabled(self, xpath: str, retries: int):
        """Wait until element is enabled or timeout occurs.

        Args:
            xpath (String): XPath from element which should be hidden
            retries (Number): Maximum number from retries from wait until
        
        Raises:
            FlaUiError: If node could not be found from xpath.
            FlaUiError: If node by xpath is not enabled.
        """

        timer = 0
        old_timeout = self._timeout
        self._set_timeout(0)

        while timer < retries:

            try:
                self._element_should_be_enabled(xpath)
                self._set_timeout(old_timeout)
                return
            except FlaUiError:
                pass

            time.sleep(1)
            timer += 1

        self._set_timeout(old_timeout)
        raise FlaUiError(FlaUiError.ElementNotEnabled.format(xpath))

    def _set_timeout(self, timeout: int):
        """Set timeout in seconds.

        Args:
            timeout (Number): Timeout value in seconds
        """
        self._timeout = timeout

    def _focus_element(self,xpath):
        """Triggers focus action in given element.

        Args:
            element (Element): The element to be focused
            xpath (String): XPath of element to be focused
        
        Raises:
            FlaUiError: If the given element is not focusable.
        """
        element = self._get_element(xpath)
        try:
            element.Focus()
        except InvalidOperationException:
            raise FlaUiError(FlaUiError.ElementNotFocusable.format(xpath)) from None
        
    @staticmethod
    def _try_get_automation_id_property(element):
        """
        Try to get automation id property from element. Return empty string if failed.

        Args:
            element (UIA): AutomationElement.
        """
        try:
            return element.AutomationId
        except PropertyNotSupportedException:
            return ""

    @staticmethod
    def _try_get_name_property(element):
        """
        Try to get name property from element. Return empty string if failed.

        Args:
            element (UIA): AutomationElement.
        """
        try:
            return element.Name
        except PropertyNotSupportedException:
            return ""

    @staticmethod
    def _try_get_classname_property(element):
        """
        Try to get class name property from element. Return empty string if failed.

        Args:
            element (UIA): AutomationElement.
        """
        try:
            return element.ClassName
        except PropertyNotSupportedException:
            return ""
