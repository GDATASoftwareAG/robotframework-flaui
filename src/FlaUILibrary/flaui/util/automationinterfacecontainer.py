from typing import Dict
from FlaUILibrary.flaui.interface import WindowsAutomationInterface


class AutomationInterfaceContainer:

    def __init__(self, modules: Dict[str, WindowsAutomationInterface], identifier: str):
        self._modules = modules
        self._identifier = identifier

    def get_module(self):
        return self._modules[self._identifier]

    def set_identifier(self, identifier: str):
        self._identifier = identifier
