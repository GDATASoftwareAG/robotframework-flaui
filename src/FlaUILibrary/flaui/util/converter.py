import re
from datetime import timedelta
from typing import Any, Optional, Tuple, Union
from robot.errors import DataError
from robot.utils import normalize, timestr_to_secs
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
    def cast_to_retry(value: Any, default: str = "10x", error_msg=None) -> Tuple[str, float]:
        """
        Convert a Wait Until Keyword Succeeds retry value to ``(mode, value)``.

        Count values need an ``x`` or ``times`` postfix. Anything else is parsed as
        a Robot Framework timeout in seconds.

        Args:
            value (Object): Retry count or timeout
            default (String): Value to use when ``value`` is None
            error_msg (String): Custom error message

        Returns:
            Tuple[str, float]: ``("count", attempts)`` or ``("timeout", seconds)``
        """
        value = Converter._unwrap_property(value)
        if value is None:
            value = default

        text = normalize(str(value))
        try:
            if text.endswith("times"):
                count = int(text[:-5])
            elif text.endswith("x"):
                count = int(text[:-1])
            else:
                raise ValueError
            if count <= 0:
                if error_msg is None:
                    error_msg = FlaUiError.InvalidRetryValue.format(value)
                raise FlaUiError(error_msg) from None
            return "count", float(count)
        except ValueError:
            pass

        try:
            if isinstance(value, timedelta):
                return "timeout", value.total_seconds()
            return "timeout", float(timestr_to_secs(value))
        except (ValueError, TypeError, DataError):
            if error_msg is None:
                error_msg = FlaUiError.InvalidRetryValue.format(value)

        raise FlaUiError(error_msg) from None

    @staticmethod
    def cast_to_timestr_seconds(value: Any, default: Optional[float] = None, error_msg=None) -> Optional[float]:
        """
        Convert a Robot Framework time value to seconds.

        Accepts RF time strings (``1s``, ``1000ms``, ``2 min 3 s``), numbers as
        seconds, and ``timedelta`` objects. ``None`` returns ``default``.

        Raises:
            FlaUiError: If the value is not a valid Robot Framework time.

        Args:
            value (Object): Time value to convert
            default (float): Value to return when ``value`` is None
            error_msg (String): Custom error message
        """
        value = Converter._unwrap_property(value)
        if value is None:
            return default

        if isinstance(value, timedelta):
            return value.total_seconds()

        try:
            return float(timestr_to_secs(value))
        except (ValueError, TypeError, DataError):
            if error_msg is None:
                error_msg = FlaUiError.InvalidTimeString.format(value)

        raise FlaUiError(error_msg) from None

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

        if isinstance(value, (bool, int, float, str, timedelta)):
            return value

        # Should be from type FlaUI.Core.AutomationProperty[T]
        if hasattr(value, "Value"):
            return value.Value

        return value
