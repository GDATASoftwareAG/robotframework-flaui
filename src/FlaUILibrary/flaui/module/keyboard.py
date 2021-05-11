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
        KEY_COMBINATION = "KEY_COMBINATION"
        KEYS_COMBINATIONS = "KEYS_COMBINATIONS"

    def execute_action(self, action, values=None):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

            * Action.KEY_COMBINATION
              * Values (String) : user defined string for shortcuts or chars.
              * Returns : None

            * Action.KEYS_COMBINATIONS
              * Values (String Array) : user defined sequence of shortcuts and text values.
              * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.KEYS_COMBINATIONS: lambda: Keyboard._type_keys_combinations(values),
            self.Action.KEY_COMBINATION: lambda: Keyboard._type_key_combination(values)
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
    def _type_key_combination(key_combination):
        """
        Execution of key control.

        Args:
            key_combination (String): Array from String to execute keyboard actions or send input data.
        """
        if isinstance(key_combination, list):
            raise FlaUiError(FlaUiError.ArgumentShouldNotBeList)
        try:
            (action, converting_result) = KeyboardInputConverter.convert_key_combination(key_combination)
            if action == KeyboardInputConverter.InputType.TEXT:
                Keyboard._type_text(converting_result)
            elif action == KeyboardInputConverter.InputType.SHORTCUT:
                Keyboard._type_keys(converting_result)
        except Exception as ex:
            raise FlaUiError.raise_fla_ui_error(str(ex))

    @staticmethod
    def _type_keys_combinations(keys_combination):
        """
        Parse a sequence of key controls.

        Args:
            keys_combination (String array): Array from String to execute keyboard actions or send input data.
        """
        if not isinstance(keys_combination, list):
            raise FlaUiError(FlaUiError.ArgumentShouldBeList)
        try:
            for key_combination in keys_combination:
                Keyboard._type_key_combination(key_combination)
        except Exception as ex:
            raise FlaUiError.raise_fla_ui_error(str(ex))
