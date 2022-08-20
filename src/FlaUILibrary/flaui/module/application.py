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

    class ApplicationContainer:
        """
        Application container to handle an attached or launched process.
        """
        pid: Optional[int]
        application: Optional[str]

        def __init__(self, pid: int, application: Any):
            """
            Application container class to store applications.

            Args:
                pid (int): Process id from process
                application (Object) : Application object to store.
            """
            self.pid = pid
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

    def __init__(self, automation: Any):
        """
        Application module wrapper for FlaUI usage.

        Args:
            automation (Object): UIA3/UIA2 automation object from FlaUI.
        """
        self._applications = []
        self._automation = automation

    @staticmethod
    def create_value_container(name=None, pid=None, args=None, msg=None):
        """
        Helper to create container object.

        Raises:
            FlaUiError: If creation from container object failed by invalid values.

        Args:
            name (String): Name from application
            pid (Number): PID number to attach to process
            args (String): Arguments to use by application
            msg (String): Optional error message
        """
        return Application.Container(name=Converter.cast_to_string(name),
                                     pid=Converter.cast_to_int(pid, msg),
                                     args=Converter.cast_to_string(args))

    def execute_action(self, action: Action, values: Container):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.ATTACH_APPLICATION_BY_NAME
            * Values ["name"] : Name from application to attach
            * Returns : PID from attached process.

          *  Action.ATTACH_APPLICATION_BY_PID
            * Values ["pid"] : PID to attach
            * Returns : PID from attached process.

          *  Action.LAUNCH_APPLICATION
            * Values ["name"] : Process name to launch
            * Returns : PID from started process.

          *  Action.LAUNCH_APPLICATION_WITH_ARGS
            * Values ["name", "args"] : Process name to start for example outlook.exe
                                        Additional arguments for process for example outlook.exe Hello World
            * Returns : PID from started process.

          *  Action.EXIT_APPLICATION
            * Values  : ["id"] : PID from process attached or launched process to stop.
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action: Action to use.
            values: See supported action definitions for value usage and value container definition.
        """

        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.ATTACH_APPLICATION_BY_NAME: lambda: self._attach_application_by_name(values["name"]),
            self.Action.ATTACH_APPLICATION_BY_PID: lambda: self._attach_application_by_pid(values["pid"]),
            self.Action.LAUNCH_APPLICATION: lambda: self._launch_application(values["name"]),
            self.Action.LAUNCH_APPLICATION_WITH_ARGS: lambda: self._launch_application_with_args(values["name"],
                                                                                                 values["args"]),
            self.Action.EXIT_APPLICATION: lambda: self._exit_application(values["pid"])
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
            return self._insert_application(FlaUI.Core.Application.Attach(name))
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
            return self._insert_application(FlaUI.Core.Application.Attach(pid))
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
            return self._insert_application(FlaUI.Core.Application.Launch(application))
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
            return self._insert_application(FlaUI.Core.Application.Launch(application, arguments))
        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None

    def _exit_application(self, pid):
        """
        Try to close application and detach from window if not an FlaUiError will be thrown.

        Raises:
            FlaUiError: If no application is attached.
        """
        container = self._get_application(pid)
        container.application.Kill()
        self._applications.remove(container)

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

    def _get_application(self, pid: int):
        """
        Get application element by given pid. If not exists an Application not attached error will be thrown.

        Raises:
            FlaUiError: If no application is attached.
        """
        for container in self._applications:
            if container.pid == pid:
                return container

        raise FlaUiError(FlaUiError.ApplicationNotAttached) from None

    def _insert_application(self, application: Any):
        """
        Set application element by given pid.
        If not exists an Application not found error will be thrown.

        Raises:
            FlaUiError: If no application is attached.
        """
        try:
            pid = application.ProcessId

            if not self._exists_pid(pid):
                self._applications.append(self.ApplicationContainer(pid=pid, application=application))

            return pid

        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None
