from enum import Enum
from typing import Any

from FlaUILibrary.flaui.process.elementhandle import ElementHandle
from FlaUILibrary.flaui.process.enumhandle import EnumHandle
from FlaUILibrary.flaui.util.automationelement import AutomationElement as PyAutomationElement


class ValueClassifier:
    """Classifies values at the process boundary."""

    @staticmethod
    def is_python_value(value: Any) -> bool:
        """Return True if value can cross the process boundary as-is."""
        return value is None or isinstance(
            value, (bool, int, float, str, bytes, Enum, PyAutomationElement, ElementHandle, EnumHandle)
        )

    @staticmethod
    def is_automation_element(value: Any) -> bool:
        """Return True if value is a native FlaUI automation element."""
        if isinstance(value, PyAutomationElement):
            return False
        type_name = type(value).__name__
        module_name = getattr(type(value), "__module__", "") or ""
        return "AutomationElement" in type_name or "AutomationElements" in module_name

    @staticmethod
    def is_native(value: Any) -> bool:
        """Return True if value is a .NET object that cannot be pickled."""
        if ValueClassifier.is_python_value(value):
            return False
        module_name = getattr(type(value), "__module__", "") or ""
        return (
            module_name.startswith("FlaUI")
            or module_name.startswith("System")
            or module_name.startswith("Interop.UIAutomationClient")
        )

    @staticmethod
    def is_native_enum(value: Any) -> bool:
        """Return True if value is a Python Enum backed by a .NET value."""
        return isinstance(value, Enum) and ValueClassifier.is_native(value.value)
