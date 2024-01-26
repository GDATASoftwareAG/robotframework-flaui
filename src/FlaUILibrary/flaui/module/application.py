from enum import Enum
from typing import Optional, Any
import FlaUI.Core  # pylint: disable=import-error
from System.ComponentModel import Win32Exception  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


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
        timeout: Optional[int]

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
        ATTACH_APPLICATION_BY_NAME = "ATTACH_APPLICATION_BY_NAME"
        ATTACH_APPLICATION_BY_PID = "ATTACH_APPLICATION_BY_PID"
        LAUNCH_APPLICATION = "LAUNCH_APPLICATION"
        LAUNCH_APPLICATION_WITH_ARGS = "LAUNCH_APPLICATION_WITH_ARGS"
        EXIT_APPLICATION = "EXIT_APPLICATION"
        CLOSE_APPLICATION_BY_NAME = "CLOSE_APPLICATION_BY_NAME"
        WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_NAME = "WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_NAME"
        WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_PID = "WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_PID"
        WAIT_WHILE_APPLICATION_IS_BUSY_BY_NAME = "WAIT_WHILE_APPLICATION_IS_BUSY_BY_NAME"
        WAIT_WHILE_APPLICATION_IS_BUSY_BY_PID = "WAIT_WHILE_APPLICATION_IS_BUSY_BY_PID"

    def __init__(self):
        """
        Application module wrapper for FlaUI usage.
        """
        self._applications = []

    @staticmethod
    def create_value_container(name=None, pid=None, timeout=None, args=None, msg=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            name (String): Name from application
            pid (Number): PID number to attach to process
            timeout (Number) : Timeout to wait for Handle or Application
            args (String): Arguments to use by application
            msg (String): Optional error message
        """
        return Application.Container(name=Converter.cast_to_string(name),
                                     pid=Converter.cast_to_int(pid, msg),
                                     timeout=Converter.cast_to_int(timeout, msg),
                                     args=Converter.cast_to_string(args))

    def execute_action(self, action: Action, values: Container):
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
                lambda: self._attach_application_by_name(values["name"]),
            self.Action.ATTACH_APPLICATION_BY_PID:
                lambda: self._attach_application_by_pid(values["pid"]),
            self.Action.LAUNCH_APPLICATION:
                lambda: self._launch_application(values["name"]),
            self.Action.LAUNCH_APPLICATION_WITH_ARGS:
                lambda: self._launch_application_with_args(values["name"], values["args"]),
            self.Action.EXIT_APPLICATION:
                lambda: self._exit_application(values["pid"]),
            self.Action.CLOSE_APPLICATION_BY_NAME:
                lambda: self._close_application_by_name(values["name"]),
            self.Action.WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_PID:
                lambda: self._wait_while_main_handle_is_missing_by_pid(values["pid"], values["timeout"]),
            self.Action.WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_NAME:
                lambda: self._wait_while_main_handle_is_missing_by_name(values["name"], values["timeout"]),
            self.Action.WAIT_WHILE_APPLICATION_IS_BUSY_BY_NAME:
                lambda: self._wait_while_busy_by_name(values["name"], values["timeout"]),
            self.Action.WAIT_WHILE_APPLICATION_IS_BUSY_BY_PID:
                lambda: self._wait_while_busy_by_pid(values["pid"], values["timeout"]),
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _attach_application_by_name(self, name: str):
        """
        Attach to application by name.

        Args:
            name: Name from application to attach.

        Raises:
            FlaUiError: If application with name not exist.

        Returns:
            Index from attached application
        """
        try:
            return self._add_application(FlaUI.Core.Application.Attach(name))
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationNameNotFound.format(name)) from None

    def _attach_application_by_pid(self, pid: int):
        """
        Attach to a running application by pid.

        Args:
            pid: Number from process to attach.

        Raises:
            FlaUiError: If application with pid number not exist.

        Returns:
            Index from attached application
        """
        try:
            return self._add_application(self._get_application_by_pid(pid))
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationPidNotFound.format(pid)) from None

    def _launch_application(self, application: str):
        """
        Launch an application.

        Args:
            application: Name from application to start for example outlook.

        Raises:
            FlaUiError: If application could not be found.

        Returns:
            Index from started application
        """
        try:
            return self._add_application(FlaUI.Core.Application.Launch(application))
        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None

    def _launch_application_with_args(self, application: str, arguments: str):
        """
        Launch an application with given arguments.

        Args:
            application: Name from application to start for example outlook.
            arguments: Arguments to launch application.

        Raises:
            FlaUiError: If application could not be found.

        Return:
            Process id from launched application if successfully
        """
        try:
            return self._add_application(FlaUI.Core.Application.Launch(application, arguments))
        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None

    def _exit_application(self, pid):
        """
        Try to close application and detach from window if not an FlaUiError will be thrown.

        Raises:
            FlaUiError: If no application is attached.
        """
        container = self._get_attached_application_by_pid(pid)
        container.application.Kill()
        self._applications.remove(container)

    def _close_application_by_name(self, name):
        pid = self._attach_application_by_name(name)
        self._exit_application(pid)

    def _exists_pid(self, pid):
        """
        Checks if given pid exists in applications list.

        Returns:
            True if PID exists in applications otherwise False
        """
        for container in self._applications:
            if container.pid == pid:
                return True
        return False

    def _get_attached_application_by_pid(self, pid: int):
        """
        Get application element by pid.

        Raises:
            FlaUiError: If no application is attached.
        """
        for container in self._applications:
            if container.pid == pid:
                return container

        raise FlaUiError(FlaUiError.ApplicationNotAttached) from None

    def _add_application(self, application: Any):
        """
        Add application element from pid.

        Raises:
            FlaUiError: If no application is attached.
        """
        try:
            pid = application.ProcessId
            name = application.Name

            if not self._exists_pid(pid):
                self._applications.append(self.ApplicationContainer(pid=pid,
                                                                    name=name,
                                                                    application=application))

            return pid

        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None

    def _wait_while_main_handle_is_missing_by_pid(self, pid: int, timeout: Optional[int]):
        """
        Waits until the main handle is set.

        If timeout is not set. Timeout is INFINITY.

        Raises:
            FlaUiError: If no application could be found by name.

        Returns:
            True a main window handle was found, false otherwise.
        """
        application = self._get_application_by_pid(pid)
        return application.WaitWhileMainHandleIsMissing(Converter.cast_to_timespan(timeout))

    def _wait_while_main_handle_is_missing_by_name(self, name: str, timeout: Optional[int]):
        """
        Waits until the main handle is set.

        If timeout is not set. Timeout is INFINITY.

        Raises:
            FlaUiError: If no application could be found by name.

        Returns:
            True a main window handle was found, false otherwise.
        """
        application = self._get_application_by_name(name)
        return application.WaitWhileMainHandleIsMissing(Converter.cast_to_timespan(timeout))

    def _wait_while_busy_by_pid(self, pid: int, timeout: Optional[int]):
        """
        Waits as long as the application is busy.

        If timeout is not set. Timeout is INFINITY.

        Raises:
            FlaUiError: If no application could be found by pid.

        Returns:
            True if the application is idle, false otherwise.
        """
        application = self._get_application_by_pid(pid)
        return application.WaitWhileBusy(Converter.cast_to_timespan(timeout))

    def _wait_while_busy_by_name(self, name: str, timeout: Optional[int]):
        """
        Waits as long as the application is busy.

        If timeout is not set. Timeout is INFINITY.

        Raises:
            FlaUiError: If no application could be found by name.

        Returns:
            True if the application is idle, false otherwise.
        """
        application = self._get_application_by_name(name)
        return application.WaitWhileBusy(Converter.cast_to_timespan(timeout))

    @staticmethod
    def _get_application_by_pid(pid: int):
        """
        Get application element by pid.

        Raises:
            FlaUiError: If no application could be found by pid.
        """
        try:
            return FlaUI.Core.Application.Attach(pid)
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationPidNotFound.format(pid)) from None

    @staticmethod
    def _get_application_by_name(name: str):
        """
        Get application element by name.

        Raises:
            FlaUiError: If no application could be found from name.
        """
        try:
            return FlaUI.Core.Application.Attach(name)
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationNameNotFound.format(name)) from None
