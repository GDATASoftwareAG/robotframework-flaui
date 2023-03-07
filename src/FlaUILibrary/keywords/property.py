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

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                                                     |
        | Document pattern is not supported by given element to receive background color property |

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

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                                                     |
        | Document pattern is not supported by given element to receive foreground color property |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${color}  Get Foreground Color  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.FOREGROUND_COLOR,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def get_font_size(self, identifier, msg=None):
        """
        Get font size as floating point value.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                                              |
        | Document pattern is not supported by given element to receive font size property |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${font_size}  Get Font Size  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.FONT_SIZE,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def get_font_name(self, identifier, msg=None):
        """
        Get font name from element.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                                              |
        | Document pattern is not supported by given element to receive font name property |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${font_name}  Get Font Name  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.FONT_NAME,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def get_font_weight(self, identifier, msg=None):
        """
        Get font weight as floating point value.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath            |
        | Font pattern is not supported by given element |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | ${font_weight}  Get Font Weight  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.FONT_WEIGHT,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)


    @keyword
    def get_culture(self, identifier, msg=None):
        """
        Get culture from given element. This keyword only works by UIA3. UIA2 contains currently a bug.
        See https://github.com/FlaUI/FlaUI/issues/554 for more information.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Culture pattern is not supported by given element |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Example:
        | ${culture}  Get Culture  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.CULTURE,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def is_hidden(self, identifier, msg=None):
        """
        Verification if element is hidden. Returns True if element is Hidden otherwise False.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Culture pattern is not supported by given element |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${is_element_hidden}  Is Hidden  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.IS_HIDDEN,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

    @keyword
    def is_visible(self, identifier, msg=None):
        """
        Verification if element is visible. Return True if Element is Visible otherwise False.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Culture pattern is not supported by given element |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${is_element_visible}  Is Visible  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return not self._module.action(Property.Action.IS_HIDDEN,
                                       Property.create_value_container(element=element, uia=self._module.identifier()),
                                       msg)

    @keyword
    def get_window_visual_state(self, identifier, msg=None):
        """
        Get Windows Visual State as string. Possible states are "Normal", "Maximized", "Minimized"

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${state}  Get Window Visual State  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.WINDOW_VISUAL_STATE,
                                   Property.create_value_container(element=element),
                                   msg)



    @keyword
    def get_toggle_state(self, identifier, msg=None):
        """
        Get Toggle State as string. Possible states are "ON", "OFF", "Indeterminate"

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Toggle pattern is not supported by given element  |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${toggle_state}  Get Toggle State  <XPATH> |

        """
        element = self._module.get_element(identifier, msg=msg)
        return self._module.action(Property.Action.TOGGLE_STATE,
                                   Property.create_value_container(element=element),
                                   msg)
