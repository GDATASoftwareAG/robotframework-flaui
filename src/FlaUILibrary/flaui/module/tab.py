from enum import Enum
from typing import Optional, Any, List
from System import Exception as CSharpException  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.exception.flauierror import FlaUiError


class Tab(ModuleInterface):
    """
    Tab module wrapper for FlaUI usage.
    Wrapper module executes methods from Tab.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from tab module.
        """
        element: Optional[Any]
        name: Optional[str]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        GET_TAB_ITEMS_NAMES = "TAB_GET_ITEMS_NAMES"
        SELECT_TAB_ITEM_BY_NAME = "TAB_SELECT_TAB_ITEM_BY_NAME"

    @staticmethod
    def create_value_container(element=None, name=None) -> Container:
        """
        Helper to create container object.

        Args:
            element (Object): Tab element to use
            name (String): Name from tab item to search
        """
        return Tab.Container(element=element,
                             name=Converter.cast_to_string(name))

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        switcher = {
            self.Action.GET_TAB_ITEMS_NAMES: lambda: self._get_tab_items_names(values),
            self.Action.SELECT_TAB_ITEM_BY_NAME: lambda: self._select_tab_item(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _get_tab_items_names(container: Container) -> List[str]:
        """
        Return the display names of all TabItem children of the given Tab element.

        Args:
            container (Tab.Container): Container holding:
                - container['element']: FlaUI Tab control instance.

        Returns:
            List[str]: Names of all visible TabItem children. Returns an empty list if none exist.

        Raises:
            FlaUiError: If the provided container does not contain a valid Tab element
                or if retrieving the TabItems collection fails.
        """
        element = container["element"]

        child_tab_items_names = []

        for tab_items in element.TabItems:
            child_tab_items_names.append(tab_items.Name)

        return child_tab_items_names

    @staticmethod
    def _select_tab_item(container: Container) -> None:
        """
        Select the tab item with the specified display name on the given Tab element.

        Args:
            container (Tab.Container): Container holding:
                - container['element']: FlaUI Tab control instance.
                - container['name']: Display name of the TabItem to select.

        Raises:
            FlaUiError: If the named TabItem cannot be selected, or if an underlying
                CSharpException is raised during selection. The original exception
                message is included in the raised FlaUiError.
        """
        try:
            element = container["element"]
            name = container["name"]

            element.SelectTabItem(name)
        except CSharpException as exception:
            raise FlaUiError(FlaUiError.GenericError.format(exception.Message)) from None
