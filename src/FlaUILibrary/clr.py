# pylint: disable=c-extension-no-member
import os
import clr

FLAUI_CORE_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'FlaUI.Core.dll')
FLAUI_UIA2_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'FlaUI.UIA2.dll')
FLAUI_UIA3_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'FlaUI.UIA3.dll')
INTEROP_DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'Interop.UIAutomationClient.dll')

clr.AddReference(FLAUI_CORE_DLL_PATH)
clr.AddReference(FLAUI_UIA2_DLL_PATH)
clr.AddReference(FLAUI_UIA3_DLL_PATH)
clr.AddReference(INTEROP_DLL_PATH)

clr.AddReference("System")
clr.AddReference("FlaUI.Core")
clr.AddReference("FlaUI.UIA2")
clr.AddReference("FlaUI.UIA3")
clr.AddReference("Interop.UIAutomationClient")
