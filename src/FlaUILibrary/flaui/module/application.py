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

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        ATTACH_APPLICATION_BY_NAME = "ATTACH_APPLICATION_BY_NAME"
        ATTACH_APPLICATION_BY_PID = "ATTACH_APPLICATION_BY_PID"
        LAUNCH_APPLICATION = "LAUNCH_APPLICATION"
        LAUNCH_APPLICATION_WITH_ARGS = "LAUNCH_APPLICATION_WITH_ARGS"
        EXIT_APPLICATION = "EXIT_APPLICATION"
        GET_MAIN_WINDOW_FROM_APPLICATION = "GET_MAIN_WINDOW_FROM_APPLICATION"

    def __init__(self, automation: Any):
        """
        Application module wrapper for FlaUI usage.

        Args:
            automation (Object): UIA3/UIA2 automation object from FlaUI.
        """
        self._application = None
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
            * Returns : None

          *  Action.ATTACH_APPLICATION_BY_PID
            * Values ["pid"] : PID value to attach
            * Returns : None

          *  Action.LAUNCH_APPLICATION
            * Values ["name"] : Process name to launch
            * Returns : PID from launched process.

          *  Action.LAUNCH_APPLICATION_WITH_ARGS
            * Values ["name", "args"] : Process name to start for example outlook.exe
                                        Additional arguments for process for example outlook.exe Hello World
            * Returns : PID from launched process.

          *  Action.EXIT_APPLICATION
            * Values  : None
            * Returns : None

          *  Action.GET_MAIN_WINDOW_FROM_APPLICATION
            * Values  : None
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
            self.Action.EXIT_APPLICATION: lambda: self._exit_application(),
            self.Action.GET_MAIN_WINDOW_FROM_APPLICATION: lambda: self._get_main_window_from_application()
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _attach_application_by_name(self, name: str):
        """
        Attach to application by name.

        Args:
            name: Name from application to attach.

        Raises:
            FlaUiError: If application with name not exist.
        """
        try:
            self._application = FlaUI.Core.Application.Attach(name)
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationNameNotFound.format(name)) from None

    def _attach_application_by_pid(self, pid: int):
        """
        Attach to an running application by pid.

        Args:
            pid: PID number from process to attach.

        Raises:
            FlaUiError: If application with pid number not exist.
        """
        try:
            self._application = FlaUI.Core.Application.Attach(pid)
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationPidNotFound.format(pid)) from None

    def _launch_application(self, application: str):
        """
        Launch an application.

        Args:
            application: Name from application to start for example outlook.

        Raises:
            FlaUiError: If application could not be found.

        Return:
            Process id from launched application if successfully
        """
        try:
            self._application = FlaUI.Core.Application.Launch(application)
            return self._application.ProcessId
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
            self._application = FlaUI.Core.Application.Launch(application, arguments)
            return self._application.ProcessId
        except Win32Exception:
            raise FlaUiError(FlaUiError.ApplicationNotFound.format(application)) from None

    def _get_main_window_from_application(self):
        """
        Stores main window from attached application.

        Raises:
            FlaUiError: If no application is attached.
        """
        try:
            window = self._application.GetMainWindow(self._automation)

            if window is None:
                raise FlaUiError(FlaUiError.NoElementAttached)

            return window

        except AttributeError:
            raise FlaUiError(FlaUiError.ApplicationNotAttached) from None

    def _exit_application(self):
        """
        Try to close application and detach from window if not an FlaUiError will be thrown.

        Raises:
            FlaUiError: If no application is attached.
        """
        try:
            self._application.Kill()
            self._application = None
        except AttributeError:
            raise FlaUiError(FlaUiError.ApplicationNotAttached) from None
