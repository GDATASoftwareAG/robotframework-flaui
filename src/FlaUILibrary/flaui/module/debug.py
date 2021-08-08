from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)


class Debug(ModuleInterface):
    """
    Debugging control module wrapper for FlaUI usage.
    Wrapper module executes methods from implementation IAutomationElementFinder interface implemented
    by AutomationElementFind.cs.
    """

    class Container(ValueContainer):
        """
        Value container from debug module.
        """
        element: Optional[Any]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        GET_CHILDS_FROM_ELEMENT = "GET_CHILDS_FROM_ELEMENT"

    @staticmethod
    def create_value_container(element=None):
        """
        Helper to create container object.

        Args:
            element (Object): Any ui element to debug
        """
        return Debug.Container(element=element)

    def execute_action(self, action: Action, values: Container = None):
        """
        If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

            * Action.PRINT_ALL_CHILDS
              * Values ["element"]
              * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.GET_CHILDS_FROM_ELEMENT: lambda: Debug._get_childs_from_element(values["element"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_childs_from_element(element: Any):
        """
        Return trace information about element and all childs.
        """

        element_string = element.ToString() + "\n"

        for children in element.FindAllChildren():
            element_string += "------> " + children.ToString() + "\n"

        return element_string
