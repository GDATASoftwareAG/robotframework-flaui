"""One helper process per UIA identifier so UIA2 and UIA3 never share a process."""
from __future__ import annotations

import threading
from typing import Dict

from FlaUILibrary.flaui.interface.windowsautomationinterface import WindowsAutomationInterface
from FlaUILibrary.flaui.automation.remoteuia import RemoteUIA
from FlaUILibrary.robotframework import robotlog

_LOCK = threading.Lock()
_MODULES: Dict[str, RemoteUIA] = {}


def create_automation_module(identifier: str,
                             retry_timeout_in_milliseconds: int) -> WindowsAutomationInterface:
    """Return the worker process for UIA2 or UIA3, creating it on first use."""
    with _LOCK:
        if identifier not in _MODULES:
            _MODULES[identifier] = RemoteUIA(
                identifier,
                retry_timeout_in_milliseconds,
                robotlog.get_log_directory(),
            )
        return _MODULES[identifier]
