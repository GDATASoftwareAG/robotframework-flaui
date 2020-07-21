from abc import ABC, abstractmethod


class ModuleInterface(ABC):
    """Module interface class for ui component handling."""

    @abstractmethod
    def execute_action(self, action, values=None):
        """Executes a defined action method.

        Args:
            action (Action): Specific action to call for execution.
            values (Object): Parameter values to use for method execution.
        """
        raise NotImplementedError('Subclasses must override execute_action method')
