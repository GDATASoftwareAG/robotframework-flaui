from enum import Enum


class InterfaceType(Enum):
    """Enum declaration for supported ui component handling"""
    INVALID = 0
    TEXTBOX = 1
    CHECKBOX = 2
    COMBOBOX = 3
    WINDOW = 4
    LISTVIEW = 5
    RADIOBUTTON = 6
    LISTBOX = 7
    TAB = 8
