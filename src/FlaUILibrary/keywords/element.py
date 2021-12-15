from robotlibcore import keyword
from FlaUILibrary.flaui.module.element import Element


class ElementKeywords:
    """
    Interface implementation from robotframework usage for element keywords.
    """

    def __init__(self, module):
        """
        Constructor for element keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def element_should_exist(self, identifier, use_exception=True, msg=None):
        """
        Checks if element exists. If element exists True will be returned otherwise False.
        If element could not be found by xpath False will be returned.

        XPath syntax is explained in `XPath locator`.

        Arguments:
        | Argument      | Type   | Description                   |
        | identifier    | string | XPath identifier from element |
        | use_exception | bool   | Indicator if an FlaUI exception should be called if element
                                   could not be found by xpath |
        | msg           | string | Custom error message |

        Example for custom result handling:
        | ${RESULT}  Element Should Exist  <XPATH>  ${FALSE} |
        | Run Keyword If  ${RESULT} == ${False} |

        Example if element will be shown after a click and takes a few seconds to open:
        | Click  <XPATH> |
        | Wait Until Keyword Succeeds  5x  10ms  Element Should Exist  <XPATH> |

        """
        return self._module.action(Element.Action.ELEMENT_SHOULD_EXIST,
                                   Element.create_value_container(xpath=identifier,
                                                                  use_exception=use_exception,
                                                                  msg=msg), msg)

    @keyword
    def element_should_not_exist(self, identifier, use_exception=True, msg=None):
        """
        Checks if element exists. If element exists False will be returned otherwise True.
        If element could not be found by xpath True will be returned.

        XPath syntax is explained in `XPath locator`.

        Arguments:
        | Argument      | Type   | Description                   |
        | identifier    | string | XPath identifier from element |
        | use_exception | bool   | Indicator if an FlaUI exception should be called if element
                                   could not be found by xpath |
        | msg           | string | Custom error message |


        Example for custom result handling:
        | ${RESULT}  Element Should Not Exist  <XPATH>  ${FALSE} |
        | Run Keyword If  ${RESULT} == ${False} |

        Example if element will be shown after a click and takes a few seconds to open:
        | Click  <XPATH> |
        | Wait Until Keyword Succeeds  5x  10ms  Element Should Not Exist  <XPATH> |

        """
        return self._module.action(Element.Action.ELEMENT_SHOULD_NOT_EXIST,
                                   Element.create_value_container(xpath=identifier,
                                                                  use_exception=use_exception,
                                                                  msg=msg), msg)

    @keyword
    def focus(self, identifier, msg=None):
        """
        Try to focus element by given xpath.

        XPath syntax is explained in `XPath locator`.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Focus  <XPATH>  |

        """
        self._module.action(Element.Action.FOCUS_ELEMENT,
                            Element.create_value_container(xpath=identifier, msg=msg),
                            msg)

    @keyword
    def get_name_from_element(self, identifier, msg=None):
        """
        Return name value from element.

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
        return self._module.action(Element.Action.GET_ELEMENT_NAME,
                                   Element.create_value_container(xpath=identifier, msg=msg),
                                   msg)

    @keyword
    def name_should_be(self, name, identifier, msg=None):
        """
        Verifies if name from element is equal.

        Arguments:
        | Argument   | Type   | Description                   |
        | name       | string | Name to compare               |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

         Example:
        | Name Should Be  <NAME>  <XPATH> |
        """
        self._module.action(Element.Action.NAME_SHOULD_BE,
                            Element.create_value_container(xpath=identifier, name=name, msg=msg),
                            msg)

    @keyword
    def name_contains_text(self, name, identifier, msg=None):
        """
        Verifies if element name contains to name.

        Arguments:
        | Argument   | Type   | Description                   |
        | name       | string | Name to compare               |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Name Contains Text  <NAME>  <XPATH> |

        """
        self._module.action(Element.Action.NAME_SHOULD_CONTAINS,
                            Element.create_value_container(xpath=identifier, name=name, msg=msg),
                            msg)

    @keyword
    def is_element_enabled(self, identifier, msg=None):
        """
        Verifies if element is enabled (true) or not (false).

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
        return self._module.action(Element.Action.IS_ELEMENT_ENABLED,
                                   Element.create_value_container(xpath=identifier, msg=msg),
                                   msg)

    @keyword
    def is_element_visible(self, identifier, msg=None):
        """
        Checks if element is visible (true) or not (false).

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | ${IS_VISIBLE}  Is Element Visible  <XPATH> |

        """
        return not self._module.action(Element.Action.IS_ELEMENT_VISIBLE,
                                       Element.create_value_container(xpath=identifier, msg=msg),
                                       msg)

    @keyword
    def element_should_be_visible(self, identifier, msg=None):
        """
        Checks if element is visible.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Element Should Be Visible  <XPATH> |

        """
        self._module.action(Element.Action.ELEMENT_SHOULD_BE_VISIBLE,
                            Element.create_value_container(xpath=identifier, msg=msg),
                            msg)


    @keyword
    def element_should_not_be_visible(self, identifier, msg=None):
        """
        Checks if element is visible.

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Element Should Not Be Visible  <XPATH> |

        """
        self._module.action(Element.Action.ELEMENT_SHOULD_NOT_BE_VISIBLE,
                            Element.create_value_container(xpath=identifier, msg=msg),
                            msg)

    @keyword
    def wait_until_element_is_hidden(self, identifier, retries=10, msg=None):
        """
        Waits until element is hidden or timeout was reached. If timeout was reached an FlaUIError occurred.

        XPath syntax is explained in `XPath locator`.

        Arguments:
        | Argument   | Type   | Description                                                           |
        | identifier | string | XPath identifier from element                                         |
        | retries    | number | Maximum amount of retries per seconds to wait. By default 10 retries. |
        | msg        | string | Custom error message                                                  |

        Example:
        | Wait Until Element Is Hidden  <XPATH>  <RETRIES=10> |
        | Wait Until Element Is Hidden  <XPATH>  <RETRIES=10>  <MSG> |
        """
        self._module.action(Element.Action.WAIT_UNTIL_ELEMENT_IS_HIDDEN,
                            Element.create_value_container(xpath=identifier, retries=retries),
                            msg)

    @keyword
    def wait_until_element_is_visible(self, identifier, retries=10, msg=None):
        """
        Waits until element is visible or timeout was reached. If timeout was reached an FlaUIError occurred.

        XPath syntax is explained in `XPath locator`.

        Arguments:
        | Argument   | Type   | Description                                                           |
        | identifier | string | XPath identifier from element                                         |
        | retries    | number | Maximum amount of retries per seconds to wait. By default 10 retries. |
        | msg        | string | Custom error message                                                  |

        Example:
        | Wait Until Element Is VISIBLE  <XPATH>  <RETRIES=10> |
        | Wait Until Element Is VISIBLE  <XPATH>  <RETRIES=10>  <MSG> |
        """
        self._module.action(Element.Action.WAIT_UNTIL_ELEMENT_IS_VISIBLE,
                            Element.create_value_container(xpath=identifier, retries=retries),
                            msg)
