from typing import Dict
from FlaUILibrary.flaui.interface import WindowsAutomationInterface
from FlaUILibrary.flaui.exception import FlaUiError


class AutomationInterfaceContainer:

    def __init__(self, timeout: int, identifier: str):
        self._identifier = identifier
        self._modules: Dict[str, WindowsAutomationInterface] = {}
        self._timeout = timeout

    def create_or_get_module(self):
        if self._identifier not in self._modules:
            self._modules[self._identifier] = self._create_module()

        return self._modules[self._identifier]

    def set_identifier(self, identifier: str):
        self._identifier = identifier

    def get_identifier(self):
        return self._identifier

    def _create_module(self):
        from FlaUILibrary.flaui.automation.uia2 import UIA2
        from FlaUILibrary.flaui.automation.uia3 import UIA3

        if self._identifier == "UIA2":
            return UIA2(self._timeout)
        elif self._identifier == "UIA3":
            return UIA3(self._timeout)

        FlaUiError.raise_fla_ui_error("Identifier not supported")
