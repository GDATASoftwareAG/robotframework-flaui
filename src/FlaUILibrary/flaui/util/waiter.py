import time
from typing import Any, Callable, NoReturn, Optional
from FlaUILibrary.flaui.exception.flauierror import FlaUiError


class Waiter:
    """
    Poll a condition like BuiltIn.Wait Until Keyword Succeeds.

    ``retry`` is a count (``10x``, ``5 times``) or a timeout. ``retry_interval``
    is the time to wait after a failed attempt. Exhausted retry raises FlaUiError.
    """

    @staticmethod
    def wait_until(predicate: Callable[[], Any],
                   retry_mode: str,
                   retry_value: float,
                   retry_interval: float,
                   error_factory: Optional[Callable[[], Exception]] = None) -> Any:
        """
        Run ``predicate`` until it returns a truthy value or retry is exhausted.

        Args:
            predicate (Callable): Condition to evaluate. A falsy result is retried.
            retry_mode (String): ``count`` or ``timeout``
            retry_value (float): Attempt count or timeout in seconds
            retry_interval (float): Sleep after a failed attempt in seconds
            error_factory (Callable): Optional factory used when retry is exhausted

        Returns:
            Any: The truthy predicate result.

        Raises:
            FlaUiError: When retry is exhausted.
        """
        last_error = None
        count = int(retry_value) if retry_mode == "count" else -1
        deadline = time.monotonic() + retry_value if retry_mode == "timeout" else None

        while True:
            try:
                result = predicate()
                if result:
                    return result
            except FlaUiError as err:
                last_error = err

            if retry_mode == "count":
                count -= 1
                if count <= 0:
                    Waiter._raise_retry_exhausted(last_error, error_factory)
            elif deadline is not None and time.monotonic() >= deadline:
                Waiter._raise_retry_exhausted(last_error, error_factory)

            time.sleep(retry_interval)

    @staticmethod
    def _raise_retry_exhausted(last_error, error_factory) -> NoReturn:
        if error_factory:
            raise error_factory()
        if last_error:
            raise last_error
        raise FlaUiError(FlaUiError.GenericError.format("Retry exhausted"))
