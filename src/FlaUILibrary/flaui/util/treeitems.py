from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.util.treeitemsparser import TreeItemsParser


class TreeItems:
    """
    A helper class for Tree control.
    Every tree consist of tree items or nodes this class represesents those sub items of tree control.
    """
    def __init__(self,control):
        self.control = control
        self.treeitems = control.Items
        self.current_treeitem = None
        self.selected_treeitem = self.control.SelectedTreeItem
        self.treeitems_name = []
        self.treeitems_count = 0
        self.location = []

    def get_every_visible_treeitems_name(self):
        """This function reterns a list of  every visible node in tree.
        It iterates the given tree and adds the names of the tree items to self.treeitems_name
        and the total count of them to self.treeitems_count
        """
        for item in self.treeitems:
            state = item.ExpandCollapseState
            self.current_treeitem = item
            self.treeitems_name.append(self.current_treeitem.Name)
            self.treeitems_count +=1

            #The element is Expanded All children are visible.
            if state == 1:
                self.treeitems = item.Items
                self.get_every_visible_treeitems_name()
            #The element is PartiallyExpanded Some, but not all, children are visible..
            elif state == 2:
                self.treeitems = item.Items
                self.get_every_visible_treeitems_name()
            #The element is LeafNode does not expand or collapse.
            elif state == 3:
                continue
            #The element is Collapsed No children are visible.
            elif state == 0:
                continue
        return self.treeitems_name

    def select_visible_treeitem_by_name(self, name):
        """This function selects a tree item with the given name in tree
        if item not found a flauierror will be thrown.
        """
        for item in self.treeitems:
            state = item.ExpandCollapseState
            self.current_treeitem = item
            if self.current_treeitem.Name == name:
                self.current_treeitem.Select()
                self.treeitems_name.append(self.current_treeitem.Name)
            #The element is Expanded All children are visible.
            if state == 1:
                self.treeitems = item.Items
                self.select_visible_treeitem_by_name(name)
            #The element is PartiallyExpanded Some, but not all, children are visible..
            elif state == 2:
                self.treeitems = item.Items
                self.select_visible_treeitem_by_name(name)
            #The element is Collapsed No children are visible.
            elif state == 0:
                continue
            #The element is LeafNode does not expand or collapse.
            elif state == 3:
                continue
        if not self.treeitems_name:
            raise FlaUiError(FlaUiError.ElementNameNotFound.format(name))
        return True

    def expand_all_treeitems(self):
        """This function expands every expandable tree item in tree
        """
        for item in self.treeitems:
            state = item.ExpandCollapseState
            self.current_treeitem = item
            #The element is PartiallyExpanded Some, but not all, children are visible..
            if state == 2:
                self.current_treeitem.Expand()
                self.treeitems = item.Items
                self.expand_all_treeitems()
            #The element is Collapsed No children are visible.
            elif state == 0:
                self.current_treeitem.Expand()
                self.treeitems = item.Items
                self.expand_all_treeitems()
            #The element is LeafNode does not expand or collapse.
            elif state == 3:
                continue
            #The element is Expanded All children are visible.
            elif state == 1:
                continue
        return True

    def execute_by_location(self, location , exec_func):
        """This function executes the given exec_func function to the last element in location
        after iterating the whole location through.
        The given location will be parsed with the help of TreeItemsParser
        """
        parser = TreeItemsParser(location)
        for index in range(len(parser.location)):
            self.current_treeitem = parser.get_treeitem(self.treeitems, index)
            if parser.is_last_element(index):
                function = "self.current_treeitem." + exec_func + "()"
                try:
                    # proved if the exec_func string is valid
                    if exec_func == "Expand":
                        self.current_treeitem.Expand()
                    elif exec_func == "Collapse":
                        self.current_treeitem.Collapse()
                    elif exec_func == "Select":
                        self.current_treeitem.Select()
                except ValueError as ex:
                    raise FlaUiError(FlaUiError.FalseSyntax.format(function)) from None
                except Exception as ex:
                    if ex.__class__.__name__=="InvalidOperationException":
                        raise FlaUiError(FlaUiError.ElementNotExpandable.format(self.current_treeitem.Name)) from None
                    raise FlaUiError(FlaUiError.FalseSyntax.format(function)) from None
            else:
                if self.current_treeitem.ExpandCollapseState == 3:
                    raise FlaUiError(FlaUiError.ElementNotExpandable.format(self.current_treeitem.Name))
                self.current_treeitem.Expand()
                self.treeitems = self.current_treeitem.Items

    def collapse(self):
        """This function collapses every collapsable tree item in root level.
        """
        for item in self.treeitems:
            if item.ExpandCollapseState == 1 or item.ExpandCollapseState == 2:
                item.Collapse()
