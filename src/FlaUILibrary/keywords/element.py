from robotlibcore import keyword
from FlaUILibrary.flaui.module.element import Element
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class ElementKeywords:
    """
    Interface implementation from robotframework usage for element keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for element keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def element_should_exist(self, identifier, use_exception=True, msg=None):
        """
        Checks if element exists. If element exists True will be returned otherwise False.
        If element could not be found by xpath False will be returned.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |

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
        module = self._container.get_module()
        return module.action(Element.Action.ELEMENT_SHOULD_EXIST,
                             Element.create_value_container(xpath=identifier, use_exception=use_exception, msg=msg),
                             msg)

    @keyword
    def element_should_not_exist(self, identifier, use_exception=True, msg=None):
        """
        Checks if element exists. If element exists False will be returned otherwise True.
        If element could not be found by xpath True will be returned.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element <XPATH> exists |

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
        module = self._container.get_module()
        return module.action(Element.Action.ELEMENT_SHOULD_NOT_EXIST,
                             Element.create_value_container(xpath=identifier, use_exception=use_exception, msg=msg),
                             msg)

    @keyword
    def focus(self, identifier, msg=None):
        """
        Try to focus element by given xpath.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Focus  <XPATH>  |

        """
        module = self._container.get_module()
        module.action(Element.Action.FOCUS_ELEMENT,
                      Element.create_value_container(xpath=identifier, msg=msg),
                      msg)

    @keyword
    def get_name_from_element(self, identifier, msg=None):
        """
        Return name value from element.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${NAME}  Get Name From Element  <XPATH> |

        Returns:
        | Name from element if set otherwise empty string |

        """
        module = self._container.get_module()
        return module.action(Element.Action.GET_ELEMENT_NAME,
                             Element.create_value_container(xpath=identifier, msg=msg),
                             msg)

    @keyword
    def get_rectangle_bounding_from_element(self, identifier, msg=None):
        """
        Return rectangle value from element.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | @{Rectangle}  Get Rectangle Bounding From Element  <XPATH> |

        Returns:
        | An array Rectangle Bounding from element : [rect.X, rect.Y, rect.Width, rect.Height]|

        """
        module = self._container.get_module()
        return module.action(Element.Action.GET_ELEMENT_RECTANGLE_BOUNDING,
                             Element.create_value_container(xpath=identifier, msg=msg),
                             msg)

    @keyword
    def name_should_be(self, name, identifier, msg=None):
        """
        Verifies if name from element is equal.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Name from element <XPATH> is not equals to <NAME> |

        Arguments:
        | Argument   | Type   | Description                   |
        | name       | string | Name to compare               |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

         Example:
        | Name Should Be  <NAME>  <XPATH> |
        """
        module = self._container.get_module()
        module.action(Element.Action.NAME_SHOULD_BE,
                      Element.create_value_container(xpath=identifier, name=name, msg=msg),
                      msg)

    @keyword
    def name_contains_text(self, name, identifier, msg=None):
        """
        Verifies if element name contains to name.

        Possible FlaUI-Errors:
        | Element could not be found by xpath              |
        | Name from element <XPATH> does not contain <NAME> |

        Arguments:
        | Argument   | Type   | Description                   |
        | name       | string | Name to compare               |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Name Contains Text  <NAME>  <XPATH> |

        """
        module = self._container.get_module()
        module.action(Element.Action.NAME_SHOULD_CONTAINS,
                      Element.create_value_container(xpath=identifier, name=name, msg=msg),
                      msg)

    @keyword
    def is_element_enabled(self, identifier, msg=None):
        """
        Verifies if element is enabled (true) or not (false).

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | ${IS_ENABLED} =  Is Element Enabled  <XPATH> |

        Returns:
        | <True> if element is enabled otherwise <False> |
        """
        module = self._container.get_module()
        return module.action(Element.Action.IS_ELEMENT_ENABLED,
                             Element.create_value_container(xpath=identifier, msg=msg),
                             msg)

    @keyword
    def is_element_visible(self, identifier, msg=None):
        """
        Checks if element is visible (true) or not (false).

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | ${IS_VISIBLE}  Is Element Visible  <XPATH> |

        """
        module = self._container.get_module()
        return not module.action(Element.Action.IS_ELEMENT_VISIBLE,
                                 Element.create_value_container(xpath=identifier, msg=msg),
                                 msg)

    @keyword
    def element_should_be_visible(self, identifier, msg=None):
        """
        Checks if element is visible.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is not visible      |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Element Should Be Visible  <XPATH> |

        """
        module = self._container.get_module()
        module.action(Element.Action.ELEMENT_SHOULD_BE_VISIBLE,
                      Element.create_value_container(xpath=identifier, msg=msg),
                      msg)

    @keyword
    def element_should_not_be_visible(self, identifier, msg=None):
        """
        Checks if element is visible.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is visible          |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Element Should Not Be Visible  <XPATH> |

        """
        module = self._container.get_module()
        module.action(Element.Action.ELEMENT_SHOULD_NOT_BE_VISIBLE,
                      Element.create_value_container(xpath=identifier, msg=msg),
                      msg)

    @keyword
    def element_should_be_enabled(self, identifier, msg=None):
        """
        Checks if element is enabled.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is not enabled      |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Element Should Be Enabled  <XPATH> |

        """
        module = self._container.get_module()
        module.action(Element.Action.ELEMENT_SHOULD_BE_ENABLED,
                      Element.create_value_container(xpath=identifier, msg=msg),
                      msg)

    @keyword
    def element_should_be_disabled(self, identifier, msg=None):
        """
        Checks if element is disabled.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is not disabled     |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | Element Should Be Disabled  <XPATH> |

        """
        module = self._container.get_module()
        module.action(Element.Action.ELEMENT_SHOULD_BE_DISABLED,
                      Element.create_value_container(xpath=identifier, msg=msg),
                      msg)

    @keyword
    def wait_until_element_is_hidden(self, identifier, retries=10, msg=None):
        """
        Waits until element is hidden or timeout was reached. If timeout was reached an FlaUIError occurred.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is visible          |

        Arguments:
        | Argument   | Type   | Description                                                           |
        | identifier | string | XPath identifier from element                                         |
        | retries    | number | Maximum amount of retries per seconds to wait. By default, 10 retries. |
        | msg        | string | Custom error message                                                  |

        Example:
        | Wait Until Element Is Hidden  <XPATH>  <RETRIES=10> |
        | Wait Until Element Is Hidden  <XPATH>  <RETRIES=10>  <MSG> |
        """
        module = self._container.get_module()
        module.action(Element.Action.WAIT_UNTIL_ELEMENT_IS_HIDDEN,
                      Element.create_value_container(xpath=identifier, retries=retries),
                      msg)

    @keyword
    def wait_until_element_is_visible(self, identifier, retries=10, msg=None):
        """
        Waits until element is visible or timeout was reached. If timeout was reached an FlaUIError occurred.

        XPaths syntax is explained in `XPath locator`.
        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is not visible      |

        Arguments:
        | Argument   | Type   | Description                                                           |
        | identifier | string | XPath identifier from element                                         |
        | retries    | number | Maximum amount of retries per seconds to wait. By default, 10 retries. |
        | msg        | string | Custom error message                                                  |

        Example:
        | Wait Until Element Is Visible  <XPATH>  <RETRIES=10> |
        | Wait Until Element Is Visible  <XPATH>  <RETRIES=10>  <MSG> |
        """
        module = self._container.get_module()
        module.action(Element.Action.WAIT_UNTIL_ELEMENT_IS_VISIBLE,
                      Element.create_value_container(xpath=identifier, retries=retries),
                      msg)

    @keyword
    def wait_until_element_is_enabled(self, identifier, retries=10, msg=None):
        """
        Waits until element is enabled or timeout was reached. If timeout was reached an FlaUIError occurred.

        XPaths syntax is explained in `XPath locator`.
        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is not enabled      |

        Arguments:
        | Argument   | Type   | Description                                                           |
        | identifier | string | XPath identifier from element                                         |
        | retries    | number | Maximum amount of retries per seconds to wait. By default, 10 retries. |
        | msg        | string | Custom error message                                                  |

        Example:
        | Wait Until Element Is Enabled  <XPATH>  <RETRIES=10> |
        | Wait Until Element Is Enabled  <XPATH>  <RETRIES=10>  <MSG> |
        """
        module = self._container.get_module()
        module.action(Element.Action.WAIT_UNTIL_ELEMENT_IS_ENABLED,
                      Element.create_value_container(xpath=identifier, retries=retries),
                      msg)
