from robotlibcore import keyword
from FlaUILibrary.flaui.module import Property
from FlaUILibrary.flaui.automation.uia import UIA


class PropertyKeywords:
    """
    Interface implementation from robotframework usage for property keywords.
    """

    def __init__(self, module: UIA):
        """
        Constructor for mouse keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def get_background_color(self, identifier, msg=None):
        """
        Returns background color as ARGB Tuple (int, int, int, int) from element if background color pattern is
        supported.

        If background color pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Background Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.BACKGROUND_COLOR,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def get_foreground_color(self, identifier, msg=None):
        """
        Returns foreground color as ARGB Tuple (int, int, int, int) from element if foreground color pattern is
        supported.

        If foreground color pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Background Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.FOREGROUND_COLOR,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def get_font_size(self, identifier, msg=None):
        """
        Get font size as floating point value.

        If font size pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Background Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.FONT_SIZE,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def get_font_name(self, identifier, msg=None):
        """
        Get given font name from element.

        If font name pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Background Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.FONT_NAME,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def get_font_weight(self, identifier, msg=None):
        """
        Get font weight pattern as floating point value.

        If font size pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Background Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.FONT_WEIGHT,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)


    @keyword
    def get_culture(self, identifier, msg=None):
        """
        Get culture from given element. This keyword only works by UIA3. UIA2 contains currently a bug.
        See https://github.com/FlaUI/FlaUI/issues/554 for mor informations.

        If culture pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Background Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.CULTURE,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def is_hidden(self, identifier, msg=None):
        """
        Verification if element is hidden.

        If pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Background Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.IS_HIDDEN,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def is_visible(self, identifier, msg=None):
        """
        Verification if element is visible.

        If pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Background Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return not self._module.action(Property.Action.IS_HIDDEN,
                                       Property.create_value_container(element=element, uia=self._module.identifier()),
                                       msg)

    @keyword
    def get_window_visual_state(self, identifier, msg=None):
        """
        Get Windows Visual State as string. Possible states are "Normal", "Maximized", "Minimized"

        If pattern is not supported a Not Supported Exception will be called.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Window Visual State  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.WINDOW_VISUAL_STATE,
                                   Property.create_value_container(element=element),
                                   msg)
