from FlaUILibrary.flaui.exception.flauierror import FlaUiError


class UiaFactory:
    """Creates the in-process UIA2 or UIA3 interface. Used only inside the worker."""

    @staticmethod
    def create(identifier: str, retry_timeout_in_milliseconds: int):
        """Create UIA2 or UIA3 for the given identifier."""
        if identifier == "UIA2":
            from FlaUILibrary.flaui.automation.uia2 import UIA2  # pylint: disable=import-outside-toplevel
            return UIA2(retry_timeout_in_milliseconds)
        if identifier == "UIA3":
            from FlaUILibrary.flaui.automation.uia3 import UIA3  # pylint: disable=import-outside-toplevel
            return UIA3(retry_timeout_in_milliseconds)
        raise FlaUiError("Identifier not supported")
