from abc import ABC, abstractmethod
from typing import Any
from enum import Enum
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer


class WindowsAutomationInterface(ABC):
    """
    Generic windows automation interface to react on keyword usage from robotframework to FlaUI modules.
    """

    @abstractmethod
    def action(self, action: Enum, values: ValueContainer, msg: str = None):
        """
        Performs a defined action like a button click.

        Args:
            action : User interface action to perform.
            values : Argument container for actions.
            msg    : Custom error message.
        """
        raise NotImplementedError('Subclass must override action method')

    @abstractmethod
    def register_action(self, automation: Any):
        """
        Register all supported core actions.

        Args:
            automation (Object)       : Windows user automation object.
        """
        raise NotImplementedError('Subclass must override action method')

    @abstractmethod
    def identifier(self):
        """
        Returns identifier which windows automation interface is in usage.
        """
        raise NotImplementedError('Subclass must override action method')
