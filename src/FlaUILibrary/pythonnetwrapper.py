# pylint: disable=c-extension-no-member
# pylint: disable=no-member

import os
import clr

FLAUI_CORE_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'FlaUI.Core.dll')
FLAUI_UIA2_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'FlaUI.UIA2.dll')
FLAUI_UIA3_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'FlaUI.UIA3.dll')
INTEROP_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'Interop.UIAutomationClient.dll')
SYSTEM_CODE_DOME_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'System.CodeDom.dll')
SAFE_XPATH_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'FlaUiNative.dll')


clr.AddReference(FLAUI_CORE_DLL_PATH)
clr.AddReference(FLAUI_UIA2_DLL_PATH)
clr.AddReference(FLAUI_UIA3_DLL_PATH)
clr.AddReference(INTEROP_DLL_PATH)
clr.AddReference(SYSTEM_CODE_DOME_DLL_PATH)
clr.AddReference(SAFE_XPATH_DLL_PATH)

clr.AddReference("System")
clr.AddReference("FlaUI.Core")
clr.AddReference("FlaUI.UIA2")
clr.AddReference("FlaUI.UIA3")
clr.AddReference("Interop.UIAutomationClient")
clr.AddReference("System.CodeDom")
clr.AddReference("FlaUiNative")

from System.Reflection import Assembly, BindingFlags  # pylint: disable=import-error,wrong-import-position

_SAFE_XPATH_TYPE = Assembly.LoadFrom(SAFE_XPATH_DLL_PATH).GetType("FlaUiNative.SafeXPath")
_INVOKE_STATIC = BindingFlags.InvokeMethod | BindingFlags.Public | BindingFlags.Static


class SafeXPath:  # pylint: disable=invalid-name
    """Wrapper for FlaUiNative.SafeXPath static methods."""

    @staticmethod
    def FindFirstByXPath(element, xpath):
        """Find the first automation element matching xpath."""
        return _SAFE_XPATH_TYPE.InvokeMember(
            "FindFirstByXPath", _INVOKE_STATIC, None, None, [element, xpath]
        )

    @staticmethod
    def FindAllByXPath(element, xpath):
        """Find all automation elements matching xpath."""
        return _SAFE_XPATH_TYPE.InvokeMember(
            "FindAllByXPath", _INVOKE_STATIC, None, None, [element, xpath]
        )
