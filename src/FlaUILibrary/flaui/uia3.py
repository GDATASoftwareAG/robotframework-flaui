from FlaUILibrary.flaui.util import InterfaceType
from FlaUILibrary.flaui.interface import WindowsAutomationInterface
from FlaUILibrary.flaui.module import (Application,
                                       Debug,
                                       ListView,
                                       ToggleButton,
                                       ListControl,
                                       Mouse,
                                       Keyboard,
                                       Textbox,
                                       Tab,
                                       Element,
                                       Window)
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUI.UIA3 import UIA3Automation
from FlaUI.Core.AutomationElements import AutomationElementExtensions


class UIA3(WindowsAutomationInterface):

    def __init__(self):
        """Creates UIA3 module from FlaUI to interact with C# Framework."""
        self._automation = UIA3Automation()

        self._modules = [Application(self._automation), Debug(), Element(self._automation), Keyboard(), ListControl(),
                         ListView(), Mouse(), Textbox(), ToggleButton(), Tab(), Window(self._automation)]

        self._actions = {}

        for module in self._modules:
            for value in module.Action:
                self._actions[value] = module

    def __del__(self):
        """Destructor to cleanup all C# interfaces"""

        """ C# --> class UIA3Automation : AutomationBase --> abstract class AutomationBase : IDisposable  """
        self._automation.Dispose()

    def action(self, action, values=None, msg=None):
        """Performs a application action if supported. If not supported an NotSupported FlaUI error will be thrown.

        Args:
            action (Action) : Application action to perform.
            values (Object) : Specified argument values for action. By default if not set is None.
                              See action declaration from specific module for value attributes.
            msg    (String) : Optional custom error message.

        Raises:
            FlaUiError: If execute action throws a flaui error.
            FlaUiError: If action is not supported.
        """
        try:
            if action in self._actions:
                return self._actions[action].execute_action(action, values)

            raise FlaUiError(FlaUiError.ActionNotSupported)

        except FlaUiError as error:
            raise FlaUiError(msg) if msg is not None else error

    @staticmethod
    def cast_element_to_type(element, ui_type):
        """ Cast element to given type.

        ``element`` Element to capture if not set set 'None' desktop will be captured.
        ``ui_type`` InterfaceType to cast to specific module element.
        """

        switcher = {
            InterfaceType.TEXTBOX: {"cast": lambda: AutomationElementExtensions.AsTextBox(element), "type": "Textbox"},
            InterfaceType.CHECKBOX: {"cast": lambda: AutomationElementExtensions.AsCheckBox(element),
                                     "type": "Checkbox"},
            InterfaceType.COMBOBOX: {"cast": lambda: AutomationElementExtensions.AsComboBox(element),
                                     "type": "Combobox"},
            InterfaceType.WINDOW: {"cast": lambda: AutomationElementExtensions.AsWindow(element), "type": "Window"},
            InterfaceType.LISTVIEW: {"cast": lambda: AutomationElementExtensions.AsGrid(element), "type": "Grid"},
            InterfaceType.RADIOBUTTON: {"cast": lambda: AutomationElementExtensions.AsRadioButton(element),
                                        "type": "Radiobutton"},
            InterfaceType.LISTBOX: {"cast": lambda: AutomationElementExtensions.AsListBox(element), "type": "Listbox"},
            InterfaceType.TAB: {"cast": lambda: AutomationElementExtensions.AsTab(element), "type": "Tab"},
        }

        dic = switcher.get(ui_type, {"cast": lambda: InterfaceType.INVALID, "type": "Unknown"})

        # FlaUI don't verify if element type is cast able to this type of element
        ui_object = dic["cast"]()

        if ui_object == InterfaceType.INVALID:
            raise FlaUiError(FlaUiError.WrongElementType.format(element.Properties.ControlType, dic["type"]))

        return ui_object
