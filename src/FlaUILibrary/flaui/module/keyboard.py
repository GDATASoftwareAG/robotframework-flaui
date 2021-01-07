from enum import Enum
from FlaUI.Core.Input import Keyboard as FlaUIKeyboard  # pylint: disable=import-error
from FlaUILibrary.flaui.util import KeyboardInputConverter
from FlaUILibrary.flaui.interface import ModuleInterface
from FlaUILibrary.flaui.exception import FlaUiError


class Keyboard(ModuleInterface):
    """
    Keyboard control module wrapper for FlaUI usage.
    Wrapper module executes methods from Keyboard.cs implementation.
    """

    class Action(Enum):
        """Supported actions for execute action implementation."""
        KEYS_COMBINATION = "KEYS_COMBINATION"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

            * Action.KEYS_COMBINATION
              * Values (Object) : UI entity object from UIA3 to set input
              * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.KEYS_COMBINATION: lambda: Keyboard._type_keys_combination(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _type_keys(keys):
        """
        Sends multiple key controls.

        Args:
            keys (VirtualKeyShort array): Array from VirtualKeyShort usage to execute keyboard actions.
        """
        FlaUIKeyboard.TypeSimultaneously(keys)

    @staticmethod
    def _type_text(text):
        """
        Send input data from keyboard.

        Args:
            text (String): Input text from keyboard input.
        """
        FlaUIKeyboard.Type(str(text))

    @staticmethod
    def _type_keys_combination(keys_combination):
        """
        Parse a sequence of key controls.

        Args:
            keys_combination (String array): Array from String to execute keyboard actions or send input data.
        """
        try:
            for key_combination in keys_combination:

                (action, converting_result) = KeyboardInputConverter.convert_key_combination(key_combination)

                if action == KeyboardInputConverter.InputType.TEXT:
                    Keyboard._type_text(converting_result)
                elif action == KeyboardInputConverter.InputType.SHORTCUT:
                    Keyboard._type_keys(converting_result)

        except Exception as ex:
            raise FlaUiError.raise_fla_ui_error(str(ex))
