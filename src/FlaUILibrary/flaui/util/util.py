from FlaUILibrary.flaui.exception import FlaUiError


def string_to_int(value):
    """Convert the value from string to int.

    Args:
        value (string): Number to convert.

    Raises:
        FlaUiError: If value is not a number
    """
    try:
        return int(value)
    except ValueError:
        raise FlaUiError(FlaUiError.ValueShouldBeANumber.format(value)) from None
