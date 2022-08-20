from FlaUI.UIA2 import UIA2Automation  # pylint: disable=import-error
from FlaUILibrary.flaui.automation.uia import UIA


class UIA2(UIA):
    """UIA2 window automation module for a centralized communication handling between robot keywords and Flaui. """

    def __init__(self, timeout=1000):
        """
        Creates UIA2 window automation module.
        ``timeout`` is the default waiting value to repeat element find action. Default value is 1000ms.
        """
        super().__init__(timeout)
        self._uia2 = UIA2Automation()
        super().register_action(self._uia2)  # pylint: disable=maybe-no-member

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
