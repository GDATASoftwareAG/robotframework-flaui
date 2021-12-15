import time
from enum import Enum
from typing import Optional, Any
from System import Exception as CSharpException  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


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
        FOCUS_ELEMENT = "FOCUS_ELEMENT"
        IS_ELEMENT_ENABLED = "IS_ELEMENT_ENABLED"
        NAME_SHOULD_BE = "NAME_SHOULD_BE"
        NAME_SHOULD_CONTAINS = "NAME_SHOULD_CONTAINS"
        ELEMENT_SHOULD_EXIST = "ELEMENT_SHOULD_EXIST"
        ELEMENT_SHOULD_NOT_EXIST = "ELEMENT_SHOULD_NOT_EXIST"
        IS_ELEMENT_VISIBLE = "IS_ELEMENT_VISIBLE"
        ELEMENT_SHOULD_BE_VISIBLE = "ELEMENT_SHOULD_BE_VISIBLE"
        ELEMENT_SHOULD_NOT_BE_VISIBLE = "ELEMENT_SHOULD_NOT_BE_VISIBLE"
        WAIT_UNTIL_ELEMENT_IS_HIDDEN = "WAIT_UNTIL_ELEMENT_IS_HIDDEN"
        WAIT_UNTIL_ELEMENT_IS_VISIBLE = "WAIT_UNTIL_ELEMENT_IS_VISIBLE"

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
    def create_value_container(name=None, xpath=None, retries=None, use_exception=None,  msg=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            name (String): Name from element
            xpath (String): Searched element as xpath
            retries (Number): Retry counter to repeat calls as number
            use_exception (Bool) : Indicator to ignore exception handling by flaui
            msg (String): Optional error message
        """
        return Element.Container(name=Converter.cast_to_string(name),
                                 xpath=Converter.cast_to_string(xpath),
                                 use_exception=Converter.cast_to_bool(use_exception),
                                 retries=Converter.cast_to_int(retries, msg))

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.FOCUS_ELEMENT
            * Values ["xpath"]
            * Returns : None

          *  Action.GET_ELEMENT
            * Values ["xpath"]
            * Returns (Object): UI entity from XPATH if found

          *  Action.GET_ELEMENT_NAME
            * Values ["xpath"]
            * Returns (String): UI entity name from XPATH

          *  Action.IS_ELEMENT_ENABLED
            * Values ["xpath"]
            * Returns : True if element is enabled otherwise False

          *  Action.NAME_SHOULD_BE
            * Values ["xpath", "name"]
            * Returns : None

          *  Action.NAME_SHOULD_CONTAINS
            * Values ["xpath", "name"]
            * Returns : None

           *  Action.IS_ELEMENT_VISIBLE
            * Values ["xpath"]
            * Returns : True if element is visible otherwise False

          *  Action.ELEMENT_SHOULD_BE_VISIBLE
            * Values ["xpath"]
            * Returns : None

          *  Action.ELEMENT_SHOULD_NOT_BE_VISIBLE
            * Values ["xpath"]
            * Returns : None

          *  Action.ELEMENT_SHOULD_EXIST
            * Values ["xpath", "use_exception"]
            * Returns : True if element exists otherwise False

          *  Action.ELEMENT_SHOULD_NOT_EXIST
            * Values ["xpath", "use_exception"]
            * Returns : True if element not exists otherwise False

          *  Action.WAIT_UNTIL_ELEMENT_IS_HIDDEN
            * Values ["xpath", "retries"]
            * Returns : None

          *  Action.WAIT_UNTIL_ELEMENT_IS_VISIBLE
            * Values ["xpath", "retries"]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.FOCUS_ELEMENT: lambda: self._get_element(values["xpath"]).Focus(),
            self.Action.GET_ELEMENT: lambda: self._get_element(values["xpath"]),
            self.Action.GET_ELEMENT_NAME: lambda: self._get_name_from_element(values["xpath"]),
            self.Action.IS_ELEMENT_ENABLED: lambda: self._get_element(values["xpath"]).IsEnabled,
            self.Action.NAME_SHOULD_BE: lambda: self._name_should_be(values["xpath"], values["name"]),
            self.Action.NAME_SHOULD_CONTAINS: lambda: self._name_should_contain(values["xpath"], values["name"]),
            self.Action.IS_ELEMENT_VISIBLE: lambda: self._get_element(values["xpath"]).IsOffscreen,
            self.Action.ELEMENT_SHOULD_BE_VISIBLE: lambda: self._element_should_be_visible(values["xpath"]),
            self.Action.ELEMENT_SHOULD_NOT_BE_VISIBLE: lambda: self._element_should_not_be_visible(values["xpath"]),
            self.Action.ELEMENT_SHOULD_EXIST: lambda: self._element_should_exist(values["xpath"],
                                                                                 values["use_exception"]),
            self.Action.ELEMENT_SHOULD_NOT_EXIST: lambda: self._element_should_not_exist(values["xpath"],
                                                                                         values["use_exception"]),
            self.Action.WAIT_UNTIL_ELEMENT_IS_HIDDEN: lambda: self._wait_until_element_is_hidden(
                values["xpath"], values["retries"]),
            self.Action.WAIT_UNTIL_ELEMENT_IS_VISIBLE: lambda: self._wait_until_element_is_visible(
                values["xpath"], values["retries"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _get_name_from_element(self, xpath: str):
        """
        Get name from element if exists.

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            COMException: If node don't exists.
        """
        return self._get_element(xpath).Name

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

        if not element_name == name:
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

        Args:
            xpath (string): XPath identifier from element.
        """
        return self._automation.GetDesktop().FindFirstByXPath(xpath)

    def _element_should_exist(self, xpath: str, use_exception: bool):
        """
        Checks if element exists.

        Args:
            xpath (string): XPath identifier from element.
            use_exception (bool): Indicator if to throw an FlaUI error

        Raises:
            FlaUiError: If element could not be found
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
            FlaUiError: If element could be found
        """
        try:
            component = self._get_element(xpath)
        except FlaUiError:
            return True

        if component and use_exception:
            raise FlaUiError(FlaUiError.ElementExists.format(xpath))

        return False

    def _element_should_be_visible(self, xpath: str):
        """
        Checks if the element with the given xpath is visible

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could found by xpath.
            FlaUiError: If node by xpath is not visible.
        """
        hidden = self._get_element(xpath).IsOffscreen
        if hidden:
            raise FlaUiError(FlaUiError.ElementNotVisible.format(xpath))

    def _element_should_not_be_visible(self, xpath: str):
        """
        Checks if the element with the given xpath is visible

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could found by xpath.
            FlaUiError: If node by xpath is visible.
        """
        hidden = self._get_element(xpath).IsOffscreen

        if not hidden:
            raise FlaUiError(FlaUiError.ElementVisible.format(xpath))

    def _wait_until_element_is_hidden(self, xpath: str, retries: int):
        """
        Wait until element is hidden or timeout occurs.

        Args:
            xpath (String): XPath from element which should be hidden
            retries (Number): Maximum number from retries from wait until
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
        raise FlaUiError(FlaUiError.ElementVisible.format(xpath))

    def _wait_until_element_is_visible(self, xpath: str, retries: int):
        """Wait until element is visible or timeout occurs.

        Args:
            xpath (String): XPath from element which should be hidden
            retries (Number): Maximum number from retries from wait until
        """

        timer = 0
        old_timeout = self._timeout
        self._set_timeout(0)

        while timer < retries:

            try:
                self._element_should_be_visible(xpath)
                self._set_timeout(old_timeout)
                return
            except FlaUiError:
                pass

            time.sleep(1)
            timer += 1

        self._set_timeout(old_timeout)
        raise FlaUiError(FlaUiError.ElementNotVisible.format(xpath))

    def _set_timeout(self, timeout: int):
        """Set timeout in seconds.

        Args:
            timeout (Number): Timeout value in seconds
        """
        self._timeout = timeout
