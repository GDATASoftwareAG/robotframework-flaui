from re import split, match, search
from enum import Enum
from FlaUI.Core.WindowsAPI import VirtualKeyShort  # pylint: disable=import-error
from FlaUILibrary.flaui.exception import FlaUiError


class KeyboardInputConverter:
    """Helper class for simplifying keyboard input converting."""

    SHORTCUT = r'^s\'(.+?)\'$'
    TEXT = r'^t\'(.+?)\'$'
    SHORTCUT_DELIMITER = r'[+]'

    class InputType(Enum):
        """Supported input types."""
        TEXT = 0
        SHORTCUT = 1

    # Supported keyboard keys
    Keys = {
        "LBUTTON": VirtualKeyShort.LBUTTON,  # Left mouse button
        "RBUTTON": VirtualKeyShort.RBUTTON,  # Right mouse button
        "CANCEL": VirtualKeyShort.CANCEL,  # Control-break processing
        "MBUTTON": VirtualKeyShort.MBUTTON,  # Middle mouse button (three-button mouse)
        "XBUTTON1": VirtualKeyShort.XBUTTON1,  # Windows 2000/XP: X1 mouse button
        "XBUTTON2": VirtualKeyShort.XBUTTON2,  # Windows 2000/XP: X2 mouse button
        "BACK": VirtualKeyShort.BACK,  # BACKSPACE key
        "TAB": VirtualKeyShort.TAB,  # TAB key
        "CLEAR": VirtualKeyShort.CLEAR,  # CLEAR key
        "ENTER": VirtualKeyShort.ENTER,  # ENTER key
        "SHIFT": VirtualKeyShort.SHIFT,  # SHIFT key
        "CONTROL": VirtualKeyShort.CONTROL,  # CTRL key
        "CTRL": VirtualKeyShort.CONTROL,
        "ALT": VirtualKeyShort.ALT,
        "CAPITAL": VirtualKeyShort.CAPITAL,
        "PAUSE": VirtualKeyShort.PAUSE,
        "ESCAPE": VirtualKeyShort.ESCAPE,
        "ESC": VirtualKeyShort.ESCAPE,
        "CONVERT": VirtualKeyShort.CONVERT,  # IME convert
        "SPACE": VirtualKeyShort.SPACE,
        "PRIOR": VirtualKeyShort.PRIOR,  # PAGE UP key
        "NEXT": VirtualKeyShort.NEXT,  # PAGE DOWN key
        "END": VirtualKeyShort.END,
        "HOME": VirtualKeyShort.HOME,
        "LEFT": VirtualKeyShort.LEFT,  # LEFT ARROW key
        "RIGHT": VirtualKeyShort.RIGHT,  # RIGHT ARROW key
        "UP": VirtualKeyShort.UP,  # UP ARROW key
        "DOWN": VirtualKeyShort.DOWN,  # DOWN ARROW key
        "SELECT": VirtualKeyShort.SELECT,
        "PRINT": VirtualKeyShort.PRINT,
        "EXECUTE": VirtualKeyShort.EXECUTE,
        "SNAPSHOT": VirtualKeyShort.SNAPSHOT,  # PRINT SCREEN key
        "INSERT": VirtualKeyShort.INSERT,
        "DELETE": VirtualKeyShort.DELETE,
        "HELP": VirtualKeyShort.HELP,
        "0": VirtualKeyShort.KEY_0,
        "1": VirtualKeyShort.KEY_1,
        "2": VirtualKeyShort.KEY_2,
        "3": VirtualKeyShort.KEY_3,
        "4": VirtualKeyShort.KEY_4,
        "5": VirtualKeyShort.KEY_5,
        "6": VirtualKeyShort.KEY_6,
        "7": VirtualKeyShort.KEY_7,
        "8": VirtualKeyShort.KEY_8,
        "9": VirtualKeyShort.KEY_9,
        "A": VirtualKeyShort.KEY_A,
        "B": VirtualKeyShort.KEY_B,
        "C": VirtualKeyShort.KEY_C,
        "D": VirtualKeyShort.KEY_D,
        "E": VirtualKeyShort.KEY_E,
        "F": VirtualKeyShort.KEY_F,
        "G": VirtualKeyShort.KEY_G,
        "H": VirtualKeyShort.KEY_H,
        "I": VirtualKeyShort.KEY_I,
        "J": VirtualKeyShort.KEY_J,
        "K": VirtualKeyShort.KEY_K,
        "L": VirtualKeyShort.KEY_L,
        "M": VirtualKeyShort.KEY_M,
        "N": VirtualKeyShort.KEY_N,
        "O": VirtualKeyShort.KEY_O,
        "P": VirtualKeyShort.KEY_P,
        "Q": VirtualKeyShort.KEY_Q,
        "R": VirtualKeyShort.KEY_R,
        "S": VirtualKeyShort.KEY_S,
        "T": VirtualKeyShort.KEY_T,
        "U": VirtualKeyShort.KEY_U,
        "V": VirtualKeyShort.KEY_V,
        "W": VirtualKeyShort.KEY_W,
        "X": VirtualKeyShort.KEY_X,
        "Y": VirtualKeyShort.KEY_Y,
        "Z": VirtualKeyShort.KEY_Z,
        "LWIN": VirtualKeyShort.LWIN,
        "RWIN": VirtualKeyShort.RWIN,
        "APPS": VirtualKeyShort.APPS,
        "SLEEP": VirtualKeyShort.SLEEP,
        "MULTIPLY": VirtualKeyShort.MULTIPLY,  # '*'
        "ADD": VirtualKeyShort.ADD,  # '+'
        "SEPARATOR": VirtualKeyShort.SEPARATOR,
        "SUBTRACT": VirtualKeyShort.SUBTRACT,
        "DECIMAL": VirtualKeyShort.DECIMAL,
        "DIVIDE": VirtualKeyShort.DIVIDE,
        "F1": VirtualKeyShort.F1,
        "F2": VirtualKeyShort.F2,
        "F3": VirtualKeyShort.F3,
        "F4": VirtualKeyShort.F4,
        "F5": VirtualKeyShort.F5,
        "F6": VirtualKeyShort.F6,
        "F7": VirtualKeyShort.F7,
        "F8": VirtualKeyShort.F8,
        "F9": VirtualKeyShort.F9,
        "F10": VirtualKeyShort.F10,
        "F11": VirtualKeyShort.F11,
        "F12": VirtualKeyShort.F12
    }

    @staticmethod
    def convert_key_combination(key_combination):
        """
        Convert user-defined keys combination into text or VirtualKeyShort combination.

        Args:
            key_combination (String array): Array of Strings to execute keyboard actions.

        Raises:
            FlaUiError: If key_combination is invalid.

        Returns:
            Pair(Action, ConvertedValue): Action type (text or shortcut) and prepared value.
        """
        if match(KeyboardInputConverter.SHORTCUT, key_combination):

            (is_success, result) = KeyboardInputConverter._try_convert_to_shortcut(key_combination)

            if is_success:
                return KeyboardInputConverter.InputType.SHORTCUT, result

            return KeyboardInputConverter.InputType.TEXT, result

        if match(KeyboardInputConverter.TEXT, key_combination):
            return (KeyboardInputConverter.InputType.TEXT,
                    KeyboardInputConverter._extract_value_from_input(KeyboardInputConverter.TEXT,
                                                                     key_combination))

        raise FlaUiError.raise_fla_ui_error(FlaUiError.KeyboardInvalidKeysCombination.format(key_combination))

    @staticmethod
    def _try_convert_to_shortcut(key_combination: str):
        """
        Convert keys combination to shortcut.

        Args:
            key_combination (String): combination of keys to be converted to the shortcut.

        Returns:
            Tuple (convert_status, convert_result): z.B. (True, VirtualKeyShort Array), (False, String).
        """

        shortcut_keys = []
        extracted_key_combination = KeyboardInputConverter._extract_value_from_input(KeyboardInputConverter.SHORTCUT,
                                                                                     key_combination)

        keys = split(KeyboardInputConverter.SHORTCUT_DELIMITER,
                     extracted_key_combination)

        for key in keys:

            if key not in KeyboardInputConverter.Keys:
                return False, extracted_key_combination

            shortcut_keys.append(KeyboardInputConverter.Keys[key])

        return True, shortcut_keys

    @staticmethod
    def _extract_value_from_input(value_type, keyboard_input):
        """
        Extract input, which should be processed, from the following patterns:
        - s'CTRL+A'
        - t'Text to be processed'

        Args:
            value_type (KeyboardInputConverter.SHORTCUT or TEXT): expected value type.
            keyboard_input (String): Keyboard input in the format like s'<shortcut>' or t'<text>'.

        Raises:
            FlaUiError: If key_combination is impossible to extract.

        Returns:
            extracted_value (String): extracted from the input value.
        """

        value = search(value_type, keyboard_input)
        if value:
            return value.group(1)

        raise FlaUiError.raise_fla_ui_error(FlaUiError.KeyboardExtractionFailed)
