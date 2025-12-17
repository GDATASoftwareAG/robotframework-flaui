import time
from enum import Enum
from typing import Optional, Any
from FlaUI.Core.Input import Keyboard as FlaUIKeyboard  # pylint: disable=import-error
from FlaUILibrary.flaui.util.converter import Converter
from FlaUILibrary.flaui.util.keyboardinputconverter import KeyboardInputConverter
from FlaUILibrary.flaui.interface.moduleinterface import ModuleInterface
from FlaUILibrary.flaui.interface.valuecontainer import ValueContainer
from FlaUILibrary.flaui.exception.flauierror import FlaUiError


class Keyboard(ModuleInterface):
    """
    Keyboard control module wrapper for FlaUI usage.
    Wrapper module executes methods from Keyboard.cs implementation.
    """

    class Container(ValueContainer):
        """
        Value container from keyboard module.
        """
        key_combination: Optional[str]
        key_combinations: Optional[list]
        delay_in_ms: Optional[int]
        press_only: Optional[bool]
        release_only: Optional[bool]

    class Action(Enum):
        """
        Supported actions for execute action implementation.
        """
        KEY_COMBINATION = "KEYBOARD_KEY_COMBINATION"
        KEYS_COMBINATIONS = "KEYBOARD_KEYS_COMBINATIONS"

    @staticmethod
    def create_value_container(key_combination=None,
                               key_combinations=None,
                               delay_in_ms=None,
                               press_only=False,
                               release_only=False) -> Container:
        """
        Helper to create container object.

        Args:
            key_combination (String): Key_combination command to execute
            key_combinations (List): Key combinations commands to execute as list
            delay_in_ms (Number): Delay in ms to wait until key was pressed
            press_only (Bool): Press key only without releasing
            release_only (Bool): Release key only without pressing
        """
        return Keyboard.Container(key_combination=Converter.cast_to_string(key_combination),
                                  key_combinations=key_combinations,
                                  delay_in_ms=delay_in_ms,
                                  press_only=press_only,
                                  release_only=release_only)

    def execute_action(self, action: Action, values: Container) -> Any:
        """
        If action is not supported an ActionNotSupported error will be raised.

        Raises:
            FlaUiError: If action is not supported.

        Args:
            action (Action): Action to use.
            values (Object): See action definitions for value usage.
        """

        switcher = {
        self.Action.KEYS_COMBINATIONS:
            lambda: self._type_keys_combinations(values),
        self.Action.KEY_COMBINATION:
            lambda: self._type_key_combination(values)
        }

        return switcher.get(action, lambda: FlaUiError.raise_fla_ui_error(FlaUiError.ActionNotSupported))()

    @staticmethod
    def _type_keys(keys: Any) -> None:
        """
        Send multiple virtual keys simultaneously.

        Args:
            keys (Any): Array or iterable of `VirtualKeyShort` values to send simultaneously.

        Notes:
            Uses FlaUI keyboard API to type key combinations at once.
        """
        FlaUIKeyboard.TypeSimultaneously(keys)

    @staticmethod
    def _type_text(text: str) -> None:
        """
        Send a string of text as keyboard input.

        Args:
            text (str): Text to send via keyboard input.
        """
        FlaUIKeyboard.Type(text)

    @staticmethod
    def _press_keys(key_shorts: Any) -> None:
        """
        Press (hold down) one or more keys without releasing them.

        Args:
            key_shorts (Any): Iterable of `VirtualKeyShort` values to press.
        """
        for key in key_shorts:
            FlaUIKeyboard.Press(key)

    @staticmethod
    def _release_keys(key_shorts: Any) -> None:
        """
        Release previously pressed keys.

        Args:
            key_shorts (Any): Iterable of `VirtualKeyShort` values to release.
        """
        for key in key_shorts:
            FlaUIKeyboard.Release(key)

    @staticmethod
    def _type_key_combination(container: Container) -> None:
        """
        Execute a single key combination or text input described in the container.

        Args:
            container (Keyboard.Container): Container holding:
                - container['shortcuts'] or container['shortcut']: The key or text to send.
                - container['delay_in_ms']: Optional delay after the action (milliseconds).
                - container['press_only']: If True, press keys only without releasing.
                - container['release_only']: If True, release keys only without pressing.

        Raises:
            FlaUiError: For invalid arguments, unsupported patterns (e.g., press/release for text),
                       or if underlying conversion/execution fails.
        """
        key_combination = container["key_combination"]
        delay_in_ms = container["delay_in_ms"]
        press_only = container['press_only']
        release_only = container['release_only']

        if isinstance(key_combination, list):
            raise FlaUiError(FlaUiError.ArgumentShouldNotBeList)
        try:
            action, converting_result = KeyboardInputConverter.convert_key_combination(key_combination)

            if action == KeyboardInputConverter.InputType.TEXT:
                if press_only or release_only:
                    raise FlaUiError(
                        FlaUiError.PatternNotSupported.format(" s'SOMEKEY' ") + \
                            " for key press_only and release_only events")

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
    def _type_keys_combinations(container: Container) -> None:
        """
        Execute a sequence of key combinations provided as a list.

        Args:
            container (Keyboard.Container): Container holding:
                - container['shortcuts']: List/array of key combination strings.
                - container['delay_in_ms']: Optional delay after each action (milliseconds).
                - container['press_only']: If True, press keys only without releasing.
                - container['release_only']: If True, release keys only without pressing.

        Raises:
            FlaUiError: If the provided `shortcuts` is not a list or on conversion/execution errors.
        """
        key_combinations = container["key_combinations"]
        delay_in_ms = container["delay_in_ms"]
        press_only = container['press_only']
        release_only = container['release_only']

        if not isinstance(key_combinations, list):
            raise FlaUiError(FlaUiError.ArgumentShouldBeList)

        try:
            for key_combination in key_combinations:
                container = Keyboard.create_value_container(
                    key_combination=key_combination,
                    delay_in_ms=delay_in_ms,
                    press_only=press_only,
                    release_only=release_only
                )

                Keyboard._type_key_combination(container)
        except Exception as ex:
            raise FlaUiError.raise_fla_ui_error(str(ex))
