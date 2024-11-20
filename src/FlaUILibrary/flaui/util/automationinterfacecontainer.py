from typing import Dict
from FlaUILibrary.flaui.interface import WindowsAutomationInterface
from FlaUILibrary.flaui.exception import FlaUiError


class AutomationInterfaceContainer:
    """
    Automation interface container to manage all graphical user interfaces like UIA2 and UIA3.
    """

    def __init__(self, timeout: int, identifier: str):
        self._identifier = identifier
        self._modules: Dict[str, WindowsAutomationInterface] = {}
        self._timeout = timeout

    def create_or_get_module(self):
        """
        Creates user interface module if not already created otherwise initialized module.
        """
        if self._identifier not in self._modules:
            self._modules[self._identifier] = self._create_module()

        return self._modules[self._identifier]

    def set_identifier(self, identifier: str):
        """
        Sets UIA2 or UIA3 identifier to use.

        Args:
            identifier (String): UIA2 or UIA3
        """
        self._identifier = identifier

    def get_identifier(self):
        """
        Gets current active user graphical interface module like UIA2 or UIA3.
        """
        return self._identifier

    def _create_module(self):
        # pylint: disable=C0415
        from FlaUILibrary.flaui.automation.uia2 import UIA2
        from FlaUILibrary.flaui.automation.uia3 import UIA3
        # pylint: enable=C0415

        if self._identifier == "UIA2":
            return UIA2(self._timeout)

        if self._identifier == "UIA3":
            return UIA3(self._timeout)

        raise FlaUiError("Identifier not supported")
