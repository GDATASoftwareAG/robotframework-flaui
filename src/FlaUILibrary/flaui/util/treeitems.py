from typing import Any
from System import InvalidOperationException  # pylint: disable=import-error
from FlaUI.Core.Definitions import ExpandCollapseState  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.enum.treeitemaction import TreeItemAction
from FlaUILibrary.flaui.util.treeitemsparser import TreeItemsParser


class TreeItems:
    """
    A helper class for tree control.
    """

    @staticmethod
    def get_visible_leaf_count(nodes: Any):
        """
        Get count from all visible nodes which are visible.

        Args:
            nodes (Object): TreeItems[] from current node

        Returns:
            Count from all visible nodes
        """
        node_count = nodes.Length
        for node in nodes:
            if node.ExpandCollapseState in (ExpandCollapseState.Expanded, ExpandCollapseState.PartiallyExpanded):
                node_count += TreeItems.get_visible_leaf_count(node.Items)

        return node_count

    @staticmethod
    def expand_all_tree_nodes(nodes: Any):
        """
        Expand all tree nodes.

        Args:
            nodes (Object): TreeItems[] from current node
        """
        for node in nodes:
            if node.ExpandCollapseState in (ExpandCollapseState.Expanded, ExpandCollapseState.Collapsed):
                node.Expand()
                TreeItems.expand_all_tree_nodes(node.Items)

    @staticmethod
    def collapse(nodes: Any):
        """
        Collapses every collapsable tree item in root level.

        Args:
            nodes (Object): TreeItems[] from current node
        """
        for node in nodes:
            if node.ExpandCollapseState in (ExpandCollapseState.Expanded, ExpandCollapseState.PartiallyExpanded):
                node.Collapse()

    @staticmethod
    def get_all_names_from_tree_nodes(nodes: Any):
        """
        Get all names from all visible nodes.

        Args:
            nodes (Object): TreeItems[] from current node

        Returns:
            List from all node names.
        """
        names = []

        for node in nodes:
            names.append(node.Name)
            if node.ExpandCollapseState in (ExpandCollapseState.Expanded, ExpandCollapseState.PartiallyExpanded):
                names.extend(TreeItems.get_all_names_from_tree_nodes(node.Items))

        return names

    @staticmethod
    def select_visible_node_by_name(nodes: Any, name: str):
        """
        Selects a tree item with the given name in tree

        Args:
            nodes (Object): TreeItems[] from current node
            name (String): Name to search on node.

        Raises:
            FlaUiError: If node by a given name could not be found.
        """
        if not TreeItems._find_visible_node_by_name(nodes, name):
            raise FlaUiError(FlaUiError.ElementNameNotFound.format(name))

    @staticmethod
    def execute_by_location(nodes: Any, location: str, seperator: str, action: TreeItemAction):
        """
        Executes the given TreeItemAction to the last element from a tree location.

        Args:
            nodes (Object): TreeItems[] from current node
            location (String): Location string to execute operations on nodes.
            seperator (String): Seperator to split up tree items
            action (TreeItemAction) : Action to operate on node.

        Raises:
            FlaUiError: If action is not supported.
            FlaUiError: If location syntax is wrong.
            FlaUiError: If node is not expandable.
        """
        parser = TreeItemsParser(location, seperator)
        current_nodes = nodes

        for index in range(len(parser.location)):
            node = parser.get_treeitem(current_nodes, index)
            if parser.is_last_element(index):
                try:
                    if action == TreeItemAction.EXPAND:
                        node.Expand()
                    elif action == TreeItemAction.COLLAPSE:
                        node.Collapse()
                    elif action == TreeItemAction.SELECT:
                        node.Select()
                except ValueError:
                    raise FlaUiError(FlaUiError.FalseSyntax.format(
                        "self.current_treeitem." + action.value + "()")) from None
                except InvalidOperationException:
                    raise FlaUiError(FlaUiError.ElementNotExpandable.format(node.Name)) from None
                except Exception:
                    raise FlaUiError(FlaUiError.FalseSyntax.format(
                        "self.current_treeitem." + action.value + "()")) from None
            else:
                if node.ExpandCollapseState == ExpandCollapseState.LeafNode:
                    raise FlaUiError(FlaUiError.ElementNotExpandable.format(node.Name))
                node.Expand()
                current_nodes = node.Items

    @staticmethod
    def _find_visible_node_by_name(nodes: Any, name: str):
        """
        Finds if a node is visible by a given name.

        Args:
            nodes (Object): TreeItems[] from current node
            name (String): Name from node to search.

        Returns:
            True if name was found on any visible node level otherwise False.
        """
        for node in nodes:
            if node.Name == name:
                node.Select()
                return True

            if node.ExpandCollapseState in (ExpandCollapseState.Expanded, ExpandCollapseState.PartiallyExpanded):
                if TreeItems._find_visible_node_by_name(node.Items, name):
                    return True

        return False
