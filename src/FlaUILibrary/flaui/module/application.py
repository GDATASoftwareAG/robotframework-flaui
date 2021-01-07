from enum import Enum
import FlaUI.Core  # pylint: disable=import-error
from System.ComponentModel import Win32Exception  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface


class Application(ModuleInterface):
    """
    Application control module wrapper for FlaUI usage.
    Wrapper module executes methods from Application class implementation by Application.cs.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        ATTACH_APPLICATION_BY_NAME = "ATTACH_APPLICATION_BY_NAME"
        ATTACH_APPLICATION_BY_PID = "ATTACH_APPLICATION_BY_PID"
        LAUNCH_APPLICATION = "LAUNCH_APPLICATION"
        EXIT_APPLICATION = "EXIT_APPLICATION"
        GET_MAIN_WINDOW_FROM_APPLICATION = "GET_MAIN_WINDOW_FROM_APPLICATION"

    def __init__(self, automation):
        """Application module wrapper for FlaUI usage.

        Args:
            automation (Object): UIA3 automation object from FlaUI.
        """
        self._application = None
        self._automation = automation

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

          *  Action.ATTACH_APPLICATION_BY_NAME
            * Values (String) : Name from application to attach
            * Returns : None

          *  Action.ATTACH_APPLICATION_BY_PID
            * Values (Number) : PID number from process to attach
            * Returns : None

          *  Action.LAUNCH_APPLICATION
            * Values (String) : Process name to start for example outlook.exe
            * Returns : PID from launched process.

          *  Action.EXIT_APPLICATION
            * Values : None
            * Returns : None

          *  Action.GET_MAIN_WINDOW_FROM_APPLICATION
            * Values : None
            * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        # pylint: disable=unnecessary-lambda
        switcher = {
            self.Action.ATTACH_APPLICATION_BY_NAME: lambda: self._attach_application_by_name(values),
            self.Action.ATTACH_APPLICATION_BY_PID: lambda: self._attach_application_by_pid(values),
            self.Action.LAUNCH_APPLICATION: lambda: self._launch_application(values),
            self.Action.EXIT_APPLICATION: lambda: self._exit_application(),
            self.Action.GET_MAIN_WINDOW_FROM_APPLICATION: lambda: self._get_main_window_from_application()
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    def _attach_application_by_name(self, name):
        """Attach to application by name.

        Args:
            name (string): Name from application to attach.

        Raises:
            FlaUiError: If application with name not exist.
        """
        try:
            self._application = FlaUI.Core.Application.Attach(name)
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationNameNotFound.format(name)) from None

    def _attach_application_by_pid(self, pid):
        """Attach to an running application by pid.

        Args:
            pid (int): PID number from process to attach.

        Raises:
            FlaUiError: If application with pid number not exist.
        """
        try:
            self._application = FlaUI.Core.Application.Attach(int(pid))
        except Exception:
            raise FlaUiError(FlaUiError.ApplicationPidNotFound.format(pid)) from None

    def _launch_application(self, application):
        """Launch an application.

        Args:
            application (string): Name from application to start for example outlook.

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

    def _get_main_window_from_application(self):
        """Stores main window from attached application.

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
        """Try to close application and detach from window if not an FlaUiError will be thrown.

        Raises:
            FlaUiError: If no application is attached.
        """
        try:
            self._application.Kill()
            self._application = None
        except AttributeError:
            raise FlaUiError(FlaUiError.ApplicationNotAttached) from None
