from abc import ABC, abstractmethod


class WindowsAutomationInterface(ABC):
    """Generic windows automation interface to react on keyword usage from robotframework to FlaUI modules."""

    @abstractmethod
    def action(self, action, value=None, msg=None):
        """Performs a defined action like a button click.

        Args:
            action (Action)           : User interface action to perform.
            value  (Array)            : Specified arguments for actions as array.
            msg    (String) *Optional : Custom error message.
        """
        raise NotImplementedError('Subclass must override action method')

    @abstractmethod
    def register_action(self, automation):
        """Register all supported core actions.

        Args:
            automation (Object)       : Windows user automation object.
        """
        raise NotImplementedError('Subclass must override action method')

    @abstractmethod
    def identifier(self):
        """ Returns identifier which windows automation interface is in usage."""
        raise NotImplementedError('Subclass must override action method')
