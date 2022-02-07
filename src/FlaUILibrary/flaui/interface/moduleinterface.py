from abc import ABC, abstractmethod
from enum import Enum
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer


class ModuleInterface(ABC):
    """
    Interface class to implement all FlaUI wrapper modules from Python to C#.
    Module package contains all component implementations from FlaUI usage.
    """

    @abstractmethod
    def execute_action(self, action: Enum, values: ValueContainer):
        """
        Executes a defined action method.

        Args:
            action: Enumeration from supported actions.
            values: Value container object which stores arguments from action.
        """
        raise NotImplementedError('Subclass must override execute_action method')
