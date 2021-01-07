from enum import Enum
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.interface import ModuleInterface


class Debug(ModuleInterface):
    """
    Debugging control module wrapper for FlaUI usage.
    Wrapper module executes methods from implementation IAutomationElementFinder interface implemented
    by AutomationElementFind.cs.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        GET_CHILDS_FROM_ELEMENT = "GET_CHILDS_FROM_ELEMENT"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

            * Action.PRINT_ALL_CHILDS
              * Values (Object) : UIA3 element to gain debug output
              * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.GET_CHILDS_FROM_ELEMENT: lambda: Debug._get_childs_from_element(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_childs_from_element(element):
        """Return trace information about element and all childs if exists.
        """

        element_string = element.ToString() + "\n"

        for children in element.FindAllChildren():
            element_string += "------> " + children.ToString() + "\n"

        return element_string
