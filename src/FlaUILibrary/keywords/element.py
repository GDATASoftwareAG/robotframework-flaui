from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.module.element import Element


class ElementKeywords:
    """
    Interface implementation from robotframework usage for element keywords.
    """

    def __init__(self, module):
        """Constructor for element keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def element_should_exist(self, identifier, msg=None):
        """Checks if element exists. If element exists True will be returned otherwise False.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Element Should Exist  <XPATH> |

        """
        self._module.action(Element.Action.GET_ELEMENT, identifier, msg)

    @keyword
    def element_should_not_exist(self, identifier, msg=None):
        """Checks if element exists. If element exists False will be returned otherwise True.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Element Should Exist  <XPATH> |

        """
        self._module.action(Element.Action.ELEMENT_SHOULD_NOT_EXIST, identifier, msg)

    @keyword
    def focus(self, identifier, msg=None):
        """Try to focus element by given xpath.

        XPath syntax is explained in `XPath locator`.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Focus  <XPATH>  |

        """
        self._module.action(Element.Action.FOCUS_ELEMENT, identifier, msg)

    @keyword
    def get_name_from_element(self, identifier, msg=None):
        """Return name value from element.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${NAME}  Get Name From Element  <XPATH> |

        Returns:
        | Name from element if set otherwise empty string |

        """
        return self._module.action(Element.Action.GET_ELEMENT_NAME, identifier, msg)

    @keyword
    def name_should_be(self, name, identifier, msg=None):
        """Verifies if name from element is equal.

        Arguments:
        | Argument   | Type   | Description                   |
        | name       | string | Name to compare               |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

         Example:
        | Name Should Be  <NAME>  <XPATH> |
        """
        self._module.action(Element.Action.NAME_SHOULD_BE, [identifier, name], msg)

    @keyword
    def name_contains_text(self, name, identifier, msg=None):
        """Verifies if element name contains to name.

        Arguments:
        | Argument   | Type   | Description                   |
        | name       | string | Name to compare               |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Name Contains Text  <NAME>  <XPATH> |

        """
        self._module.action(Element.Action.NAME_SHOULD_CONTAINS, [identifier, name], msg)

    @keyword
    def is_element_enabled(self, identifier, msg=None):
        """Verifies if element is enabled (true) or not (false).

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | ${IS_ENABLED} =  Is Item Enabled <XPATH> |

        Returns:
        | <True> if element is enabled otherwise <False> |
        """
        return self._module.action(Element.Action.IS_ELEMENT_ENABLED, identifier, msg)

    @keyword
    def is_element_visible(self, identifier, msg=None):
        """Checks if element is visible (true) or not (false).

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        |${IS_VISIBLE}  Is Element Visible  <XPATH> |

        """
        return not self._module.action(Element.Action.IS_ELEMENT_VISIBLE, identifier, msg)

    @keyword
    def element_should_be_visible(self, identifier, msg=None):
        """Checks if element is visible.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        |Element Should Be Visible  <XPATH> |

        """
        self._module.action(Element.Action.ELEMENT_SHOULD_BE_VISIBLE, identifier, msg)


    @keyword
    def element_should_not_be_visible(self, identifier, msg=None):
        """Checks if element is visible.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        |Element Should Not Be Visible  <XPATH> |

        """
        self._module.action(Element.Action.ELEMENT_SHOULD_NOT_BE_VISIBLE, identifier, msg)

    @keyword
    def wait_until_element_is_hidden(self, identifier, timeout=10, msg=None):
        """Waits until element is hidden or timeout was reached. If timeout was reached an FlaUIError occurred.
        Checks if element exists before Wait Until Element Is Hidden is called.

        XPath syntax is explained in `XPath locator`.

        Arguments:
        | Argument   | Type   | Description                                                       |
        | identifier | string | XPath identifier from element                                     |
        | timeout    | number | Maximum amount of time in seconds to wait. By default 10 seconds. |
        | msg        | string | Custom error message                                              |

        Example:
        | Wait Until Element Is Hidden  <XPATH>  <TIMEOUT=10> |
        | Wait Until Element Is Hidden  <XPATH>  <TIMEOUT=10>  <MSG> |
        """
        self.element_should_exist(identifier, msg)
        self._module.action(Element.Action.WAIT_UNTIL_ELEMENT_IS_HIDDEN, [identifier, timeout], msg)
