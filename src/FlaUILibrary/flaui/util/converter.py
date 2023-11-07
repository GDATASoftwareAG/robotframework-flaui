import re
from typing import Any
from System import TimeSpan  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError


class Converter:
    """
    Helper class to convert specific values.
    """

    @staticmethod
    def cast_to_timespan(value: int):
        if value is None:
            return None

        return TimeSpan.FromMilliseconds(value)

    @staticmethod
    def cast_to_int(value: Any, error_msg=None):
        """
        Helper to cast value as number.

        Raises:
            FlaUiError: If creation from convert failed by invalid values.

        Args:
            value (Object): Value to convert
            error_msg (String) : Custom error message
        """
        try:
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
        If value is None empty string will be returned.

        Args:
            value (Object): Value to convert
        """
        if value is None:
            return ""

        return str(value)

    @staticmethod
    def cast_to_bool(value: Any):
        """
        Helper to cast value as bool.
        If value is None False will be returned.

        Args:
            value (Object): Value to convert
        """
        if value is None:
            return False

        return bool(value)

    @staticmethod
    def get_combobox_xpath_from_combobox_selectionitem_xpath(xpath: str) -> str:
        is_combobox_selectionitem = True if "ComboBox" in xpath and "ComboBox" not in xpath.split("/")[-1] else False
        if is_combobox_selectionitem:
            matches = re.findall(r"/ComboBox.*?/", xpath)
            s = matches[0] if matches is not [] else ""
            result = f"{xpath.split(s)[0]}{s}"[:-1] if s else ""
            return result
        return ""
