from robotlibcore import keyword
from FlaUILibrary.flaui.module import (Keyboard, Element)


class KeyboardKeywords:
    """
    Interface implementation from robotframework usage for keyboard keywords.
    """

    def __init__(self, module):
        """
        Constructor for element keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def press_key(self, key_combination, identifier=None, msg=None):
        """
        Keyboard control to execute a user defined one shurcut or text.
        If identifier set try to attach to given element if
        operation was successfully old element will be reattached automatically.

        Arguments:
        | Argument         | Type                                  | Description                   |
        | keys_combination | List of Strings, which should         | Text to be typed by keyboard  |
        |                  | satisfy one of the following formats: |                               |
        |                  |    - s'<shortcut>'                    |                               |
        |                  |    - t'<text>'                        |                               |
        |                  |    Examples:                          |                               |
        |                  |    - s'CTRL+A'                        |                               |
        |                  |    - t'JJJ'                           |                               |
        |                  |    - s'JJJ' will be executed as text  |                               |
        | identifier       | String *Optional                      | Optional XPath identifier     |
        | msg              | String *Optional                      | Custom error message          |

        XPath syntax is explained in `XPath locator`.

        The following keys are supported for usage as a part of key_combination:
        | LBUTTON     |     Left mouse button                           |
        | RBUTTON     |     Right mouse button                          |
        | CANCEL      |     Control-break processing                    |
        | MBUTTON     |     Middle mouse button (three-button mouse)    |
        | XBUTTON1    |     Windows 2000/XP: X1 mouse button            |
        | XBUTTON2    |     Windows 2000/XP: X2 mouse button            |
        | BACK        |     BACKSPACE key                               |
        | TAB         |     TAB key                                     |
        | CLEAR       |     CLEAR key                                   |
        | ENTER       |     ENTER key                                   |
        | SHIFT       |     SHIFT key                                   |
        | CTRL        |     CTRL key                                    |
        | ALT         |     ALT key                                     |
        | CAPITAL     |     CAPITAL key                                 |
        | PAUSE       |     PAUSE key                                   |
        | ESCAPE      |     ESC key                                     |
        | ESC         |     ESC key                                     |
        | SPACE       |     Blank space key                             |
        | NEXT        |     Next key                                    |
        | END         |     END key                                     |
        | HOME        |     HOME key                                    |
        | LEFT        |     LEFT ARROW key                              |
        | RIGHT       |     RIGHT ARROW key                             |
        | UP          |     UP ARROW key                                |
        | DOWN        |     DOWN ARROW key                              |
        | SELECT      |     SELECT key                                  |
        | PRINT       |     PRINT key                                   |
        | EXECUTE     |     EXEC key                                    |
        | INSERT      |     INS key                                     |
        | DELETE      |     DEL key                                     |
        | HELP        |     HELP key                                    |
        | 0 - 9       |                                                 |
        | A - Z       |                                                 |
        | F1 - F12    |                                                 |
        | LWIN        |     Left Windows key                            |
        | RWIN        |     Right Windows key                           |
        | APPS        |                                                 |
        | SLEEP       |                                                 |
        | MULTIPLY    |     '*' key                                     |
        | ADD         |     '+' key                                     |
        | SEPARATOR   |                                                 |
        | SUBTRACT    |                                                 |
        | DECIMAL     |                                                 |
        | DIVIDE      |                                                 |

        Example:

        | ***** Variables *****                                         |
        | ${KEYBOARD_INPUT_CUT}  s'CTRL+X'                              |
        |                                                               |
        | ***** Test Cases *****                                        |
        | ...Keyboard usage in Test Case...                             |
        | Press Key  s'CTRL'    ${XPATH_COMBO_BOX_INPUT}                |
        | Press Key  t'A'       ${XPATH_COMBO_BOX_INPUT}                |
        | Press Key  s'CTRL+A'  ${XPATH_COMBO_BOX_INPUT}                |
        | Press Key  ${KEYBOARD_INPUT_CUT}    ${XPATH_COMBO_BOX_INPUT}  |
        """
        if identifier is not None:
            self._module.action(Element.Action.FOCUS_ELEMENT,
                                Element.Container(xpath=identifier, retries=None, name=None),
                                msg)

        self._module.action(Keyboard.Action.KEY_COMBINATION,
                            Keyboard.create_value_container(shortcut=key_combination),
                            msg)

    @keyword
    def press_keys(self, keys_combinations, identifier=None, msg=None):
        """
        Keyboard control to execute a user defined sequence of shortcuts and text values.
        If identifier set try to attach to given element if
        operation was successfully old element will be reattached automatically.

        Arguments:
        | Argument         | Type                                  | Description                   |
        | keys_combination | List of Strings, which should         | Text to be typed by keyboard  |
        |                  | satisfy one of the following formats: |                               |
        |                  |    - s'<shortcut>'                    |                               |
        |                  |    - t'<text>'                        |                               |
        |                  |    Examples:                          |                               |
        |                  |    - s'CTRL+A'                        |                               |
        |                  |    - t'JJJ'                           |                               |
        |                  |    - s'JJJ' will be executed as text  |                               |
        | identifier       | String *Optional                      | Optional XPath identifier     |
        | msg              | String *Optional                      | Custom error message          |

        XPath syntax is explained in `XPath locator`.

        The list of all key_combinations can be seen under Press Key keyword.
        The only difference between both keywords is:
        Press Keys supports a sequence of several to be pressed after each other
        Press Key supports can only press one key combination at a time

        Example:
        | ***** Variables *****                                                 |
        | @{KEYBOARD_INPUT_SELECT_CUT_TEXT} s'CTRL+A' s'CTRL+X'                 |
        |                                                                       |
        | ***** Test Cases *****                                                |
        | ...Keyboard usage in Test Case...                                     |
        | Press Keys ${KEYBOARD_INPUT_SELECT_CUT_TEXT} ${XPATH_COMBO_BOX_INPUT} |
        """
        if identifier is not None:
            self._module.action(Element.Action.FOCUS_ELEMENT,
                                Element.Container(xpath=identifier, retries=None, name=None),
                                msg)

        self._module.action(Keyboard.Action.KEYS_COMBINATIONS,
                            Keyboard.create_value_container(shortcuts=keys_combinations),
                            msg)
