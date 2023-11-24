from robotlibcore import keyword
from FlaUILibrary.flaui.module import Property
from FlaUILibrary.flaui.exception import FlaUiError
from FlaUILibrary.flaui.enum import InterfaceType
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer
from FlaUILibrary.flaui.util.converter import Converter


class PropertyKeywords:  # pylint: disable=too-many-public-methods
    """
    Interface implementation from robotframework usage for property keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for mouse keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def get_property_from_element(self, identifier, action, msg=None):
        # pylint: disable=line-too-long
        """
        Returns a supported property value from a given element if supported.

        XPaths syntax is explained in `XPath locator`.
        
        Supported operations:
        | Action | Type | Returns |
        | BACKGROUND_COLOR | Tuple (Numbers) | (A,R,G,B) |
        | FOREGROUND_COLOR | Tuple (Numbers) | (A,R,G,B) |
        | FONT_SIZE | Number | Font size |
        | FONT_NAME | String | Font name |
        | FONT_WEIGHT | Float | Font weight |
        | CULTURE | String | Iso Culture |
        | WINDOW_VISUAL_STATE | String | "Normal", "Maximized", "Minimized" |
        | WINDOW_INTERACTION_STATE | String | "Running", "Closing", "ReadyForUserInteraction", "BlockedByModalWindow", "NotResponding" |
        | TOGGLE_STATE | String | "ON", "OFF", "Indeterminate" |
        | CAN_WINDOW_MINIMIZE | Bool | True or False |
        | CAN_WINDOW_MAXIMIZE | Bool | True or False |
        | IS_READ_ONLY | Bool | True or False |
        | IS_WINDOW_PATTERN_SUPPORTED | Bool | True or False |
        | IS_TEXT_PATTERN_SUPPORTED | Bool | True or False |
        | IS_TOGGLE_PATTERN_SUPPORTED | Bool | True or False |
        | IS_VALUE_PATTERN_SUPPORTED | Bool | True or False |
        | VALUE | String | The Value Property of Element |
        | IS_EXPAND_COLLAPSE_PATTERN_SUPPORTED | Bool | True or False |
        | EXPAND_COLLAPSE_STATE | String | Collapsed or Expanded |   
        | IS_SELECTION_ITEM_PATTERN_SUPPORTED | Bool | True or False |    
        | IS_SELECTED | Bool | True or False |
        
        Possible FlaUI-Errors:
        | Element could not be found by xpath        |
        | Pattern is not supported by given element  |
        | Action is not supported                    |
        | Try to execute a setter property           |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | action     | string | Action to receive property    |
        | msg        | string | Custom error message          |

        Examples:
        | ${value}       Get Property From Element  <XPATH>  <PROPERTY> |

        """
        # pylint: enable=line-too-long
        
        action_value = ""
        try:
            action_value = Property.Action[action.upper()]
        except KeyError or action_value in [Property.Action.MAXIMIZE_WINDOW, Property.Action.MINIMIZE_WINDOW, Property.Action.NORMALIZE_WINDOW]:
            FlaUiError.raise_fla_ui_error(FlaUiError.InvalidPropertyArgument)
        
        module = self._container.create_or_get_module()
        
        if action_value is Property.Action.IS_SELECTED:
            # need expand parent ComboBox before to get ComboBox SelectionItem element
            combobox_xpath = Converter.get_combobox_xpath_from_combobox_selectionitem_xpath(identifier)
            if combobox_xpath:
                combobox_element = module.get_element(combobox_xpath, InterfaceType.COMBOBOX, msg)
                module.action(Property.Action.STAGE_FOR_COMBOBOX_SELECTIONITEM,
                            Property.create_value_container(element=combobox_element, uia=module.identifier()),
                            msg)

        element = module.get_element(identifier, msg=msg)
        property_value = module.action(action_value,
                            Property.create_value_container(element=element, uia=module.identifier()), 
                            msg)
        
        if action_value is Property.Action.IS_SELECTED:
            combobox_xpath = Converter.get_combobox_xpath_from_combobox_selectionitem_xpath(identifier)
            if combobox_xpath:
                combobox_element = module.get_element(combobox_xpath, InterfaceType.COMBOBOX, msg)
                module.action(Property.Action.STAGE_FOR_COMBOBOX_SELECTIONITEM,
                            Property.create_value_container(element=combobox_element, uia=module.identifier()),
                            msg)
        
        return property_value

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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.BACKGROUND_COLOR,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        color = module.action(Property.Action.BACKGROUND_COLOR,
                              Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.FOREGROUND_COLOR,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        color = module.action(Property.Action.FOREGROUND_COLOR,
                              Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.FONT_SIZE,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        size = module.action(Property.Action.FONT_SIZE,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.FONT_NAME,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        name = module.action(Property.Action.FONT_NAME,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.FONT_WEIGHT,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        weight = module.action(Property.Action.FONT_WEIGHT,
                               Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.CULTURE,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        element_culture = module.action(Property.Action.CULTURE,
                                        Property.create_value_container(element=element,
                                                                        uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.IS_HIDDEN,
                             Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return not module.action(Property.Action.IS_HIDDEN,
                                 Property.create_value_container(element=element, uia=module.identifier()),
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.WINDOW_VISUAL_STATE,
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        visual_state = module.action(Property.Action.WINDOW_VISUAL_STATE,
                                     Property.create_value_container(element=element),
                                     msg)

        if visual_state != state:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(visual_state, state))

    @keyword
    def get_window_interaction_state(self, identifier, msg=None):
        """
        Get Windows Interaction State as string.

        Possible states are:

        "Running" - The window is running. This does not guarantee that the window is ready for user interaction
                    or is responding.

        "Closing" - The window is closing.

        "ReadyForUserInteraction" - The window is ready for user interaction.

        "BlockedByModalWindow" - The window is blocked by a modal window.

        "NotResponding" - The window is not responding.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${state}  Get Window Interaction State  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.WINDOW_INTERACTION_STATE,
                             Property.create_value_container(element=element),
                             msg)

    @keyword
    def window_interaction_state_should_be(self, identifier, state, msg=None):
        # pylint: disable=line-too-long
        """
        Verification if window is in given window interaction state.

        Possible states are:

        "Running" - The window is running. This does not guarantee that the window is ready for user interaction
                    or is responding.

        "Closing" - The window is closing.

        "ReadyForUserInteraction" - The window is ready for user interaction.

        "BlockedByModalWindow" - The window is blocked by a modal window.

        "NotResponding" - The window is not responding.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |
        | Visual state is not equal to given state          |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | state      | string | Possible states are "Running", "Closing", "ReadyForUserInteraction", "BlockedByModalWindow", "NotResponding"  |
        | msg        | string | Custom error message          |

        Examples:
        | Window Interaction State Should Be  <XPATH>  <STATE> |

        """
        # pylint: enable=line-too-long
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        interaction_state = module.action(Property.Action.WINDOW_INTERACTION_STATE,
                                          Property.create_value_container(element=element),
                                          msg)

        if interaction_state != state:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(interaction_state, state))

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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.TOGGLE_STATE,
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
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)

        toggle_state = module.action(Property.Action.TOGGLE_STATE,
                                     Property.create_value_container(element=element),
                                     msg)

        if toggle_state != state:
            FlaUiError.raise_fla_ui_error(FlaUiError.PropertyNotEqual.format(toggle_state, state))

    @keyword
    def maximize_window(self, identifier, msg=None):
        """
        Maximize given window if supported.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |
        | Window could not be maximized                     |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Maximize Window  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Property.Action.MAXIMIZE_WINDOW,
                      Property.create_value_container(element=element),
                      msg)

    @keyword
    def minimize_window(self, identifier, msg=None):
        """
        Minimize given window if supported.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |
        | Window could not be minimized                     |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Minimize Window  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Property.Action.MINIMIZE_WINDOW,
                      Property.create_value_container(element=element),
                      msg)

    @keyword
    def normalize_window(self, identifier, msg=None):
        """
        Normalize given window if supported.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |
        | Window could not be normalized                    |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Normalize Window  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Property.Action.NORMALIZE_WINDOW,
                      Property.create_value_container(element=element),
                      msg)

    @keyword
    def can_window_be_maximized(self, identifier, msg=None):
        """
        Verifies if window can be maximized (True) if not False.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${result}  Can Window Be Maximized  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.CAN_WINDOW_MAXIMIZE,
                             Property.create_value_container(element=element),
                             msg)

    @keyword
    def can_window_be_minimized(self, identifier, msg=None):
        """
        Verifies if window can be minimized (True) if not False.

        XPaths syntax is explained in `XPath locator`.

        Possible FlaUI-Errors:
        | Element could not be found by xpath               |
        | Window pattern is not supported by given element  |

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | ${result}  Can Window Be Minimized  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        return module.action(Property.Action.CAN_WINDOW_MINIMIZE,
                             Property.create_value_container(element=element),
                             msg)
