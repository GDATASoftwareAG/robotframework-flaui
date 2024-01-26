from abc import ABC
from typing import Any
from enum import Enum
from FlaUI.Core.AutomationElements import AutomationElementExtensions  # pylint: disable=import-error
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.interface import (WindowsAutomationInterface, ValueContainer)
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.module import (Application, Combobox, Debug, Grid, Tree, Mouse, Keyboard, Textbox, Tab,
                                       Element, Window, Checkbox, Selector, Property, ToggleButton)


class UIA(WindowsAutomationInterface, ABC):
    """
    Generic window automation module for a centralized communication handling between robot keywords.
    """

    def __init__(self, timeout=1000):
        """
        Creates default UIA window automation module.
        ``timeout`` is the default waiting value to repeat element find action. Default value is 1000ms.
        """
        self._actions = {}
        self._timeout = timeout

    def action(self, action: Enum, values: ValueContainer = None, msg: str = None):
        """
        Performs an application action if supported. If not supported an NotSupported error will be thrown.

        Args:
            action (Action) : Application action to perform.
            values (Array)  : Specified argument values for action.
                              See action declaration from specific module for value attributes.
            msg    (String) : Optional custom error message.

        Raises:
            FlaUiError: If execute action throws a Flaui error.
            FlaUiError: If action is not supported.
        """
        try:
            if action in self._actions:
                return self._actions[action].execute_action(action, values)

            raise FlaUiError(FlaUiError.ActionNotSupported)

        except FlaUiError as error:
            raise FlaUiError(msg) if msg is not None else error

    def register_action(self, automation: Any):
        """
        Register all supported core actions.

        Args:
            automation (Object)       : Windows user automation object.
        """
        modules = [Application(), Debug(), Element(automation, self._timeout), Keyboard(), Selector(),
                   Grid(), Mouse(automation), Textbox(), Tree(), Checkbox(), Tab(), Window(), Combobox(),
                   Property(), ToggleButton()]

        for module in modules:
            for value in module.Action:
                self._actions[value] = module

    def get_element(self, identifier: str, ui_type: InterfaceType = None, msg: str = None):
        """
        Get element from identifier.

        Args:
            identifier (String): XPath identifier to find element
            ui_type (Enum)     : Object enum to cast element
            msg (String)       : Custom error message
        """
        element = self.action(Element.Action.GET_ELEMENT,
                              Element.Container(xpath=identifier, retries=None, name=None),
                              msg)

        if not ui_type:
            return element

        return self.cast_element_to_type(element, ui_type)

    @staticmethod
    def cast_element_to_type(element: Any, ui_type: InterfaceType):
        """
        Cast element to given type.

        ``element`` Element to capture if not set 'None' desktop will be captured.
        ``ui_type`` InterfaceType to cast to specific module element.
        """

        switcher = {
            InterfaceType.TEXTBOX: {"cast": lambda: AutomationElementExtensions.AsTextBox(element),
                                    "type": "Textbox"},
            InterfaceType.CHECKBOX: {"cast": lambda: AutomationElementExtensions.AsCheckBox(element),
                                     "type": "Checkbox"},
            InterfaceType.COMBOBOX: {"cast": lambda: AutomationElementExtensions.AsComboBox(element),
                                     "type": "Combobox"},
            InterfaceType.WINDOW: {"cast": lambda: AutomationElementExtensions.AsWindow(element),
                                   "type": "Window"},
            InterfaceType.LISTVIEW: {"cast": lambda: AutomationElementExtensions.AsGrid(element),
                                     "type": "Grid"},
            InterfaceType.RADIOBUTTON: {"cast": lambda: AutomationElementExtensions.AsRadioButton(element),
                                        "type": "Radiobutton"},
            InterfaceType.LISTBOX: {"cast": lambda: AutomationElementExtensions.AsListBox(element),
                                    "type": "Listbox"},
            InterfaceType.TAB: {"cast": lambda: AutomationElementExtensions.AsTab(element),
                                "type": "Tab"},
            InterfaceType.TREE: {"cast": lambda: AutomationElementExtensions.AsTree(element),
                                 "type": "Tree"},
            InterfaceType.TOGGLEBUTTON: {"cast": lambda: AutomationElementExtensions.AsToggleButton(element),
                                         "type": "ToggleButton"},
        }

        dic = switcher.get(ui_type, {"cast": lambda: InterfaceType.INVALID, "type": "Unknown"})

        # FlaUI don't verify if element type is cast able to this type of element
        ui_object = dic["cast"]()

        if ui_object == InterfaceType.INVALID:
            raise FlaUiError(FlaUiError.WrongElementType.format(element.Properties.ControlType, dic["type"]))

        return ui_object
