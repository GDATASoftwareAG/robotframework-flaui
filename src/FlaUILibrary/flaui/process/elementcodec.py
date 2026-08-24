import importlib
from dataclasses import fields, is_dataclass
from enum import Enum
from typing import Any, Callable, Dict

from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.process.elementhandle import ElementHandle
from FlaUILibrary.flaui.process.enumhandle import EnumHandle
from FlaUILibrary.flaui.process.valueclassifier import ValueClassifier


class ElementCodec:
    """Converts values at the process boundary so native FlaUI objects stay in the worker."""

    def __init__(self):
        self._handles: Dict[int, Any] = {}
        self._next_handle = 1

    @staticmethod
    def encode(value: Any) -> Any:
        """Make values picklable before they leave the Robot process."""
        if is_dataclass(value) and not isinstance(value, type):
            return {item.name: ElementCodec.encode(getattr(value, item.name)) for item in fields(value)}
        if isinstance(value, dict):
            return {key: ElementCodec.encode(item) for key, item in value.items()}
        if isinstance(value, list):
            return [ElementCodec.encode(item) for item in value]
        if isinstance(value, tuple):
            return tuple(ElementCodec.encode(item) for item in value)
        if ValueClassifier.is_native_enum(value):
            return EnumHandle(value.__class__.__module__, value.__class__.__qualname__, value.name)
        return value

    def wrap(self, value: Any) -> Any:
        """Replace native elements with handles and other .NET objects with strings."""
        return self._transform(value, self._wrap_item)

    def unwrap(self, value: Any) -> Any:
        """Restore native elements and enums before module execution."""
        return self._transform(value, self._unwrap_item)

    def _wrap_item(self, value: Any) -> Any:
        if ValueClassifier.is_automation_element(value):
            handle = self._next_handle
            self._next_handle += 1
            self._handles[handle] = value
            return ElementHandle(handle)
        if ValueClassifier.is_native(value):
            to_string = getattr(value, "ToString", None)
            return str(to_string()) if callable(to_string) else str(value)
        return value

    def _unwrap_item(self, value: Any) -> Any:
        if isinstance(value, ElementHandle):
            return self._handles[value.handle]
        if isinstance(value, EnumHandle):
            return self._decode_enum(value)
        return value

    @staticmethod
    def _decode_enum(value: EnumHandle) -> Enum:
        module = importlib.import_module(value.module)
        enum_cls = module
        for part in value.qualname.split("."):
            enum_cls = getattr(enum_cls, part)
        try:
            return getattr(enum_cls, value.name)
        except AttributeError as error:
            raise FlaUiError(f"Unknown enum value {value.qualname}.{value.name}") from error

    @staticmethod
    def _transform(value: Any, convert: Callable[[Any], Any]) -> Any:
        if is_dataclass(value) and not isinstance(value, type):
            return {
                item.name: ElementCodec._transform(getattr(value, item.name), convert)
                for item in fields(value)
            }
        if isinstance(value, list):
            return [ElementCodec._transform(item, convert) for item in value]
        if isinstance(value, tuple):
            return tuple(ElementCodec._transform(item, convert) for item in value)
        if isinstance(value, dict):
            return {key: ElementCodec._transform(item, convert) for key, item in value.items()}
        return convert(value)
