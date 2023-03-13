from robotlibcore import keyword
from FlaUILibrary.flaui.module import Mouse
from FlaUILibrary.flaui.automation.uia import UIA


class MouseKeywords:
    """
    Interface implementation from robotframework usage for mouse keywords.
    """

    def __init__(self, module: UIA):
        """
        Constructor for mouse keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def click(self, identifier, msg=None):
        """
        Left click to element by an XPath.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Click  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        self._module.action(Mouse.Action.LEFT_CLICK,
                            Mouse.create_value_container(element=element),
                            msg)

    @keyword
    def click_hold(self, identifier, timeout_in_ms=1000, msg=None):
        """
        Left click and hold to element by XPath and release after timeout.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument         | Type   | Description                   |
        | identifier       | string | XPath identifier from element |
        | timeout_in_ms    | int    | Holding time in ms            |
        | msg              | string | Custom error message          |

        Examples:
        | Click Hold <XPATH>  5000 |

        """
        element = self._module.get_element(identifier, msg=msg)
        self._module.action(Mouse.Action.LEFT_CLICK_HOLD,
                            Mouse.create_value_container(element=element, timeout_in_ms=int(timeout_in_ms)),
                            msg)

    @keyword
    def double_click(self, identifier, msg=None):
        """
        Double click to element.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Double Click  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        self._module.action(Mouse.Action.DOUBLE_CLICK,
                            Mouse.create_value_container(element=element),
                            msg)

    @keyword
    def double_click_hold(self, identifier, timeout_in_ms=1000, msg=None):
        """
        Double click and hold to element by XPath and release after timeout.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument         | Type   | Description                       |
        | identifier       | string | XPath identifier from element     |
        | timeout_in_ms    | int    | Holding time in ms                |
        | msg              | string | Custom error message              |

        Examples:
        | Double Click Hold  <XPATH>  5000 |

        """
        element = self._module.get_element(identifier, msg=msg)
        self._module.action(Mouse.Action.DOUBLE_CLICK_HOLD,
                            Mouse.create_value_container(element=element, timeout_in_ms=int(timeout_in_ms)),
                            msg)

    @keyword
    def right_click(self, identifier, msg=None):
        """
        Right click to element.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Right Click  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        self._module.action(Mouse.Action.RIGHT_CLICK,
                            Mouse.create_value_container(element=element),
                            msg)

    @keyword
    def right_click_hold(self, identifier, timeout_in_ms=1000, msg=None):
        """
        Right click and hold to element by XPath and release after timeout.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument      | Type   | Description                   |
        | identifier    | string | XPath identifier from element |
        | timeout_in_ms | int    | Holding time in ms            |
        | msg           | string | Custom error message          |

        Examples:
        | Right Click Hold  <XPATH>  5000 |

        """
        element = self._module.get_element(identifier, msg=msg)
        self._module.action(Mouse.Action.RIGHT_CLICK_HOLD,
                            Mouse.create_value_container(element=element, timeout_in_ms=int(timeout_in_ms)),
                            msg)

    @keyword
    def move_to(self, identifier, msg=None):
        """
        Move mouse cursor to given element.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Move To  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        self._module.action(Mouse.Action.MOVE_TO,
                            Mouse.create_value_container(element=element),
                            msg)

    @keyword
    def drag_and_drop(self, start_identifier, end_identifier, msg=None):
        """
        Clicks and hold the item with start_identifier and drops it at item with end_identifier.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument         | Type   | Description                                                        |
        | start_identifier | string | XPath identifier of element which should be holded and draged from |
        | end_identifier   | string | XPath identifier of element which should be holded and draged to   |
        | msg              | string | Custom error message                                               |

        Examples:
        | Drag And Drop  <XPATH>  <XPATH> |

        """
        start_element = self._module.get_element(start_identifier, msg=msg)
        end_element = self._module.get_element(end_identifier, msg=msg)
        self._module.action(Mouse.Action.DRAG_AND_DROP,
                            Mouse.create_value_container(element=start_element, second_element=end_element),
                            msg)
