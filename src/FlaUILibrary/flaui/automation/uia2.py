from FlaUI.UIA2 import UIA2Automation  # pylint: disable=import-error
from FlaUILibrary.flaui.automation.uia import UIA


class UIA2(UIA):
    """UIA2 window automation module for a centralized communication handling between robot keywords and Flaui. """

    def __init__(self, retry_timeout_in_milliseconds: int):
        """
        Creates UIA2 window automation module.

        Args:
            retry_timeout_in_milliseconds (Number):
              Timeout in milliseconds for automatic retry if element could not be found.
        """
        super().__init__()
        self._uia2 = UIA2Automation()
        super().register_action(self._uia2, retry_timeout_in_milliseconds)  # pylint: disable=maybe-no-member

    def __del__(self):
        """
        Destructor to clean up all C# interfaces
        """
        try:
            # C# --> class UIA2Automation : AutomationBase --> abstract class AutomationBase : IDisposable
            self._uia2.Dispose()
        except TypeError:
            pass

    def identifier(self):
        """
        Returns identifier which windows automation interface is in usage.
        """
        return "UIA2"
