import time
from enum import Enum
from typing import Optional, Any, Union, List
from System import Exception as CSharpException  # pylint: disable=import-error
from System import InvalidOperationException # pylint: disable=import-error
from System.Runtime.InteropServices import COMException # pylint: disable=import-error
from FlaUI.Core import Debug as FlaUIDebug  # pylint: disable=import-error
from FlaUI.Core.Exceptions import PropertyNotSupportedException # pylint: disable=import-error
from FlaUI.Core.Exceptions import ElementNotAvailableException # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
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
        xpath: Union[str, AutomationElement]
        name: Optional[str]
        use_exception: Optional[bool]
        retries: Optional[int]
        retry_timeout_in_milliseconds: Optional[int]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        GET_ELEMENT = "ELEMENT_GET"
        GET_ELEMENT_NAME = "ELEMENT_GET_NAME"
        GET_ELEMENT_BY_XPATH = "ELEMENT_GET_BY_XPATH"
        GET_ELEMENT_RECTANGLE_BOUNDING = "ELEMENT_GET_RECTANGLE_BOUNDING"
        GET_ELEMENT_RETRY_TIMEOUT = "ELEMENT_GET_RETRY_TIMEOUT"
        SET_ELEMENT_RETRY_TIMEOUT = "ELEMENT_SET_RETRY_TIMEOUT"
        FOCUS_ELEMENT = "ELEMENT_FOCUS"
        FIND_ONE_ELEMENT = "ELEMENT_FIND_ONE"
        FIND_ALL_ELEMENTS = "ELEMENT_FIND_ALL"
        IS_ELEMENT_ENABLED = "ELEMENT_IS_ENABLED"
        IS_ELEMENT_OFFSCREEN = "ELEMENT_IS_OFFSCREEN"
        NAME_SHOULD_BE = "ELEMENT_NAME_SHOULD_BE"
        NAME_SHOULD_CONTAINS = "ELEMENT_NAME_SHOULD_CONTAINS"
        ELEMENT_SHOULD_EXIST = "ELEMENT_SHOULD_EXIST"
        ELEMENT_SHOULD_NOT_EXIST = "ELEMENT_SHOULD_NOT_EXIST"
        ELEMENT_SHOULD_BE_ENABLED = "ELEMENT_SHOULD_BE_ENABLED"
        ELEMENT_SHOULD_BE_DISABLED = "ELEMENT_SHOULD_BE_DISABLED"
        ELEMENT_SHOULD_BE_OFFSCREEN = "ELEMENT_SHOULD_BE_OFFSCREEN"
        ELEMENT_SHOULD_NOT_BE_OFFSCREEN = "ELEMENT_SHOULD_NOT_BE_OFFSCREEN"
        WAIT_UNTIL_ELEMENT_IS_OFFSCREEN = "ELEMENT_WAIT_UNTIL_IS_OFFSCREEN"
        WAIT_UNTIL_ELEMENT_IS_ENABLED = "ELEMENT_WAIT_UNTIL_IS_ENABLED"
        WAIT_UNTIL_ELEMENT_EXIST = "ELEMENT_WAIT_UNTIL_EXIST"
        WAIT_UNTIL_ELEMENT_DOES_NOT_EXIST = "ELEMENT_WAIT_UNTIL_DOES_NOT_EXIST"

    def __init__(self, automation: Any, retry_timeout_in_milliseconds: int):
        """
        Element module wrapper for FlaUI usage.

        Args:
            automation (Object): UIA3/UIA2 automation object from FlaUI.
            retry_timeout_in_milliseconds (Integer): Timeout handler for element wait if not found.
        """
        self._element = None
        self._automation = automation
        self._retry_timeout_in_milliseconds = retry_timeout_in_milliseconds

    @staticmethod
    def create_value_container(name=None,
                               xpath=None,
                               retries=None,
                               use_exception=None,
                               retry_timeout_in_milliseconds=None,
                               msg=None) -> Container:
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            name (String): Name from element
            xpath (String | AutomationElement): Searched element as xpath from string or AutomationElement
            retries (Number): Retry counter to repeat calls as number
            retry_timeout_in_milliseconds (Number): Timeout handler for element wait if not found.
            use_exception (Bool) : Indicator to ignore exception handling by Flaui
            msg (String): Optional error message
        """
        return Element.Container(name=Converter.cast_to_string(name),
                                 xpath=Converter.cast_to_xpath_string(xpath),
                                 use_exception=Converter.cast_to_bool(use_exception),
                                 retry_timeout_in_milliseconds=Converter.cast_to_int(
                                     retry_timeout_in_milliseconds, msg),
                                 retries=Converter.cast_to_int(retries, msg))

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.FOCUS_ELEMENT:
                lambda: self._focus_element(values),
            self.Action.GET_ELEMENT:
                lambda: self._get_element(values),
            self.Action.GET_ELEMENT_BY_XPATH:
                lambda: self._get_element_by_xpath(values),
            self.Action.GET_ELEMENT_NAME:
                lambda: self._get_name_from_element(values),
            self.Action.GET_ELEMENT_RECTANGLE_BOUNDING:
                lambda: self._get_rectangle_bounding_from_element(values),
            self.Action.IS_ELEMENT_ENABLED:
                lambda: self._is_enabled(values),
            self.Action.NAME_SHOULD_BE:
                lambda: self._name_should_be(values),
            self.Action.NAME_SHOULD_CONTAINS:
                lambda: self._name_should_contain(values),
            self.Action.IS_ELEMENT_OFFSCREEN:
                lambda: self._element_is_offscreen(values),
            self.Action.ELEMENT_SHOULD_BE_ENABLED:
                lambda: self._element_should_be_enabled(values),
            self.Action.ELEMENT_SHOULD_BE_DISABLED:
                lambda: self._element_should_be_disabled(values),
            self.Action.ELEMENT_SHOULD_BE_OFFSCREEN:
                lambda: self._element_should_be_offscreen(values),
            self.Action.ELEMENT_SHOULD_NOT_BE_OFFSCREEN:
                lambda: self._element_should_not_be_offscreen(values),
            self.Action.ELEMENT_SHOULD_EXIST:
                lambda: self._element_should_exist(values),
            self.Action.ELEMENT_SHOULD_NOT_EXIST:
                lambda: self._element_should_not_exist(values),
            self.Action.WAIT_UNTIL_ELEMENT_IS_OFFSCREEN:
                lambda: self._wait_until_element_is_offscreen(values),
            self.Action.WAIT_UNTIL_ELEMENT_IS_ENABLED:
                lambda: self._wait_until_element_is_enabled(values),
            self.Action.FIND_ONE_ELEMENT:
                lambda: self._find_one_element(values),
            self.Action.FIND_ALL_ELEMENTS:
                lambda: self._find_all_elements(values),
            self.Action.WAIT_UNTIL_ELEMENT_EXIST:
                lambda: self._wait_until_element_exist(values),
            self.Action.WAIT_UNTIL_ELEMENT_DOES_NOT_EXIST:
                lambda: self._wait_until_element_does_not_exist(values),
            self.Action.GET_ELEMENT_RETRY_TIMEOUT:
                lambda: self._get_element_retry_timeout(),
            self.Action.SET_ELEMENT_RETRY_TIMEOUT:
                lambda: self._set_element_retry_timeout(values)
        }
        # pylint: enable=unnecessary-lambda

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _is_enabled(self, container: Container) -> bool:
        """
        Return whether the element identified by the container is enabled.

        Args:
            container (Container): Value container with at least the `xpath` key.

        Returns:
            bool: True if the element is enabled, False otherwise.

        Raises:
            FlaUiError: If the element cannot be found.
        """
        return self._get_element(container).IsEnabled

    def _get_name_from_element(self, container: Container) -> str:
        """
        Return the Name property of the element found by the container.

        Args:
            container (Container): Value container with at least the `xpath` key.

        Returns:
            str: The element's Name property.

        Raises:
            FlaUiError: If the element cannot be found.
        """
        return self._get_element(container).Name

    def _get_rectangle_bounding_from_element(self, container: Container) -> List[int]:
        """
        Return the element's bounding rectangle as a list of integers:
        [X, Y, Width, Height].

        Args:
            container (Container): Value container with at least the `xpath` key.

        Returns:
            List[int]: Bounding rectangle values converted to ints.

        Raises:
            FlaUiError: If the element cannot be found.
        """
        rect = self._get_element(container).BoundingRectangle
        return [Converter.cast_to_int(rect.X),
                Converter.cast_to_int(rect.Y),
                Converter.cast_to_int(rect.Width),
                Converter.cast_to_int(rect.Height)]

    def _name_should_be(self, container: Container) -> None:
        """
        Assert that the element's name equals the expected `name` in container.

        Args:
            container (Container): Must contain `xpath` and `name`.

        Raises:
            FlaUiError: If the element name does not equal the expected value
                        or the element cannot be found.
        """
        element_name = self._get_name_from_element(container)
        name = container["name"]
        if element_name != container["name"]:
            raise FlaUiError(FlaUiError.ElementNameNotEquals.format(element_name, name))

    def _name_should_contain(self, container: Container) -> None:
        """
        Assert that the expected `name` is a substring of the element's name.

        Args:
            container (Container): Must contain `xpath` and `name`.

        Raises:
            FlaUiError: If the expected value is not contained in the element name
                        or the element cannot be found.
        """
        element_name = self._get_name_from_element(container)
        name = container["name"]
        if name not in element_name:
            raise FlaUiError(FlaUiError.ElementNameDoesNotContainsFromValue.format(element_name, name))

    def _get_element(self, container: Container) -> Any:
        """
        Return the AutomationElement found by `xpath` in the container.
        Performs a retry using the configured retry timeout if the element is
        not found on first attempt.

        Args:
            container (Container): Must contain `xpath`; may override retry timeout.

        Returns:
            AutomationElement: The found element.

        Raises:
            FlaUiError: If the element cannot be found after retries.
        """
        retry_timeout_in_ms = self._get_element_retry_timeout()
        component = self._get_element_by_xpath(container)

        if not component and retry_timeout_in_ms > 0:
            time.sleep(retry_timeout_in_ms / 1000)
            component = self._get_element_by_xpath(container)

        if component:
            return component

        xpath = container["xpath"]
        raise FlaUiError(FlaUiError.XPathNotFound.format(xpath))

    def _get_element_by_xpath(self, container: Container) -> Any:
        """
        Try to locate the first element by XPath using the automation desktop root.

        Args:
            container (Container): Must contain `xpath`.

        Returns:
            AutomationElement | None: The element if found, otherwise None.

        Notes:
            - Catches automation exceptions (element not available, COM errors,
              general C# exceptions) and returns None on failure.
        """
        try:
            return self._automation.GetDesktop().FindFirstByXPath(container["xpath"])
        except ElementNotAvailableException:
            return None
        except COMException:
            return None
        except CSharpException:
            return None

    def _find_one_element(self, container: Container) -> AutomationElement:
        """
        Find one element by XPath and return a serializable AutomationElement
        representation (automation id, name, classname, xpath).

        Args:
            container (Container): Must contain `xpath`.

        Returns:
            AutomationElement: A lightweight representation suitable for JSON/xml.

        Raises:
            FlaUiError: If no element is found.
        """
        element = self._get_element_by_xpath(container)

        if element:
            return AutomationElement(
                self._try_get_automation_id_property(element),
                self._try_get_name_property(element),
                self._try_get_classname_property(element),
                FlaUIDebug.GetXPathToElement(element)
            )

        raise FlaUiError(FlaUiError.XPathNotFound.format(container["xpath"]))

    def _find_all_elements(self, container: Container) -> List[AutomationElement]:
        """
        Find all elements matching the XPath and return a list of serializable
        AutomationElement representations.

        Args:
            container (Container): Must contain `xpath`.

        Returns:
            List[AutomationElement]: List of element representations (may be empty).
        """
        values = []
        elements = self._get_all_elements_by_xpath(container)
        for element in elements:
            values.append(AutomationElement(
                self._try_get_automation_id_property(element),
                self._try_get_name_property(element),
                self._try_get_classname_property(element),
                FlaUIDebug.GetXPathToElement(element)
            ))

        return values

    def _get_all_elements_by_xpath(self, container: Container) -> List[AutomationElement]:
        """
        Return all AutomationElements that match the supplied XPath.

        Args:
            container (Container): Must contain `xpath`.

        Returns:
            list[AutomationElement]: All matched elements (framework-specific collection).
        """
        return self._automation.GetDesktop().FindAllByXPath(container["xpath"])

    def _element_should_exist(self, container: Container) -> bool:
        """
        Check whether an element exists for the provided XPath.

        Args:
            container (Container): Must contain `xpath` and optional `use_exception`.

        Returns:
            bool: True if the element exists, False otherwise.

        Raises:
            FlaUiError: If the element is missing and `use_exception` is True.
        """
        try:
            if self._get_element(container):
                return True
        except FlaUiError as ex:
            if container["use_exception"]:
                raise ex from None

        return False

    def _element_should_not_exist(self, container: Container) -> bool:
        """
        Assert that no element exists for the provided XPath.

        Args:
            container (Container): Must contain `xpath` and optional `use_exception`.

        Returns:
            bool: True if the element does not exist.

        Raises:
            FlaUiError: If the element exists and `use_exception` is True.
        """
        try:
            component = self._get_element(container)
        except FlaUiError:
            return True

        if component and container["use_exception"]:
            raise FlaUiError(FlaUiError.ElementExists.format(container["xpath"]))

        return False

    def _element_is_offscreen(self, container: Container) -> bool:
        """
        Return whether the identified element is offscreen.

        Args:
            container (Container): Must contain `xpath`.

        Returns:
            bool: True if offscreen, False otherwise.

        Raises:
            FlaUiError: If the element cannot be found.
        """
        return self._get_element(container).IsOffscreen

    def _element_should_be_enabled(self, container: Container) -> None:
        """
        Assert that the element is enabled.

        Args:
            container (Container): Must contain `xpath`.

        Raises:
            FlaUiError: If the element is not enabled or cannot be found.
        """
        enabled = self._get_element(container).IsEnabled
        if not enabled:
            raise FlaUiError(FlaUiError.ElementNotEnabled.format(container["xpath"]))

    def _element_should_be_disabled(self, container: Container) -> None:
        """
        Assert that the element is disabled.

        Args:
            container (Container): Must contain `xpath`.

        Raises:
            FlaUiError: If the element is enabled or cannot be found.
        """
        enabled = self._get_element(container).IsEnabled

        if enabled:
            raise FlaUiError(FlaUiError.ElementNotDisabled.format(container["xpath"]))

    def _element_should_be_offscreen(self, container: Container) -> None:
        """
        Assert that the element is offscreen.

        Args:
            container (Container): Must contain `xpath`.

        Raises:
            FlaUiError: If the element is not offscreen or cannot be found.
        """
        offscreen = self._element_is_offscreen(container)

        if not offscreen:
            raise FlaUiError(FlaUiError.ElementNotOffscreen.format(container["xpath"]))

    def _element_should_not_be_offscreen(self, container: Container) -> None:
        """
        Assert that the element is not offscreen.

        Args:
            container (Container): Must contain `xpath`.

        Raises:
            FlaUiError: If the element is offscreen or cannot be found.
        """
        offscreen = self._element_is_offscreen(container)

        if offscreen:
            raise FlaUiError(FlaUiError.ElementIsOffscreen.format(container["xpath"]))

    def _wait_until_element_is_offscreen(self, container: Container) -> None:
        """
        Poll until the element becomes offscreen or until the number of retries
        in the container is exhausted.

        Args:
            container (Container): Must contain `xpath` and `retries`.

        Raises:
            FlaUiError: If the element did not become offscreen within retries.
        """
        retries = container["retries"]
        container["retry_timeout_in_milliseconds"] = 0
        timer = 0

        while timer < retries:
            try:
                if self._element_is_offscreen(container):
                    self._set_element_retry_timeout(container)
                    return
            except FlaUiError:
                return

            time.sleep(1)
            timer += 1

        raise FlaUiError(FlaUiError.ElementIsOffscreen.format(container["xpath"]))

    def _wait_until_element_exist(self, container: Container) -> None:
        """
        Poll until the element exists or until the number of retries in the
        container is exhausted.

        Args:
            container (Container): Must contain `xpath` and `retries`.

        Raises:
            FlaUiError: If the element did not appear within retries.
        """
        retries = container["retries"]
        container["retry_timeout_in_milliseconds"] = 0
        timer = 0

        while timer < retries:

            try:
                self._get_element(container)
                return
            except FlaUiError:
                pass

            time.sleep(1)
            timer += 1

        raise FlaUiError(FlaUiError.ElementNotExists.format(container["xpath"]))

    def _wait_until_element_does_not_exist(self, container: Container) -> None:
        """
        Poll until the element no longer exists or until the number of retries
        in the container is exhausted.

        Args:
            container (Container): Must contain `xpath` and `retries`.

        Raises:
            FlaUiError: If the element still exists after retries.
        """
        retries = container["retries"]
        container["retry_timeout_in_milliseconds"] = 0
        timer = 0

        while timer < retries:
            try:
                self._get_element(container)
            except FlaUiError:
                return

            time.sleep(1)
            timer += 1

        raise FlaUiError(FlaUiError.ElementExists.format(container["xpath"]))

    def _wait_until_element_is_enabled(self, container: Container) -> None:
        """
        Poll until the element becomes enabled or until the number of retries
        in the container is exhausted.

        Args:
            container (Container): Must contain `xpath` and `retries`.

        Raises:
            FlaUiError: If the element did not become enabled within retries.
        """
        retries = container["retries"]
        container["retry_timeout_in_milliseconds"] = 0
        timer = 0

        while timer < retries:
            try:
                self._element_should_be_enabled(container)
                return
            except FlaUiError:
                pass

            time.sleep(1)
            timer += 1

        raise FlaUiError(FlaUiError.ElementNotEnabled.format(container["xpath"]))

    def _focus_element(self, container: Container) -> None:
        """
        Set keyboard focus on the identified element.

        Args:
            container (Container): Must contain `xpath`.

        Raises:
            FlaUiError: If the element cannot be focused (not focusable or missing).
        """
        try:
            element = self._get_element(container)
            element.Focus()
        except InvalidOperationException:
            xpath = container["xpath"]
            raise FlaUiError(FlaUiError.ElementNotFocusable.format(xpath)) from None

    def _get_element_retry_timeout(self) -> int:
        """
        Return the configured element retry timeout in milliseconds.

        Returns:
            int: Retry timeout in milliseconds (0 means no retry).
        """
        return self._retry_timeout_in_milliseconds

    def _set_element_retry_timeout(self, container: Container) -> None:
        """
        Set the element retry timeout from the container value.

        Args:
            container (Container): Must contain `retry_timeout_in_milliseconds`.

        Notes:
            - Negative or zero values will result in a timeout of 0.
            - None will force the default timeout of 1000 ms.
        """
        value = container.get("retry_timeout_in_milliseconds")

        if value is None:
            value = 1000

        self._retry_timeout_in_milliseconds = max(value, 0)

    @staticmethod
    def _try_get_automation_id_property(element: Any) -> str:
        """
        Safely retrieve the AutomationId property from an AutomationElement.

        Args:
            element (Any): Automation element instance.

        Returns:
            str: The AutomationId value, or empty string when the property is not supported.
        """
        try:
            return element.AutomationId
        except PropertyNotSupportedException:
            return ""

    @staticmethod
    def _try_get_name_property(element: Any) -> str:
        """
        Safely retrieve the Name property from an AutomationElement.

        Args:
            element (Any): Automation element instance.

        Returns:
            str: The Name value, or empty string when the property is not supported.
        """
        try:
            return element.Name
        except PropertyNotSupportedException:
            return ""

    @staticmethod
    def _try_get_classname_property(element: Any) -> str:
        """
        Safely retrieve the ClassName property from an AutomationElement.

        Args:
            element (Any): Automation element instance.

        Returns:
            str: The ClassName value, or empty string when the property is not supported.
        """
        try:
            return element.ClassName
        except PropertyNotSupportedException:
            return ""
