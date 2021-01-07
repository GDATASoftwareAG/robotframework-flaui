from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.module import (Mouse, Element)


class MouseKeywords:
    """
    Interface implementation from robotframework usage for mouse keywords.
    """

    def __init__(self, module):
        """Constructor for mouse keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def click(self, identifier, msg=None):
        """Left click to element by an XPath.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Click  <XPATH> |

        """
        self._module.action(Mouse.Action.LEFT_CLICK,
                            self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                            msg)

    @keyword
    def double_click(self, identifier, msg=None):
        """Double click to element.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Double Click  <XPATH> |

        """
        self._module.action(Mouse.Action.DOUBLE_CLICK,
                            self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                            msg)

    @keyword
    def right_click(self, identifier, msg=None):
        """Right click to element.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Right Click  <XPATH> |

        """
        self._module.action(Mouse.Action.RIGHT_CLICK,
                            self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                            msg)

    @keyword
    def move_to(self, identifier, msg=None):
        """Move mouse cursor to given element.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Move To  <XPATH> |

        """
        self._module.action(Mouse.Action.MOVE_TO,
                            self._module.action(Element.Action.GET_ELEMENT, identifier, msg),
                            msg)
