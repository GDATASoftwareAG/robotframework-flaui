from abc import ABC, abstractmethod


class WindowsAutomationInterface(ABC):
    """Windows automation interface for all FlaUI components."""

    @abstractmethod
    def action(self, action, value=None, msg=None):
        """Performs a defined windows ui api action.

        Args:
            action (Action) : Application action to perform.
            value  (Array)  : Specified arguments for actions as array.
            msg    (String) : Optional custom error message.
        """
        raise NotImplementedError('Subclasses must override action method')
