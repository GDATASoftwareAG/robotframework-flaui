"""Proxy that talks to a UIA worker process over a local connection."""
from __future__ import annotations

import atexit
import os
import secrets
import subprocess
import sys
import threading
from enum import Enum
from multiprocessing.connection import Listener
from typing import Any

from FlaUILibrary.flaui.enum.interfacetype import InterfaceType
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.interface.windowsautomationinterface import WindowsAutomationInterface

_WORKER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uiaworker.py")
_CONNECT_TIMEOUT_IN_SECONDS = 30
_CREATE_NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


class RemoteUIA(WindowsAutomationInterface):
    """Forwards UIA calls to a dedicated helper process for one identifier."""

    def __init__(self, identifier: str, retry_timeout_in_milliseconds: int, output_dir: str = None):
        self._identifier = identifier
        self._process = None
        self._parent_conn = None
        authkey = secrets.token_bytes(32)
        listener = Listener(("127.0.0.1", 0), authkey=authkey)
        try:
            self._process = self._spawn_worker(
                identifier,
                retry_timeout_in_milliseconds,
                listener.address,
                authkey,
                output_dir,
            )
            self._parent_conn = self._accept(listener)
        except Exception:
            listener.close()
            self.shutdown()
            raise
        listener.close()
        atexit.register(self.shutdown)

    def identifier(self):
        """Return UIA2 or UIA3 for this helper process."""
        return self._identifier

    def register_action(self, automation: Any, retry_timeout_in_milliseconds: int):  # pylint: disable=unused-argument
        """Actions are registered inside the helper process."""
        return None

    def get_element(self, identifier: str, ui_type: InterfaceType = None, msg: str = None):
        """Find an element by XPath in the helper process."""
        return self._call("get_element", identifier, ui_type, msg)

    def action(self, action: Enum, values: ValueContainer = None, msg: str = None):
        """Execute a FlaUI module action in the helper process."""
        return self._call("action", action, values, msg)

    def shutdown(self) -> None:
        """Stop the helper process."""
        process = self._process
        connection = self._parent_conn
        self._process = None
        self._parent_conn = None
        if connection is not None:
            try:
                connection.send(("shutdown",))
            except (OSError, EOFError, BrokenPipeError):
                pass
            try:
                connection.close()
            except (OSError, EOFError, BrokenPipeError):
                pass
        if process is None:
            return
        try:
            process.wait(5)
        except subprocess.TimeoutExpired:
            process.terminate()
            try:
                process.wait(5)
            except subprocess.TimeoutExpired:
                process.kill()

    def _call(self, *request: Any) -> Any:
        if self._process is None or self._process.poll() is not None:
            raise FlaUiError(f"{self._identifier} helper process is not running")
        try:
            self._parent_conn.send(request)
            status, payload = self._parent_conn.recv()
        except (OSError, EOFError, BrokenPipeError) as error:
            raise FlaUiError(f"{self._identifier} helper process failed: {error}") from error
        if status == "error":
            raise FlaUiError(payload)
        return payload

    @staticmethod
    def _spawn_worker(identifier: str,
                      retry_timeout_in_milliseconds: int,
                      address: Any,
                      authkey: bytes,
                      output_dir: str) -> subprocess.Popen:
        host, port = address
        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join(sys.path)
        args = [
            sys.executable,
            _WORKER,
            identifier,
            str(retry_timeout_in_milliseconds),
            host,
            str(port),
            authkey.hex(),
            output_dir or "",
        ]
        return subprocess.Popen(  # pylint: disable=consider-using-with
            args,
            env=env,
            creationflags=_CREATE_NO_WINDOW,
        )

    def _accept(self, listener: Listener):
        result = []
        error = []

        def wait_for_client():
            try:
                result.append(listener.accept())
            except Exception as accept_error:  # pylint: disable=broad-except
                error.append(accept_error)

        waiter = threading.Thread(target=wait_for_client)
        waiter.daemon = True
        waiter.start()
        waiter.join(_CONNECT_TIMEOUT_IN_SECONDS)

        if self._process is not None and self._process.poll() is not None:
            raise FlaUiError(f"{self._identifier} helper process exited before it was ready")
        if error:
            raise FlaUiError(f"{self._identifier} helper process failed: {error[0]}") from error[0]
        if not result:
            raise FlaUiError(f"{self._identifier} helper process did not connect")
        return result[0]
