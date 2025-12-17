from FlaUI.UIA3 import UIA3Automation  # pylint: disable=import-error
from FlaUILibrary.flaui.automation.uia import UIA


class UIA3(UIA):
    """UIA3 window automation module for a centralized communication handling between robot keywords and Flaui. """

    def __init__(self, retry_timeout_in_milliseconds: int):
        """
        Creates UIA3 window automation module.

        Args:
            retry_timeout_in_milliseconds (Number):
              Timeout in milliseconds for automatic retry if element could not be found.
        """
        super().__init__()
        self._uia3 = UIA3Automation()
        super().register_action(self._uia3, retry_timeout_in_milliseconds)  # pylint: disable=maybe-no-member

    def __del__(self):
        """
        Destructor to clean up all C# interfaces
        """
        try:
            # C# --> class UIA3Automation : AutomationBase --> abstract class AutomationBase : IDisposable
            self._uia3.Dispose()
        except TypeError:
            pass

    def identifier(self):
        """
        Returns identifier which windows automation interface is in usage.
        """
        return "UIA3"
