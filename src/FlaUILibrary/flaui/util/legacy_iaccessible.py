from typing import Any, Optional
from FlaUI.Core import FrameworkAutomationElementBase  # pylint: disable=import-error
from FlaUI.Core.WindowsAPI import AccessibilityState  # pylint: disable=import-error
from FlaUI.Core.Exceptions import NotSupportedByFrameworkException  # pylint: disable=import-error
from FlaUILibrary.flaui.exception.flauierror import FlaUiError
from FlaUILibrary.flaui.util.converter import Converter


class LegacyIAccessibleProperties:
    """
    Helper to read LegacyIAccessible pattern properties from automation elements.
    """

    @staticmethod
    def is_supported(element: Any) -> bool:
        """
        Check whether the LegacyIAccessible pattern is supported by the element.

        Args:
            element (Any): Automation element to query.

        Returns:
            bool: True if LegacyIAccessible pattern is supported, False otherwise.
        """
        try:
            patterns = LegacyIAccessibleProperties._get_legacy_iaccessible_patterns(element)
            if patterns is None:
                return False
            return Converter.cast_to_bool(patterns.LegacyIAccessible.IsSupported)
        except NotSupportedByFrameworkException:
            return False

    @staticmethod
    def get_state(element: Any) -> str:
        """
        Return the LegacyIAccessible state flags as a string.

        Args:
            element (Any): Automation element supporting LegacyIAccessible pattern.

        Returns:
            str: LegacyIAccessible state flags (for example expanded or collapsed).
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        state = LegacyIAccessibleProperties._get_automation_property(pattern, "State")
        return str(state)

    @staticmethod
    def get_role(element: Any) -> str:
        """
        Return the LegacyIAccessible role of the element as a string.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        role = LegacyIAccessibleProperties._get_automation_property(pattern, "Role")
        return str(role)

    @staticmethod
    def get_name(element: Any) -> str:
        """
        Return the LegacyIAccessible name of the element as a string.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        name = LegacyIAccessibleProperties._get_automation_property(pattern, "Name")
        if name is not None:
            return str(name)
        return ""

    @staticmethod
    def get_value(element: Any) -> str:
        """
        Return the LegacyIAccessible value of the element as a string.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        value = LegacyIAccessibleProperties._get_automation_property(pattern, "Value")
        if value is not None:
            return str(value)
        return ""

    @staticmethod
    def get_default_action(element: Any) -> str:
        """
        Return the LegacyIAccessible default action of the element as a string.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        default_action = LegacyIAccessibleProperties._get_automation_property(pattern, "DefaultAction")
        if default_action is not None:
            return str(default_action)
        return ""

    @staticmethod
    def get_description(element: Any) -> str:
        """
        Return the LegacyIAccessible description of the element as a string.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        description = LegacyIAccessibleProperties._get_automation_property(pattern, "Description")
        if description is not None:
            return str(description)
        return ""

    @staticmethod
    def get_help(element: Any) -> str:
        """
        Return the LegacyIAccessible help text of the element as a string.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        help_text = LegacyIAccessibleProperties._get_automation_property(pattern, "Help")
        if help_text is not None:
            return str(help_text)
        return ""

    @staticmethod
    def get_keyboard_shortcut(element: Any) -> str:
        """
        Return the LegacyIAccessible keyboard shortcut of the element as a string.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        keyboard_shortcut = LegacyIAccessibleProperties._get_automation_property(pattern, "KeyboardShortcut")
        if keyboard_shortcut is not None:
            return str(keyboard_shortcut)
        return ""

    @staticmethod
    def get_child_id(element: Any) -> str:
        """
        Return the LegacyIAccessible child id of the element as a string.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        child_id = LegacyIAccessibleProperties._get_automation_property(pattern, "ChildId")
        return str(child_id)

    @staticmethod
    def is_expanded(element: Any) -> bool:
        """
        Return whether the LegacyIAccessible state contains STATE_SYSTEM_EXPANDED.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        state = LegacyIAccessibleProperties._get_automation_property(pattern, "State")
        return Converter.cast_to_bool(state.HasFlag(AccessibilityState.STATE_SYSTEM_EXPANDED))

    @staticmethod
    def is_collapsed(element: Any) -> bool:
        """
        Return whether the LegacyIAccessible state contains STATE_SYSTEM_COLLAPSED.
        """
        pattern = LegacyIAccessibleProperties._get_pattern(element)
        state = LegacyIAccessibleProperties._get_automation_property(pattern, "State")
        return Converter.cast_to_bool(state.HasFlag(AccessibilityState.STATE_SYSTEM_COLLAPSED))

    @staticmethod
    def _get_legacy_iaccessible_patterns(element: Any) -> Optional[Any]:
        """
        Retrieve framework patterns with LegacyIAccessible support from an element.

        Python.NET requires casting to IFrameworkPatterns to access LegacyIAccessible.
        Returns None when the active framework (for example UIA2) does not support the pattern.
        """
        try:
            patterns = FrameworkAutomationElementBase.IFrameworkPatterns(element.Patterns)
            _ = patterns.LegacyIAccessible
            return patterns
        except NotSupportedByFrameworkException:
            return None

    @staticmethod
    def _get_pattern(element: Any) -> Any:
        """
        Retrieve the LegacyIAccessible pattern instance from the element.
        """
        patterns = LegacyIAccessibleProperties._get_legacy_iaccessible_patterns(element)
        if patterns is not None and LegacyIAccessibleProperties.is_supported(element):
            pattern = patterns.LegacyIAccessible.Pattern
            if pattern is not None:
                return pattern

        raise FlaUiError(FlaUiError.PatternNotSupported.format("LegacyIAccessible"))

    @staticmethod
    def _get_automation_property(pattern: Any, property_name: str) -> Any:
        """
        Read a LegacyIAccessible automation property value from a pattern.
        """
        automation_property = getattr(pattern, property_name)
        return automation_property.Value
