import time
from enum import Enum
import os
from typing import Optional, Any
import FlaUI.Core  # pylint: disable=import-error
from System.ComponentModel import Win32Exception  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.util.waiter import Waiter
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer


class Application(ModuleInterface):
    """
    Application control module wrapper for FlaUI usage.
    Wrapper module executes methods from Application class implementation by Application.cs.
    """

    class Container(ValueContainer):
        """
        Value container from application module.
        """
        name: Optional[str]
        pid: Optional[int]
        args: Optional[str]
        retry_mode: Optional[str]
        retry_value: Optional[float]
        retry_interval: Optional[float]

    class ApplicationContainer:
        """
        Application container to handle an attached or launched process.
        """
        pid: Optional[int]
        name: Optional[str]
        application: Optional[str]

        def __init__(self, pid: int, name: str, application: Any):
            """
            Application container class to store applications.

            Args:
                pid (int): Process id
                name (str): Process name
                application (Object) : Application object to store.
            """
            self.pid = pid
            self.name = name
            self.application = application

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        ATTACH_APPLICATION_BY_NAME = "APPLICATION_ATTACH_BY_NAME"
        ATTACH_APPLICATION_BY_PID = "APPLICATION_ATTACH_BY_PID"
        LAUNCH_APPLICATION = "APPLICATION_LAUNCH"
        LAUNCH_APPLICATION_WITH_ARGS = "APPLICATION_LAUNCH_WITH_ARGS"
        EXIT_APPLICATION = "APPLICATION_EXIT"
        CLOSE_APPLICATION_BY_NAME = "APPLICATION_CLOSE_BY_NAME"
        WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_NAME = "APPLICATION_WAIT_WHILE_HANDLE_IS_MISSING_BY_NAME"
        WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_PID = "APPLICATION_WAIT_WHILE_HANDLE_IS_MISSING_BY_PID"
        WAIT_WHILE_APPLICATION_IS_BUSY_BY_NAME = "APPLICATION_WAIT_WHILE_IS_BUSY_BY_NAME"
        WAIT_WHILE_APPLICATION_IS_BUSY_BY_PID = "APPLICATION_WAIT_WHILE_IS_BUSY_BY_PID"

    def __init__(self):
        """
        Application module wrapper for FlaUI usage.
        """
        self._applications = []

    @staticmethod
    def create_value_container(name=None,
                               pid=None,
                               retry="10x",
                               retry_interval="1s",
                               args=None,
                               msg=None) -> Container:
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            name (String): Name from application
            pid (Number): PID number to attach to process
            retry (Number | String): Wait Until Keyword Succeeds retry as count or timeout
            retry_interval (Number | String): Time to wait after a failed attempt
            args (String): Arguments to use by application
            msg (String): Optional error message
        """
        retry_mode, retry_value = Converter.cast_to_retry(retry, default="10x", error_msg=msg)
        return Application.Container(name=Converter.cast_to_string(name),
                                     pid=Converter.cast_to_int(pid, msg),
                                     retry_mode=retry_mode,
                                     retry_value=retry_value,
                                     retry_interval=Converter.cast_to_timestr_seconds(
                                         retry_interval, default=1, error_msg=msg),
                                     args=Converter.cast_to_string(args))

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        Execute all supported actions from application module wrapper by FlaUI.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action: Method action to use.
            values: See supported action definitions for value usage and value container definition.
        """

        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.ATTACH_APPLICATION_BY_NAME:
                lambda: self._attach_application_by_name(values),
            self.Action.ATTACH_APPLICATION_BY_PID:
                lambda: self._attach_application_by_pid(values),
            self.Action.LAUNCH_APPLICATION:
                lambda: self._launch_application(values),
            self.Action.LAUNCH_APPLICATION_WITH_ARGS:
                lambda: self._launch_application_with_args(values),
            self.Action.EXIT_APPLICATION:
                lambda: self._exit_application_by_pid(values),
            self.Action.CLOSE_APPLICATION_BY_NAME:
                lambda: self._exit_application_by_name(values),
            self.Action.WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_PID:
                lambda: self._wait_while_main_handle_is_missing_by_pid(values),
            self.Action.WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_NAME:
                lambda: self._wait_while_main_handle_is_missing_by_name(values),
            self.Action.WAIT_WHILE_APPLICATION_IS_BUSY_BY_NAME:
                lambda: self._wait_while_busy_by_name(values),
            self.Action.WAIT_WHILE_APPLICATION_IS_BUSY_BY_PID:
                lambda: self._wait_while_busy_by_pid(values),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _attach_application_by_name(self, container: Container) -> int:
        """
        Attach to a running process by name and register the attached application.

        Args:
            container (Container): Must contain `name`.

        Returns:
            int: Process id of the attached application.

        Raises:
            FlaUiError: If no process with the given name can be attached.
        """
        name = container["name"]
        try:
            return self._add_application(self._flaui_attach_application_by_name(name))
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationNameNotFound.format(name)) from None

    def _attach_application_by_pid(self, container: Container) -> int:
        """
        Attach to a running process by pid and register the attached application.

        Args:
            container (Container): Must contain `pid`.

        Returns:
            int: Process id of the attached application.

        Raises:
            FlaUiError: If no process with the given pid can be attached.
        """
        pid = container["pid"]
        try:
            return self._add_application(self._flaui_attach_application_by_pid(pid))
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationPidNotFound.format(pid)) from None

    def _launch_application(self, container: Container) -> int:
        """
        Launch an application without additional arguments and register the launched process.

        Args:
            container (Container): Must contain `name`.

        Returns:
            int: Process id of the launched application.

        Raises:
            FlaUiError: If the application cannot be launched.
        """
        application = container["name"]
        try:
            return self._add_application(self._flaui_launch_application(application))
        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None

    def _launch_application_with_args(self, container: Container) -> int:
        """
        Launch an application with supplied arguments and register the launched process.

        Args:
            container (Container): Must contain `name` and optional `args`.

        Returns:
            int: Process id of the launched application.

        Raises:
            FlaUiError: If the application cannot be launched.
        """
        application = container["name"]
        arguments = container["args"]

        try:
            return self._add_application(self._flaui_launch_application(application, arguments))
        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None

    def _exit_application_by_pid(self, container: Container) -> None:
        """
        Terminate an attached application identified by pid and remove it from the registry.

        Args:
            container (Container): Must contain `pid`.

        Raises:
            FlaUiError: If no attached application with the given pid exists or termination fails.
        """
        self._stop_application(self._get_attached_application_by_pid(container))

    def _exit_application_by_name(self, container: Container) -> None:
        """
        Terminate an application identified by name and remove it from the registry.

        If the process is not already attached, attach to it first so processes started
        outside FlaUI can be closed by name.

        Args:
            container (Container): Must contain `name`.

        Raises:
            FlaUiError: If no running application with the given name exists or termination fails.
        """
        attached = self._find_attached_application_by_name(container["name"])
        if attached is None:
            pid = self._attach_application_by_name(container)
            attached = self._get_attached_application_by_pid(
                Application.create_value_container(pid=pid))
        self._stop_application(attached)

    def _stop_application(self, app_container: ApplicationContainer) -> None:
        """
        Terminate the application represented by the provided ApplicationContainer
        and remove its container from the internal registry.

        Args:
            app_container (ApplicationContainer): The application container holding
                the FlaUI application instance to terminate.

        Raises:
            FlaUiError: If terminating the application fails or the container is
                not present in the internal applications list.
        """
        app_container.application.Kill()
        self._applications.remove(app_container)

    def _get_attached_application_by_pid(self, container: Container) -> ApplicationContainer:
        """
        Return the stored ApplicationContainer for an attached application by pid.

        Args:
            container (Container): Must contain `pid`.

        Returns:
            ApplicationContainer: The matched stored application container.

        Raises:
            FlaUiError: If no attached application with the given pid exists.
        """
        pid = container["pid"]
        for application in self._applications:
            if application.pid == pid:
                return application

        raise FlaUiError(FlaUiError.ApplicationNotAttached) from None

    def _find_attached_application_by_name(self, name: str) -> Optional[ApplicationContainer]:
        """
        Return the stored ApplicationContainer whose process name matches ``name``.

        Matching ignores path, ``.exe`` suffix and case so the same identifier can be
        used for Attach Application By Name and Close Application By Name.

        Args:
            name (str): Process name, executable name or path used to identify the application.

        Returns:
            ApplicationContainer: The matched stored application container, or None.
        """
        normalized = Application._normalize_application_name(name)
        if not normalized:
            return None

        for application in self._applications:
            if Application._normalize_application_name(application.name) == normalized:
                return application

        return None

    @staticmethod
    def _normalize_application_name(name: str) -> str:
        """
        Normalize a process name, executable name or path for comparison.

        Args:
            name (str): Process name, executable name or path.

        Returns:
            str: File name without path and ``.exe`` suffix, in case-insensitive form.
        """
        if not name:
            return ""

        return os.path.splitext(os.path.basename(str(name).strip()))[0].casefold()

    def _wait_while_main_handle_is_missing_by_pid(self, container: Container) -> None:
        """
        Wait until the main window handle for the application identified by pid is available.

        Args:
            container (Container): Must contain `pid`, `retry_mode`, `retry_value` and `retry_interval`.

        Raises:
            FlaUiError: If the application cannot be found by pid or retry is exhausted.
        """
        application = self._flaui_attach_application_by_pid(container["pid"])
        self._wait_for_application(
            application.WaitWhileMainHandleIsMissing,
            container,
            lambda: FlaUiError(FlaUiError.ApplicationHandleIsMissing.format(container["pid"]))
        )

    def _wait_while_main_handle_is_missing_by_name(self, container: Container) -> None:
        """
        Wait until the main window handle for the application identified by name is available.

        Args:
            container (Container): Must contain `name`, `retry_mode`, `retry_value` and `retry_interval`.

        Raises:
            FlaUiError: If the application cannot be found by name or retry is exhausted.
        """
        application = self._flaui_attach_application_by_name(container["name"])
        self._wait_for_application(
            application.WaitWhileMainHandleIsMissing,
            container,
            lambda: FlaUiError(FlaUiError.ApplicationHandleIsMissing.format(container["name"]))
        )

    def _wait_while_busy_by_pid(self, container: Container) -> None:
        """
        Wait until the application identified by pid is no longer busy.

        Args:
            container (Container): Must contain `pid`, `retry_mode`, `retry_value` and `retry_interval`.

        Raises:
            FlaUiError: If the application cannot be found by pid or retry is exhausted.
        """
        application = self._flaui_attach_application_by_pid(container["pid"])
        self._wait_for_application(
            application.WaitWhileBusy,
            container,
            lambda: FlaUiError(FlaUiError.ApplicationIsBusy.format(container["pid"]))
        )

    def _wait_while_busy_by_name(self, container: Container) -> None:
        """
        Wait until the application identified by name is no longer busy.

        Args:
            container (Container): Must contain `name`, `retry_mode`, `retry_value` and `retry_interval`.

        Raises:
            FlaUiError: If the application cannot be found by name or retry is exhausted.
        """
        application = self._flaui_attach_application_by_name(container["name"])
        self._wait_for_application(
            application.WaitWhileBusy,
            container,
            lambda: FlaUiError(FlaUiError.ApplicationIsBusy.format(container["name"]))
        )

    @staticmethod
    def _wait_for_application(wait_method, container: Container, error_factory) -> None:
        """
        Poll a FlaUI application wait method until it succeeds or retry is exhausted.

        Attach errors are raised by the caller before this helper is used.
        Each attempt waits up to ``retry_interval`` inside FlaUI, so the waiter does
        not add an extra sleep.

        Args:
            wait_method: FlaUI WaitWhileBusy or WaitWhileMainHandleIsMissing.
            container (Container): Must contain `retry_mode`, `retry_value` and `retry_interval`.
            error_factory: Factory for the FlaUiError when retry is exhausted.

        Raises:
            FlaUiError: If retry is exhausted.
        """
        slice_ms = int(container["retry_interval"] * 1000)
        retry_mode = container["retry_mode"]
        retry_value = container["retry_value"]
        deadline = time.monotonic() + retry_value if retry_mode == "timeout" else None

        Waiter.wait_until(
            lambda: Application._wait_application_slice(wait_method, slice_ms, deadline),
            retry_mode,
            retry_value,
            0,
            error_factory
        )

    @staticmethod
    def _wait_application_slice(wait_method, slice_ms: int, deadline: Optional[float]) -> bool:
        """
        Run one FlaUI wait slice, capped by remaining timeout when a deadline is set.

        Args:
            wait_method: FlaUI WaitWhileBusy or WaitWhileMainHandleIsMissing.
            slice_ms (int): Maximum wait duration for this attempt in milliseconds.
            deadline (Optional[float]): Monotonic deadline for timeout mode, otherwise None.

        Returns:
            bool: True if the FlaUI wait succeeded, False if the deadline has passed.
        """
        wait_ms = slice_ms
        if deadline is not None:
            remaining_ms = int((deadline - time.monotonic()) * 1000)
            if remaining_ms <= 0:
                return False
            wait_ms = min(slice_ms, remaining_ms)
        return wait_method(Converter.cast_to_timespan(wait_ms))

    def _exists_pid(self, pid: int) -> bool:
        """
        Check whether a process id is already present in the internal applications list.

        Args:
            pid (int): Process id to check.

        Returns:
            bool: True if the pid is present, False otherwise.
        """
        for container in self._applications:
            if container.pid == pid:
                return True
        return False

    def _add_application(self, application: Any) -> int:
        """
        Register a FlaUI Application instance in the module's internal list.

        Converts and stores the application's process id and name in an ApplicationContainer.

        Args:
            application (Any): FlaUI Application instance with ProcessId and Name attributes.

        Returns:
            int: The process id of the added (or existing) application.

        Raises:
            FlaUiError: If the application information cannot be retrieved or is invalid.
        """
        try:
            pid = int(application.ProcessId)
            name = str(application.Name)

            if not self._exists_pid(pid):
                self._applications.append(self.ApplicationContainer(pid=pid,
                                                                    name=name,
                                                                    application=application))

            return pid

        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None

    @staticmethod
    def _flaui_launch_application(application: str, arguments: Optional[str] = None) -> Any:
        """
        Launch an application via FlaUI, optionally with command-line arguments.

        Args:
            application (str): Path or name of the application to launch.
            arguments (Optional[str]): Optional command-line arguments.

        Returns:
            Any: FlaUI Application object for the launched process.

        Raises:
            Win32Exception: If the launch fails due to system errors (e.g. executable not found).
        """
        if arguments is not None:
            return FlaUI.Core.Application.Launch(application, arguments)

        return FlaUI.Core.Application.Launch(application)

    @staticmethod
    def _flaui_attach_application_by_pid(pid: int) -> Any:
        """
        Attach to a running application by process id (PID) using FlaUI.

        Args:
            pid (int): Process id to attach to.

        Returns:
            Any: FlaUI Application object when attachment succeeds.

        Raises:
            FlaUiError: When the attachment fails because the PID does not correspond to a running application.
        """
        try:
            return FlaUI.Core.Application.Attach(pid)
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationPidNotFound.format(pid)) from None

    @staticmethod
    def _flaui_attach_application_by_name(name: str) -> Any:
        """
        Attach to a running application by its process or executable name using FlaUI.

        Args:
            name (str): Process or executable name to attach to.

        Returns:
            Any: FlaUI Application object when attachment succeeds.

        Raises:
            FlaUiError: When the attachment fails because no matching application was found.
        """
        try:
            return FlaUI.Core.Application.Attach(name)
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationNameNotFound.format(name)) from None
