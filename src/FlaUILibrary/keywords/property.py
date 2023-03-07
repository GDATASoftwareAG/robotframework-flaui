from robotlibcore import keyword
from FlaUILibrary.flaui.module import Property
from FlaUILibrary.flaui.automation.uia import UIA
from FlaUILibrary.flaui.exception import FlaUiError


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
    def background_color_should_be(self, identifier, argb_color, msg=None):
        """
        Verification if background color is equal.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                |
        | Document pattern is not supported by given element |
        | Color is not equal                                 |

        Arguments:
        | Argument   | Type   | Description                            |
        | identifier | string | XPath identifier from element          |
        | argb_color | tuple  | ARGB color format (int, int, int, int) |
        | msg        | string | Custom error message                   |

        Example:
        | Background Color Should Be  <XPATH>  <COLOR_ARGB_TUPLE> |

        """
        element = self._module.get_element(identifier, msg=msg)
        color = self._module.action(Property.Action.BACKGROUND_COLOR,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

        if color != argb_color:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(color, argb_color))

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
    def foreground_color_should_be(self, identifier, argb_color, msg=None):
        """
        Verification if foreground color is equal.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                |
        | Document pattern is not supported by given element |
        | Color is not equal                                 |

        Arguments:
        | Argument   | Type   | Description                            |
        | identifier | string | XPath identifier from element          |
        | argb_color | tuple  | ARGB color format (int, int, int, int) |
        | msg        | string | Custom error message                   |

        Example:
        | Foreground Color Should Be  <XPATH>  <COLOR_ARGB_TUPLE> |

        """
        element = self._module.get_element(identifier, msg=msg)
        color = self._module.action(Property.Action.FOREGROUND_COLOR,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

        if color != argb_color:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(color, argb_color))

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
    def font_size_should_be(self, identifier, font_size, msg=None):
        """
        Verification if font size is equal.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                |
        | Document pattern is not supported by given element |
        | Font size is not equal                             |

        Arguments:
        | Argument   | Type    | Description                       |
        | identifier | string  | XPath identifier from element     |
        | font_size  | float   | Font size as floating point value |
        | msg        | string  | Custom error message              |

        Example:
        | Font Size Should Be  <XPATH>  <FONT_SIZE_FLOATING_POINT> |

        """
        element = self._module.get_element(identifier, msg=msg)
        size = self._module.action(Property.Action.FONT_SIZE,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

        if size != font_size:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(size, font_size))

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
    def font_name_should_be(self, identifier, font_name, msg=None):
        """
        Verification if font name is equal.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                |
        | Document pattern is not supported by given element |
        | Font name is not equal                             |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | font_name  | string | Font name to equalize         |
        | msg        | string | Custom error message          |

        Example:
        | Font Name Should Be  <XPATH>  <FONT_NAME> |

        """
        element = self._module.get_element(identifier, msg=msg)
        name = self._module.action(Property.Action.FONT_NAME,
                                   Property.create_value_container(element=element, uia=self._module.identifier()),
                                   msg)

        if name != font_name:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(name, font_name))

    @keyword
    def get_font_weight(self, identifier, msg=None):
        """
        Get font weight as floating point value.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath            |
        | Document pattern is not supported by given element |

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
    def font_weight_should_be(self, identifier, font_weight, msg=None):
        """
        Verification if font weight is equal.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath                |
        | Document pattern is not supported by given element |
        | Font weight is not equal                           |

        Arguments:
        | Argument     | Type   | Description                         |
        | identifier   | string | XPath identifier from element       |
        | font_weight  | float  | Font weight as floating point value |
        | msg          | string | Custom error message                |

        Example:
        | Font Weight Should Be  <XPATH>  <FONT_WEIGHT_FLOATING_POINT> |

        """
        element = self._module.get_element(identifier, msg=msg)
        weight = self._module.action(Property.Action.FONT_WEIGHT,
                                     Property.create_value_container(element=element, uia=self._module.identifier()),
                                     msg)

        if weight != font_weight:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(weight, font_weight))

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
    def culture_should_be(self, identifier, culture, msg=None):
        """
        Checks if element is in given culture. This keyword only works by UIA3. UIA2 contains currently a bug.
        See https://github.com/FlaUI/FlaUI/issues/554 for more information.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element is not in expected culture format         |
        | Element could not be found by xpath               |
        | Culture pattern is not supported by given element |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | culture    | string | Culture to equalize           |
        | msg        | string | Custom error message          |

        Example:
        | Culture Should Be  <XPATH>  <CULTURE> |

        """
        element = self._module.get_element(identifier, msg=msg)
        element_culture = self._module.action(Property.Action.CULTURE,
                                              Property.create_value_container(element=element,
                                                                              uia=self._module.identifier()),
                                              msg)

        if culture != element_culture:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(element_culture, culture))

    @keyword
    def is_hidden(self, identifier, msg=None):
        """
        Verification if element is hidden. Returns True if element is Hidden otherwise False.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Text pattern is not supported by given element |

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
        | Text pattern is not supported by given element |

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
    def window_visual_state_should_be(self, identifier, state, msg=None):
        """
        Verification if window is in given window visual state.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |
        | Visual state is not equal to given state          |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | state      | string | Possible states are "Normal", "Maximized", "Minimized"  |
        | msg        | string | Custom error message          |

        Examples:
        | Window Visual State Should Be  <XPATH>  <STATE> |

        """
        element = self._module.get_element(identifier, msg=msg)
        visual_state = self._module.action(Property.Action.WINDOW_VISUAL_STATE,
                                           Property.create_value_container(element=element),
                                           msg)

        if visual_state != state:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(visual_state, state))

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

    @keyword
    def toggle_state_should_be(self, identifier, state, msg=None):
        """
        Verification if element is in expected toggle state.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Toggle pattern is not supported by given element  |
        | Toggle state is not equal to given state          |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | state      | string | Possible states are "ON", "OFF", "Indeterminate" |
        | msg        | string | Custom error message          |

        Examples:
        | Toggle State Should Be  <XPATH>  <STATE> |

        """
        element = self._module.get_element(identifier, msg=msg)

        toggle_state = self._module.action(Property.Action.TOGGLE_STATE,
                                           Property.create_value_container(element=element),
                                           msg)

        if toggle_state != state:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(toggle_state, state))
