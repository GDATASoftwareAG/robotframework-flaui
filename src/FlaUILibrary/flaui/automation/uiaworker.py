"""Worker process that hosts a single UIA2 or UIA3 backend."""
import os
import sys
from enum import Enum
from multiprocessing.connection import Client
from typing import Any, Dict

from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.util.automationelement import AutomationElement as PyAutomationElement


class ElementRef:
    """Picklable reference to a native FlaUI element stored in the worker."""

    def __init__(self, handle: int):
        self.handle = handle


def _is_python_value(value: Any) -> bool:
    return value is None or isinstance(
        value, (bool, int, float, str, bytes, Enum, PyAutomationElement, ElementRef)
    )


def _is_automation_element(value: Any) -> bool:
    type_name = type(value).__name__
    module_name = getattr(type(value), "__module__", "") or ""
    return "AutomationElement" in type_name or "AutomationElements" in module_name


def _is_native(value: Any) -> bool:
    if _is_python_value(value):
        return False
    module_name = getattr(type(value), "__module__", "") or ""
    return (
            module_name.startswith("FlaUI")
            or module_name.startswith("System")
            or module_name.startswith("Interop.UIAutomationClient")
    )


def _create_module(identifier: str, retry_timeout_in_milliseconds: int):
    # Import inside the worker so the Robot process never constructs UIA2/UIA3.
    if identifier == "UIA2":
        from FlaUILibrary.flaui.automation.uia2 import UIA2  # pylint: disable=import-outside-toplevel
        return UIA2(retry_timeout_in_milliseconds)
    if identifier == "UIA3":
        from FlaUILibrary.flaui.automation.uia3 import UIA3  # pylint: disable=import-outside-toplevel
        return UIA3(retry_timeout_in_milliseconds)
    raise FlaUiError("Identifier not supported")


def run_worker(identifier: str,
               retry_timeout_in_milliseconds: int,
               conn,
               output_dir: str = None) -> None:
    """Serve action and get_element calls for one UIA identifier until shutdown."""
    if output_dir:
        os.environ["FLAUI_OUTPUT_DIR"] = output_dir

    handles: Dict[int, Any] = {}
    next_handle = [1]
    module = _create_module(identifier, retry_timeout_in_milliseconds)

    def wrap(value: Any) -> Any:
        result = value
        if isinstance(value, list):
            result = [wrap(item) for item in value]
        elif isinstance(value, tuple):
            result = tuple(wrap(item) for item in value)
        elif isinstance(value, dict):
            result = {key: wrap(item) for key, item in value.items()}
        elif _is_automation_element(value):
            handle = next_handle[0]
            next_handle[0] += 1
            handles[handle] = value
            result = ElementRef(handle)
        elif _is_native(value):
            to_string = getattr(value, "ToString", None)
            result = str(to_string()) if callable(to_string) else str(value)
        return result

    def unwrap(value: Any) -> Any:
        if isinstance(value, ElementRef):
            return handles[value.handle]
        if isinstance(value, dict):
            return {key: unwrap(item) for key, item in value.items()}
        if isinstance(value, list):
            return [unwrap(item) for item in value]
        if isinstance(value, tuple):
            return tuple(unwrap(item) for item in value)
        return value

    while True:
        request = conn.recv()
        operation = request[0]
        if operation == "shutdown":
            break
        try:
            if operation == "get_element":
                result = wrap(module.get_element(request[1], request[2], request[3]))
            elif operation == "action":
                result = wrap(module.action(request[1], unwrap(request[2]), request[3]))
            else:
                raise FlaUiError(FlaUiError.ActionNotSupported)
            conn.send(("ok", result))
        except FlaUiError as error:
            conn.send(("error", str(error)))
        except Exception as error:  # pylint: disable=broad-except
            conn.send(("error", str(error)))


def main(argv=None) -> None:
    """Connect back to the Robot process and host one UIA backend."""
    argv = sys.argv[1:] if argv is None else argv
    identifier = argv[0]
    retry_timeout_in_milliseconds = int(argv[1])
    host = argv[2]
    port = int(argv[3])
    authkey = bytes.fromhex(argv[4])
    output_dir = argv[5] if len(argv) > 5 and argv[5] else None
    conn = Client((host, port), authkey=authkey)
    run_worker(identifier, retry_timeout_in_milliseconds, conn, output_dir)


if __name__ == "__main__":
    main()
