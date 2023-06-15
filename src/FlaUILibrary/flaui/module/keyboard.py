import time
from enum import Enum
from typing import Optional, Any
from FlaUI.Core.Input import Keyboard as FlaUIKeyboard  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.util import KeyboardInputConverter
from FlaUILibrary.flaui.interface import (ModuleInterface, ValueContainer)
from FlaUILibrary.flaui.exception import FlaUiError


class Keyboard(ModuleInterface):
    """
    Keyboard control module wrapper for FlaUI usage.
    Wrapper module executes methods from Keyboard.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from keyboard module.
        """
        shortcut: Optional[str]
        shortcuts: Optional[list]
        delay_in_ms: Optional[int]

    class Action(Enum):
        """Supported actions for execute action implementation."""
        KEY_COMBINATION = "KEY_COMBINATION"
        KEYS_COMBINATIONS = "KEYS_COMBINATIONS"

    @staticmethod
    def create_value_container(shortcut=None, shortcuts=None, delay_in_ms=None):
        """
        Helper to create container object.

        Args:
            shortcut (String): Shortcut command to execute
            shortcuts (List): Shortcut commands to execute as list
            delay_in_ms (Number): Delay in ms to wait until key was pressed
        """
        return Keyboard.Container(shortcut=Converter.cast_to_string(shortcut),
                                  shortcuts=shortcuts,
                                  delay_in_ms=delay_in_ms)

    def execute_action(self, action: Action, values: Container):
        """If action is not supported an ActionNotSupported error will be raised.

        Supported action usages are:

            * Action.KEY_COMBINATION
              * Values ["shortcut"] : user defined string for shortcuts or chars.
              * Returns : None

            * Action.KEYS_COMBINATIONS
              * Values ["shortcuts"] : user defined sequence of shortcuts and text values.
              * Returns : None

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See supported action definitions for value usage.
        """

        switcher = {
            self.Action.KEYS_COMBINATIONS: lambda: self._type_keys_combinations(values["shortcuts"],
                                                                                values["delay_in_ms"]),
            self.Action.KEY_COMBINATION: lambda: self._type_key_combination(values["shortcut"],
                                                                            values["delay_in_ms"])
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _type_keys(keys: Any):
        """
        Sends multiple key controls.

        Args:
            keys (VirtualKeyShort array): Array from VirtualKeyShort usage to execute keyboard actions.
        """
        FlaUIKeyboard.TypeSimultaneously(keys)

    @staticmethod
    def _type_text(text: str):
        """
        Send input data from keyboard.

        Args:
            text (String): Input text from keyboard input.
        """
        FlaUIKeyboard.Type(text)

    @staticmethod
    def _type_key_combination(key_combination: Any, delay_in_ms: Any):
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

            if delay_in_ms:
                time.sleep(int(delay_in_ms) / 1000)

        except Exception as ex:
            raise FlaUiError.raise_fla_ui_error(str(ex))

    @staticmethod
    def _type_keys_combinations(keys_combination: Any, delay_in_ms: Any):
        """
        Parse a sequence of key controls.

        Args:
            keys_combination (String array): Array from String to execute keyboard actions or send input data.
        """
        if not isinstance(keys_combination, list):
            raise FlaUiError(FlaUiError.ArgumentShouldBeList)
        try:
            for key_combination in keys_combination:
                Keyboard._type_key_combination(key_combination, delay_in_ms)
        except Exception as ex:
            raise FlaUiError.raise_fla_ui_error(str(ex))
