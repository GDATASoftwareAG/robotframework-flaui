from enum import Enum
from typing import Optional, Any
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer


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
        GET_CHILDS_FROM_ELEMENT = "DEBUG_GET_CHILDS_FROM_ELEMENT"

    @staticmethod
    def create_value_container(element=None) -> Container:
        """
        Helper to create container object.

        Args:
            element (Object): Any ui element to debug
        """
        return Debug.Container(element=element)

    def execute_action(self, action: Action, values: Container = None) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.GET_CHILDS_FROM_ELEMENT:
                lambda: Debug._get_childs_from_element(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_childs_from_element(container: Container) -> str:
        """
        Return a trace string for the given element and its direct children.

        The returned string starts with the element's string representation
        followed by one line per direct child prefixed with \"------> \".

        Args:
            container (Debug.Container): Container holding:
                - container['element']: Automation element to inspect.

        Returns:
            str: Multi-line trace with the element and its direct children.

        Raises:
            FlaUiError: If the required element is missing or not usable.
        """
        element = container["element"]
        element_string = element.ToString() + "\n"

        for children in element.FindAllChildren():
            element_string += "------> " + children.ToString() + "\n"

        return element_string
