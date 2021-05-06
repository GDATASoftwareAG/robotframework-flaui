import time
from enum import Enum
from System import Exception as CSharpException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface
from FlaUILibrary.flaui.util import util


class Element(ModuleInterface):
    """
    Element control module wrapper for FlaUI usage.
    Wrapper module executes methods from AutomationElement.cs implementation.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        GET_ELEMENT = "GET_ELEMENT"
        GET_ELEMENT_NAME = "GET_ELEMENT_NAME"
        FOCUS_ELEMENT = "FOCUS_ELEMENT"
        IS_ELEMENT_ENABLED = "IS_ELEMENT_ENABLED"
        NAME_SHOULD_BE = "NAME_SHOULD_BE"
        NAME_SHOULD_CONTAINS = "NAME_SHOULD_CONTAINS"
        ELEMENT_SHOULD_NOT_EXIST = "ELEMENT_SHOULD_NOT_EXIST"
        IS_ELEMENT_VISIBLE = "IS_ELEMENT_VISIBLE"
        ELEMENT_SHOULD_BE_VISIBLE = "ELEMENT_SHOULD_BE_VISIBLE"
        ELEMENT_SHOULD_NOT_BE_VISIBLE = "ELEMENT_SHOULD_NOT_BE_VISIBLE"
        WAIT_UNTIL_ELEMENT_IS_HIDDEN = "WAIT_UNTIL_ELEMENT_IS_HIDDEN"
        WAIT_UNTIL_ELEMENT_IS_VISIBLE = "WAIT_UNTIL_ELEMENT_IS_VISIBLE"

    def __init__(self, automation, timeout=1000):
        """Element module wrapper for FlaUI usage.

        Args:
            automation (Object): UIA3/UIA2 automation object from FlaUI.
            timeout (Integer): Timeout handler for element wait if not found.
        """
        self._element = None
        self._automation = automation
        self._timeout = timeout

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.FOCUS_ELEMENT
            * Values (String) : XPATH from element to find
            * Returns : None

          *  Action.GET_ELEMENT
            * Values (String) : XPATH from element to find
            * Returns (Object): UI entity from XPATH if found

          *  Action.GET_ELEMENT_NAME
            * Values (String) : XPATH from element to obtain name
            * Returns (String): UI entity name from XPATH

          *  Action.IS_ELEMENT_ENABLED
            * Values (Object) : UI entity to verify if is enabled
            * Returns : True if element is enabled otherwise False

          *  Action.NAME_SHOULD_BE
            * Values : (Array) : [@ELEMENT_XPATH, @EXPECTED_NAME]
            * Returns : None

          *  Action.NAME_SHOULD_CONTAINS
            * Values : (Array) : [@ELEMENT_XPATH, @EXPECTED_NAME]
            * Returns : None

           *  Action.IS_ELEMENT_VISIBLE
            * Values (Object): UI entity from XPATH if found
            * Returns : True if element is visible otherwise False

          *  Action.ELEMENT_SHOULD_BE_VISIBLE
            * Values (Object) : UI entity from XPATH if found
            * Returns : None

          *  Action.ELEMENT_SHOULD_NOT_BE_VISIBLE
            * Values (Object) : UI entity from XPATH if found
            * Returns : None

          *  Action.ELEMENT_SHOULD_NOT_EXIST
            * Values (Object) : UI entity from XPATH if found
            * Returns : None

          *  Action.WAIT_UNTIL_ELEMENT_IS_HIDDEN
            * Values (Array) : [@ELEMENT_XPATH, @TIMEOUT]
            * Returns : None

          *  Action.WAIT_UNTIL_ELEMENT_IS_VISIBLE
            * Values (Array) : [@ELEMENT_XPATH, @TIMEOUT]
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.FOCUS_ELEMENT: lambda: self._get_element(values).Focus(),
            self.Action.GET_ELEMENT: lambda: self._get_element(values),
            self.Action.GET_ELEMENT_NAME: lambda: self._get_name_from_element(values),
            self.Action.IS_ELEMENT_ENABLED: lambda: self._get_element(values).IsEnabled,
            self.Action.NAME_SHOULD_BE: lambda: self._name_should_be(values),
            self.Action.NAME_SHOULD_CONTAINS: lambda: self._name_should_contain(values),
            self.Action.IS_ELEMENT_VISIBLE: lambda: self._get_element(values).IsOffscreen,
            self.Action.ELEMENT_SHOULD_BE_VISIBLE: lambda: self._element_should_be_visible(values),
            self.Action.ELEMENT_SHOULD_NOT_BE_VISIBLE: lambda: self._element_should_not_be_visible(values),
            self.Action.ELEMENT_SHOULD_NOT_EXIST: lambda: self._element_should_not_exist(values),
            self.Action.WAIT_UNTIL_ELEMENT_IS_HIDDEN: lambda: self._wait_until_element_is_hidden(
                values[0], util.string_to_int(values[1])),
            self.Action.WAIT_UNTIL_ELEMENT_IS_VISIBLE: lambda: self._wait_until_element_is_visible(
                values[0], util.string_to_int(values[1]))
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _get_name_from_element(self, xpath):
        """Get name from element if exists.

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            COMException: If node don't exists.
        """
        return self._get_element(xpath).Name

    def _name_should_be(self, values):
        """Verifies if name is equal.

        Args:
            values (Array): Contains xpath identifier and expected value to compare [@ELEMENT_XPATH, @EXPECTED_NAME].

        Raises:
            FlaUiError: If name not equal from element.
            FlaUiError: If element does not exist.
        """
        element_name = self._get_name_from_element(values[0])
        name = values[1]

        if not element_name == name:
            raise FlaUiError(FlaUiError.ElementNameNotEquals.format(element_name, name))

    def _name_should_contain(self, values):
        """Verifies if expected value is part from name.

        Args:
            values (Array): Contains xpath identifier and expected value to compare [@ELEMENT_XPATH, @EXPECTED_NAME].

        Raises:
            FlaUiError: If expected value don't contain to name from element.
            FlaUiError: If element does not exist.
        """
        element_name = self._get_name_from_element(values[0])
        name = values[1]

        if name not in element_name:
            raise FlaUiError(FlaUiError.ElementNameDoesNotContainsFromValue.format(element_name, name))

    def _get_element(self, xpath):
        """Try to get element from xpath.

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could not be found by xpath.
        """
        try:
            retry = 0
            max_retry = 10
            timeout = self._timeout / (1000 * max_retry)

            while retry < max_retry:
                desktop = self._automation.GetDesktop()
                component = desktop.FindFirstByXPath(xpath)
                if component:
                    return component
                if timeout > 0:
                    time.sleep(timeout)
                retry = retry + 1

            raise FlaUiError(FlaUiError.XPathNotFound.format(xpath))

        except CSharpException:
            raise FlaUiError(FlaUiError.XPathNotFound.format(xpath)) from None

    def _element_should_not_exist(self, xpath):
        """Try to get element from xpath.

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could found by xpath.
        """
        desktop = self._automation.GetDesktop()
        component = desktop.FindFirstByXPath(xpath)

        if component:
            raise FlaUiError(FlaUiError.ElementExists.format(xpath))

    def _element_should_be_visible(self, xpath):
        """Checks if the element with the given xpath is visible

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could found by xpath.
            FlaUiError: If node by xpath is not visible.
        """
        hidden = self._get_element(xpath).IsOffscreen
        if hidden:
            raise FlaUiError(FlaUiError.ElementNotVisible.format(xpath))

    def _element_should_not_be_visible(self, xpath):
        """Checks if the element with the given xpath is visible

        Args:
            xpath (string): XPath identifier from element.

        Raises:
            FlaUiError: If node could found by xpath.
            FlaUiError: If node by xpath is visible.
        """
        hidden = self._get_element(xpath).IsOffscreen

        if not hidden:
            raise FlaUiError(FlaUiError.ElementVisible.format(xpath))

    def _wait_until_element_is_hidden(self, xpath, retries):
        """Wait until element is hidden or timeout occurs.

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

    def _wait_until_element_is_visible(self, xpath, retries):
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

    def _set_timeout(self, timeout):
        """Set timeout in seconds.

        Args:
            timeout (Number): Timeout value in seconds
        """
        self._timeout = timeout
