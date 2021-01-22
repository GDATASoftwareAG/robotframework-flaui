from FlaUI.UIA3 import UIA3Automation  # pylint: disable=import-error
from FlaUILibrary.flaui.uia import UIA


class UIA3(UIA):
    """UIA3 window automation module for a centralized communication handling between robot keywords and flaui. """

    def __init__(self):
        """Creates UIA3 window automation module. """
        super().__init__()
        self._automation = UIA3Automation()
        super().register_action(self._automation)  # pylint: disable=maybe-no-member

    def __del__(self):
        """Destructor to cleanup all C# interfaces"""

        # C# --> class UIA3Automation : AutomationBase --> abstract class AutomationBase : IDisposable
        self._automation.Dispose()

    def identifier(self):
        """ Returns identifier which windows automation interface is in usage."""
        return "UIA3"
