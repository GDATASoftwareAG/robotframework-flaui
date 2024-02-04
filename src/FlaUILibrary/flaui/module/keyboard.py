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
        press_only: Optional[bool]
        release_only: Optional[bool]

    class Action(Enum):
        """Supported actions for execute action implementation."""
        KEY_COMBINATION = "KEY_COMBINATION"
        KEYS_COMBINATIONS = "KEYS_COMBINATIONS"

    @staticmethod
    def create_value_container(shortcut=None, shortcuts=None, delay_in_ms=None,
                               press_only=False, release_only=False):
        """
        Helper to create container object.

        Args:
            shortcut (String): Shortcut command to execute
            shortcuts (List): Shortcut commands to execute as list
            delay_in_ms (Number): Delay in ms to wait until key was pressed
            press_only (Bool): Press key only without releasing
            release_only (Bool): Release key only without pressing
        """
        return Keyboard.Container(shortcut=Converter.cast_to_string(shortcut),
                                  shortcuts=shortcuts,
                                  delay_in_ms=delay_in_ms,
                                  press_only=press_only,
                                  release_only=release_only)

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
                                                                            values["delay_in_ms"],
                                                                            values['press_only'],
                                                                            values['release_only']),
        self.Action.KEY_COMBINATION: lambda: self._type_key_combination(values["shortcut"],
                                                                        values["delay_in_ms"],
                                                                        values['press_only'],
                                                                        values['release_only'])
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
    def _press_keys(key_shorts: Any):
        """
        Send input data from keyboard. Press only without releasing keys.

        Args:
            key_shorts (VirtualKeyShort array): Array from VirtualKeyShort usage to execute keyboard actions.
        """
        for key in key_shorts:
            FlaUIKeyboard.Press(key)

    @staticmethod
    def _release_keys(key_shorts: Any):
        """
        Send input data from keyboard. Release only without pressing keys.

        Args:
            key_shortcuts (VirtualKeyShort array): Array from VirtualKeyShort usage to execute keyboard actions.
        """
        for key in key_shorts:
            FlaUIKeyboard.Release(key)

    @staticmethod
    def _type_key_combination(key_combination: Any, delay_in_ms: Any, 
                              press_only: bool, release_only: bool):
        """
        Execution of key control. 
        press_only and release_only supports keys only, not text.

        Args:
            key_combination (String): Array from String to execute keyboard actions or send input data.
            delay_in_ms (Number): Delay in ms to wait until key was pressed
            press_only (Bool): Press key only without releasing
            release_only (Bool): Release key only without pressing
        """
        if isinstance(key_combination, list):
            raise FlaUiError(FlaUiError.ArgumentShouldNotBeList)
        try:
            (action, converting_result) = KeyboardInputConverter.convert_key_combination(key_combination)
            if action == KeyboardInputConverter.InputType.TEXT:
                if press_only or release_only:
                    raise FlaUiError(
                        FlaUiError.PatternNotSupported.format(" s'SOMEKEY' ") + \
                            " for key press_only and release_only events")
                else:
                    Keyboard._type_text(converting_result)
            elif action == KeyboardInputConverter.InputType.SHORTCUT:
                if press_only:
                    Keyboard._press_keys(converting_result)
                elif release_only:
                    Keyboard._release_keys(converting_result)
                else:
                    Keyboard._type_keys(converting_result)

            if delay_in_ms:
                time.sleep(int(delay_in_ms) / 1000)

        except Exception as ex:
            raise FlaUiError.raise_fla_ui_error(str(ex))

    @staticmethod
    def _type_keys_combinations(keys_combination: Any, delay_in_ms: Any,
                                press_only: bool, release_only: bool):
        """
        Parse a sequence of key controls.

        Args:
            keys_combination (String array): Array from String to execute keyboard actions or send input data.
            delay_in_ms (Number): Delay in ms to wait until key was pressed
            press_only (Bool): Press key only without releasing
            release_only (Bool): Release key only without pressing
        """
        if not isinstance(keys_combination, list):
            raise FlaUiError(FlaUiError.ArgumentShouldBeList)
        try:
            for key_combination in keys_combination:
                Keyboard._type_key_combination(key_combination, delay_in_ms,
                                               press_only=press_only, 
                                               release_only=release_only
                                               )
        except Exception as ex:
            raise FlaUiError.raise_fla_ui_error(str(ex))
