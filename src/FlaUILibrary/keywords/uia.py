from robotlibcore import keyword
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class UiaKeywords:
    """
    Interface implementation from robotframework usage for user interface automation keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for mouse keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def switch_uia_to(self, uia):
        """
        Switch automation user interface from library.

        Possible arguments are 'UIA2' or 'UIA3'.

        All other interface usage will force a Rush Exception.

        Arguments:
        | Argument   | Type   | Description                             |
        | uia        | string | 'UIA2' or 'UIA3'                        |

        Example:
        | Switch UIA To  UIA2           |
        | Switch UIA To  UIA3           |

        """
        if uia == "UIA2" or uia == "UIA3":
            self._container.set_identifier(uia)
            return

        raise FlaUiError(FlaUiError.ActionNotSupported) from None

