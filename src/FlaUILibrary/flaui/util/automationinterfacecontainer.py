from FlaUILibrary.flaui.process.uiaprocess import UiaProcess
from FlaUILibrary.robotframework import robotlog


class AutomationInterfaceContainer:
    """
    Automation interface container to manage one graphical user interface, UIA2 or UIA3.
    """

    def __init__(self, identifier: str, retry_timeout_in_milliseconds: int):
        """
        Initializes AutomationInterfaceContainer.

        Args:
            identifier (str): UIA2 or UIA3 identifier to use.
            retry_timeout_in_milliseconds (Number):
              Timeout in milliseconds for automatic retry if element could not be found.
        """
        self._identifier = identifier
        self._module = None
        self._retry_timeout_in_milliseconds = retry_timeout_in_milliseconds

    def create_or_get_module(self):
        """
        Creates user interface module if not already created otherwise initialized module.
        """
        if self._module is None:
            self._module = UiaProcess(
                self._identifier,
                self._retry_timeout_in_milliseconds,
                robotlog.get_log_directory(),
            )

        return self._module

    def get_identifier(self):
        """
        Gets current active user graphical interface module like UIA2 or UIA3.
        """
        return self._identifier
