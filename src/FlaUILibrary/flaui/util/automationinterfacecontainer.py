from typing import Dict
from FlaUILibrary.flaui.interface.windowsautomationinterface import WindowsAutomationInterface
from FlaUILibrary.flaui.automation.uiaisolation import create_automation_module


class AutomationInterfaceContainer:
    """
    Automation interface container to manage all graphical user interfaces like UIA2 and UIA3.
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
        self._modules: Dict[str, WindowsAutomationInterface] = {}
        self._retry_timeout_in_milliseconds = retry_timeout_in_milliseconds

    def create_or_get_module(self):
        """
        Creates user interface module if not already created otherwise initialized module.
        """
        if self._identifier not in self._modules:
            self._modules[self._identifier] = self._create_module()

        return self._modules[self._identifier]

    def get_identifier(self):
        """
        Gets current active user graphical interface module like UIA2 or UIA3.
        """
        return self._identifier

    def _create_module(self):
        """
        Creates user interface module if not already created otherwise initialized module.
        """
        return create_automation_module(self._identifier, self._retry_timeout_in_milliseconds)
