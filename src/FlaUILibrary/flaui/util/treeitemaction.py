from enum import Enum


class TreeItemAction(Enum):
    """
    Enumeration class for supported tree item actions by syntax usage from tree selection.
    """
    EXPAND = "Expand"
    COLLAPSE = "Collapse"
    SELECT = "Select"
