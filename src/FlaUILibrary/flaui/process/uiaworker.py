import pickle
from typing import Any

from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.process.elementcodec import ElementCodec
from FlaUILibrary.flaui.process.uiafactory import UiaFactory
from FlaUILibrary.robotframework import robotlog


class UiaWorker:
    """Hosts one UIA backend and executes module actions until shutdown."""

    def __init__(self, identifier: str, retry_timeout_in_milliseconds: int, channel, output_dir: str = None):
        self._channel = channel
        self._codec = ElementCodec()
        self._bind_output_dir(output_dir)
        self._module = UiaFactory.create(identifier, retry_timeout_in_milliseconds)

    def run(self) -> None:
        """Serve action and get_element calls until shutdown."""
        while True:
            request = UiaWorker.loads(self._channel.receive())
            operation = request[0]
            if operation == "shutdown":
                break
            try:
                result = self._dispatch(operation, request)
                self._channel.send(UiaWorker.dumps(("ok", result)))
            except FlaUiError as error:
                self._channel.send(UiaWorker.dumps(("error", str(error))))
            except Exception as error:  # pylint: disable=broad-except
                self._channel.send(UiaWorker.dumps(("error", str(error))))

    def _dispatch(self, operation: str, request) -> Any:
        if operation == "get_element":
            return self._codec.wrap(self._module.get_element(request[1], request[2], request[3]))
        if operation == "action":
            return self._codec.wrap(self._module.action(request[1], self._codec.unwrap(request[2]), request[3]))
        if operation == "identifier":
            return self._module.identifier()
        raise FlaUiError(FlaUiError.ActionNotSupported)

    @staticmethod
    def dumps(value: Any) -> bytes:
        """Serialize a request or response for the execnet channel."""
        return pickle.dumps(value, protocol=4)

    @staticmethod
    def loads(value: bytes) -> Any:
        """Deserialize a request or response from the execnet channel."""
        return pickle.loads(value)

    @staticmethod
    def _bind_output_dir(output_dir: str) -> None:
        if output_dir:
            robotlog.get_log_directory = lambda: output_dir

    @staticmethod
    def start(channel) -> None:
        """Host one UIA backend on an execnet channel until shutdown."""
        identifier, retry_timeout_in_milliseconds, output_dir = UiaWorker.loads(channel.receive())
        UiaWorker(identifier, retry_timeout_in_milliseconds, channel, output_dir).run()
