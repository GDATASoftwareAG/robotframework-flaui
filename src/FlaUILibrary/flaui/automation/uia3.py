from FlaUI.UIA3 import UIA3Automation  # pylint: disable=import-error
from FlaUILibrary.flaui.automation.uia import UIA


class UIA3(UIA):
    """UIA3 window automation module for a centralized communication handling between robot keywords and Flaui. """

    def __init__(self, timeout=1000):
        """
        Creates UIA3 window automation module.
        ``timeout`` is the default waiting value to repeat element find action. Default value is 1000ms.
        """
        super().__init__(timeout)
        self._uia3 = UIA3Automation()
        super().register_action(self._uia3)  # pylint: disable=maybe-no-member

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
