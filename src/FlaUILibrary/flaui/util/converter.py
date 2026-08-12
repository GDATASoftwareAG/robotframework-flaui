import re
from typing import Any, Union
from System import TimeSpan  # pylint: disable=import-error
from FlaUILibrary.flaui.util.automationelement import AutomationElement
from FlaUILibrary.flaui.exception.flauierror import FlaUiError


class Converter:
    """
    Helper class to convert specific values.
    """

    @staticmethod
    def cast_to_timespan(value: int):
        """
        Helper to cast value to timespan. If the value is null, None will be returned.

        Args:
            value (int): Value to convert as timespan
        """
        value = Converter._unwrap_property(value)
        if value is None:
            return None

        return TimeSpan.FromMilliseconds(value)

    @staticmethod
    def cast_to_int(value: Any, error_msg=None):
        """
        Helper to cast value as a number.

        Raises:
            FlaUiError: If creation from convert failed by invalid values.

        Args:
            value (Object): Value to convert
            error_msg (String): Custom error message
        """
        try:
            value = Converter._unwrap_property(value)
            if value is None:
                return None

            return int(value)
        except ValueError:
            if error_msg is None:
                error_msg = FlaUiError.ValueShouldBeANumber.format(value)

        raise FlaUiError(error_msg) from ValueError

    @staticmethod
    def cast_to_string(value: Any):
        """
        Helper to cast value as string.
        If the value is None, an empty string will be returned.

        Args:
            value (Object): Value to convert
        """
        value = Converter._unwrap_property(value)
        if value is None:
            return ""

        return str(value)

    @staticmethod
    def cast_to_xpath_string(value: Union[str, AutomationElement]):
        """
        Helper to cast value as xpath string.
        If the value is None, an empty string will be returned.

        Args:
            value (Object): Value to convert
        """
        value = Converter._unwrap_property(value)
        if isinstance(value, AutomationElement):
            return Converter.cast_to_string(value.Xpath)

        return Converter.cast_to_string(value)

    @staticmethod
    def cast_to_bool(value: Any):
        """
        Helper to cast value as bool.
        If the value is None, False will be returned.

        Args:
            value (Object): Value to convert
        """
        value = Converter._unwrap_property(value)
        if value is None:
            return False

        return bool(value)

    @staticmethod
    def get_combobox_xpath_from_combobox_selectionitem_xpath(xpath: str) -> str:
        """
        Try to find first combobox from xpath. If found xpath will be returned otherwise empty string.

        Args:
            xpath (String): XPath find combobox element.
        """
        is_combobox_selectionitem = "ComboBox" in xpath and "ComboBox" not in xpath.split("/")[-1]
        if is_combobox_selectionitem:
            matches = re.findall(r"/ComboBox.*?/", xpath)
            s = "" if not matches else matches[0]
            result = f"{xpath.split(s)[0]}{s}"[:-1] if s else ""
            return result
        return ""

    @staticmethod
    def _unwrap_property(value: Any) -> Any:
        """
        Helper to unwrap FlaUI AutomationProperty values.
        If value is from the type AutomationProperty, Value will be returned otherwise value.

        Args:
            value (Object): Value or AutomationProperty to convert
        """
        if value is None:
            return None

        if isinstance(value, (bool, int, float, str)):
            return value

        # Should be from type FlaUI.Core.AutomationProperty[T]
        if hasattr(value, "Value"):
            return value.Value

        return value
