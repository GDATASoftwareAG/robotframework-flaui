from typing import Any
from FlaUILibrary.flaui.exception import FlaUiError


class Converter:
    """
    Helper class to convert specific values.
    """

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
            return None if not value else int(value)
        except ValueError:
            if error_msg is None:
                error_msg = FlaUiError.ValueShouldBeANumber.format(value)

        raise FlaUiError(error_msg) from ValueError

    @staticmethod
    def cast_to_string(value: Any):
        """
        Helper to cast value as string.

        Args:
            value (Object): Value to convert
        """
        return "" if not value else str(value)

    @staticmethod
    def cast_to_bool(value: Any):
        """
        Helper to cast value as bool.

        Args:
            value (Object): Value to convert
        """
        return "" if not value else bool(value)
