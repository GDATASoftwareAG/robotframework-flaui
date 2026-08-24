from __future__ import annotations

import atexit
import os
import sys
from enum import Enum
from typing import Any

import execnet

from FlaUILibrary.flaui.enum.interfacetype import InterfaceType
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.process.elementcodec import ElementCodec
from FlaUILibrary.flaui.process.uiaworker import UiaWorker


class UiaProcess:
    """Forwards action and get_element calls to a dedicated helper process."""

    def __init__(self, identifier: str, retry_timeout_in_milliseconds: int, output_dir: str = None):
        self._identifier = identifier
        self._group = None
        self._channel = None
        try:
            self._group = execnet.Group()
            gateway = self._group.makegateway("popen//execmodel=main_thread_only")
            self._prepare_sys_path(gateway)
            self._start_worker(gateway, identifier, retry_timeout_in_milliseconds, output_dir)
        except Exception:
            self.shutdown()
            raise
        atexit.register(self.shutdown)

    def identifier(self):
        """Return UIA2 or UIA3 for this helper process."""
        return self._identifier

    def get_element(self, identifier: str, ui_type: InterfaceType = None, msg: str = None):
        """Find an element by XPath in the helper process."""
        return self._call("get_element", identifier, ui_type, msg)

    def action(self, action: Enum, values: ValueContainer = None, msg: str = None):
        """Execute a FlaUI module action in the helper process."""
        return self._call("action", action, ElementCodec.encode(values), msg)

    def shutdown(self) -> None:
        """Stop the helper process."""
        channel = self._channel
        group = self._group
        self._channel = None
        self._group = None
        if channel is not None:
            try:
                channel.send(UiaWorker.dumps(("shutdown",)))
                channel.waitclose(5)
            except Exception:  # pylint: disable=broad-except
                pass
        if group is not None:
            group.terminate(5)

    def _call(self, *request: Any) -> Any:
        if self._channel is None:
            raise FlaUiError(f"{self._identifier} helper process is not running")
        try:
            self._channel.send(UiaWorker.dumps(request))
            status, payload = UiaWorker.loads(self._channel.receive())
        except Exception as error:  # pylint: disable=broad-except
            raise FlaUiError(f"{self._identifier} helper process failed: {error}") from error
        if status == "error":
            raise FlaUiError(payload)
        return payload

    def _start_worker(self,
                      gateway,
                      identifier: str,
                      retry_timeout_in_milliseconds: int,
                      output_dir: str) -> None:
        self._channel = gateway.remote_exec(
            "from FlaUILibrary.flaui.process.uiaworker import UiaWorker\n"
            "UiaWorker.start(channel)"
        )
        self._channel.send(UiaWorker.dumps((identifier, retry_timeout_in_milliseconds, output_dir)))

    @staticmethod
    def _prepare_sys_path(gateway) -> None:
        package_file = sys.modules["FlaUILibrary"].__file__
        package_parent = os.path.dirname(os.path.dirname(os.path.abspath(package_file)))
        channel = gateway.remote_exec("import sys; sys.path.insert(0, channel.receive())")
        channel.send(package_parent)
        channel.waitclose()
