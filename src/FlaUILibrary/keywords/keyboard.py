from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.module import (Keyboard, Element)


class KeyboardKeywords:
    """
    Interface implementation from robotframework usage for keyboard keywords.
    """

    def __init__(self, module):
        """Constructor for element keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def press_keys(self, keys_combination, identifier=None, msg=None):
        """Keyboard control to execute a user defined sequence of shortcuts and text values.
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
        | Press Keys  t'Example text'  s'CTRL+A'  s'CTRL+C'  ${textbox_xpath} |
        | Press Keys  s'CTRL+A'  t'Overwrite text'                            |
        """
        if identifier is not None:
            self._module.action(Element.Action.FOCUS_ELEMENT, identifier, msg)

        self._module.action(Keyboard.Action.KEYS_COMBINATION, keys_combination, msg)
