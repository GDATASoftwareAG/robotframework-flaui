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
        module = self._container.create_or_get_module()
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
        module = self._container.create_or_get_module()
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
        module = self._container.create_or_get_module()
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
        module = self._container.create_or_get_module()
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
        module = self._container.create_or_get_module()
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
        module = self._container.create_or_get_module()
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
        module = self._container.create_or_get_module()
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
        module = self._container.create_or_get_module()
        return module.action(Element.Action.IS_ELEMENT_ENABLED,
                             Element.create_value_container(xpath=identifier, msg=msg),
                             msg)

    @keyword
    def is_element_offscreen(self, identifier, msg=None):
        """
        Checks if element is offscreen (true) or not (false).

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | ${IS_OFFSCREEN}  Is Element Offscreen  <XPATH> |

        """
        module = self._container.create_or_get_module()
        return not module.action(Element.Action.IS_ELEMENT_OFFSCREEN,
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
        module = self._container.create_or_get_module()
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
        module = self._container.create_or_get_module()
        module.action(Element.Action.ELEMENT_SHOULD_BE_DISABLED,
                      Element.create_value_container(xpath=identifier, msg=msg),
                      msg)

    @keyword
    def wait_until_element_is_offscreen(self, identifier, retries=10, msg=None):
        """
        Waits until element is offscreen or timeout was reached. If timeout was reached an FlaUIError occurred.

        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is visible          |

        Arguments:
        | Argument   | Type   | Description                                                           |
        | identifier | string | XPath identifier from element                                         |
        | retries    | number | Maximum amount of retries per seconds to wait. By default, 10 retries. |
        | msg        | string | Custom error message                                                  |

        Example:
        | Wait Until Element Is Offscreen  <XPATH>  <RETRIES=10> |
        | Wait Until Element Is Offscreen  <XPATH>  <RETRIES=10>  <MSG> |
        """
        module = self._container.create_or_get_module()
        module.action(Element.Action.WAIT_UNTIL_ELEMENT_IS_OFFSCREEN,
                      Element.create_value_container(xpath=identifier, retries=retries),
                      msg)

    @keyword
    def wait_until_element_exist(self, identifier, retries=10, msg=None):
        """
        Waits until element exist or timeout was reached. If timeout was reached an FlaUIError occurred.

        XPaths syntax is explained in `XPath locator`.
        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is not enabled      |

        Arguments:
        | Argument   | Type   | Description                                                            |
        | identifier | string | XPath identifier from element                                          |
        | retries    | number | Maximum amount of retries per seconds to wait. By default, 10 retries. |
        | msg        | string | Custom error message                                                   |

        Example:
        | Wait Until Element Exist  <XPATH>  <RETRIES=10> |
        | Wait Until Element Exist  <XPATH>  <RETRIES=10>  <MSG> |
        """
        module = self._container.create_or_get_module()
        module.action(Element.Action.WAIT_UNTIl_ELEMENT_EXIST,
                      Element.create_value_container(xpath=identifier, retries=retries),
                      msg)

    @keyword
    def wait_until_element_does_not_exist(self, identifier, retries=10, msg=None):
        """
        Waits until element does not exist or timeout was reached. If timeout was reached an FlaUIError occurred.

        XPaths syntax is explained in `XPath locator`.
        Possible FlaUI-Errors:
        | Element could not be found by xpath |
        | Element <XPATH> is not enabled      |

        Arguments:
        | Argument   | Type   | Description                                                            |
        | identifier | string | XPath identifier from element                                          |
        | retries    | number | Maximum amount of retries per seconds to wait. By default, 10 retries. |
        | msg        | string | Custom error message                                                   |

        Example:
        | Wait Until Element Does Not Exist  <XPATH>  <RETRIES=10> |
        | Wait Until Element Does Not Exist  <XPATH>  <RETRIES=10>  <MSG> |
        """
        module = self._container.create_or_get_module()
        module.action(Element.Action.WAIT_UNTIL_ELEMENT_DOES_NOT_EXIST,
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
        module = self._container.create_or_get_module()
        module.action(Element.Action.WAIT_UNTIL_ELEMENT_IS_ENABLED,
                      Element.create_value_container(xpath=identifier, retries=retries),
                      msg)

    @keyword
    def find_all_elements(self, identifier, msg=None):
        """
        Find all elements from given xpath, Returns an AutomationElement list which contains properties to Xpath.
        If AutomationId, ClassName or Name is set. Xpath can be used by these values and will be returned.

        | Example usage AutomationElement                                        |
        | Xpath        --> /Window[1]/Tab/TabItem[1]                             |
        | AutomationId --> /Window[1]/Tab/TabItem[@AutomationId="SimpleControl"] |
        | Name         --> /Window[1]/Tab/TabItem[@Name="Simple Controls"]       |
        | ClassName    --> /Window[1]/Tab/TabItem[@ClassName="TabItem"]          |

        If any property is not set empty string value will be returned.

        XPaths syntax is explained in `XPath locator`.

        Arguments:
        | Argument   | Type   | Description                                                           |
        | identifier | string | XPath identifier from element                                         |
        | msg        | string | Custom error message                                                  |

        Example:
        | ${elements}  Find All Elements  <XPATH>             |
        | ${Xpath}  Set Variable  ${element[0].Xpath}         |
        | ${Id}  Set Variable  ${element[0].AutomationId}     |
        | ${Name}  Set Variable  ${element[0].Name}           |
        | ${ClassName}  Set Variable  ${element[0].ClassName} |
        """
        module = self._container.create_or_get_module()
        return module.action(Element.Action.FIND_ALL_ELEMENTS,
                             Element.create_value_container(xpath=identifier),
                             msg)
