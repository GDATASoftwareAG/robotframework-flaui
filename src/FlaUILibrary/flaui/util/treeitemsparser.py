from typing import Any
from FlaUILibrary.flaui.exception import FlaUiError


class TreeItemsParser:
    """
    Helper class which handles the management of the given location string.
    The location is used to locate the exact tree item in the tree control.
    Examples:
    location = N:Nameofitem1->N:Nameofitem2->N:Nameofitem3
    location = I:indexofitem1->I:indexofitem2->I:indexofitem3
    location = N:Nameofitem1->I:indexofitem2->I:indexofitem3
    """

    def __init__(self, location):
        self.location = location.split("->")

    def get_treeitem(self, treeitems: Any, index: Any):
        """
        This function gets the index of the location, the location can either be a name or index,
        and returns the corresponding tree item to that name or index.
        if the given name or index is not found a flauierror will be thrown.
        """
        loc = self.location[index]

        if loc.startswith("I:"):
            loc = loc[2:]
            try:
                return treeitems[int(loc)]
            except IndexError:
                raise FlaUiError(FlaUiError.ArrayOutOfBoundException.format(int(loc))) from None

        elif loc.startswith("N:"):
            loc = loc[2:]
            for item in treeitems:
                if item.Name == loc:
                    return item
            raise FlaUiError(FlaUiError.ElementNameNotFound.format(loc))
        else:
            raise FlaUiError(FlaUiError.FalseSyntax.format(loc)) from None

    def is_last_element(self, index: Any):
        """
        Returns true if the index corresponds the last element of given location series.
        """
        if index == len(self.location) - 1:
            return True
        return False
