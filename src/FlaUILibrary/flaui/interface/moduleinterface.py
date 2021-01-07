from abc import ABC, abstractmethod


class ModuleInterface(ABC):
    """
    Interface class to implement all FlaUI wrapper modules from Python to C#.
    Module package contains all component implementations from FlaUI usage.
    """

    @abstractmethod
    def execute_action(self, action, values=None):
        """Executes a defined action method.

        Args:
            action (Action): Specific action to call for execution.
            values (Object): Parameter values to use for method execution.
        """
        raise NotImplementedError('Subclass must override execute_action method')
