# pylint: disable=invalid-name
from enum import Enum
from robot.libraries.BuiltIn import BuiltIn
from FlaUILibrary import version, clr
from FlaUILibrary.keywords import (ApplicationKeywords,
                                   CheckBoxKeywords,
                                   ComboBoxKeywords,
                                   DebugKeywords,
                                   ElementKeywords,
                                   MouseKeywords,
                                   KeyboardKeywords,
                                   ScreenshotKeywords,
                                   TextBoxKeywords,
                                   WindowKeywords,
                                   GridKeywords,
                                   RadioButtonKeywords,
                                   ListBoxKeywords,
                                   TabKeywords)
from FlaUILibrary.robotframework import DynamicCore, robotlog
from FlaUILibrary.flaui import (UIA2, UIA3)
from FlaUILibrary.flaui.module import Screenshot


# pylint: enable=invalid-name
class FlaUILibrary(DynamicCore):
    """FlaUILibrary is a Robot Framework library for automating Windows GUI.

    It is a wrapper for [https://github.com/Roemer/FlaUI | FlaUI] automation framework, which is based based on
    native UI Automation libraries from Microsoft and therefore kind of a wrapper around them.

    = Getting started =

    FlaUILibrary uses XPath item identifiers to gain access to user interface components like windows, buttons, textbox
    etc.

    == Library screenshot usage ==

    FlaUiLibrary contains by default a automatic snapshot module which creates for each error case a snapshot from a
    attached element or desktop. To disable this feature use Library  screenshot_enabled=False.

    Following settings could be used for library init.

    Library  screenshot_enabled=<True/False>  screenshot_dir=<PATH_TO_STORE_IMAGES>

    == XPath locator ==

    An XPath is a tree overview from all active module application like a Taskbar or Windows (Outlook, Security Client).
    FlaUILibrary supports to interact with this XPath to select this module components by a AutomationId, Name,
    ClassName or HelpText.

    XPath identifier usage examples:
    | = Attribute = | = Description = | = Example = |
    | AutomationId  | Search for element with given automation id | /MenuBar/MenuItem[@AutomationId='<ID>'] |
    | Name  | Search for element with given name | /MenuBar/MenuItem[@Name='<NAME>'] |
    | ClassName  | Search for element with given class type | /MenuBar/MenuItem[@ClassName='<CLASS_NAME>'] |
    | HelpText  |  Search for element with given help text | /MenuBar/MenuItem[@HelpText='<HELP_TEXT>'] |

    For FlaUI there is a inspector tool [https://github.com/FlauTech/FlaUInspect | FlaUI Inspect] to verify an XPath
    from all visible UI components. Download the latest release and set UIA3 Mode and enable 'Show XPath' under mode.

    """
    ROBOT_LIBRARY_VERSION = version.VERSION
    ROBOT_LIBRARY_SCOPE = "Global"
    ROBOT_LISTENER_API_VERSION = 2

    class RobotMode(Enum):
        """Actual state from test execution by robot framework."""
        TEST_NOT_RUNNING = 1
        TEST_RUNNING = 2

    class KeywordModules(Enum):
        """Enumeration from all supported keyword modules."""
        APPLICATION = "Application"
        CHECKBOX = "Checkbox"
        COMBOBOX = "Combobox"
        DEBUG = "Debug"
        ELEMENT = "Element"
        GRID = "Grid"
        MOUSE = "Mouse"
        KEYBOARD = "Keyboard"
        SCREENSHOT = "Screenshot"
        TEXTBOX = "Textbox"
        WINDOW = "Window"
        RADIOBUTTON = "Radiobutton"
        LISTBOX = "Listbox"
        TAB = "Tab"

    def __init__(self, uia='UIA3', screenshot_on_failure='True', screenshot_dir=None):
        """FlaUiLibrary can be imported by following optional arguments:

        ``uia`` Microsoft UI-Automation framework to use. UIA2 or UIA3
        ``screenshot_on_failure`` indicator to disable or enable screenshot feature.
        ``screenshot_dir`` is the directory where screenshots are saved.

        If the given directory does not already exist, it will be created when the first screenshot is taken.
        If the argument is not given, the default location for screenshots is the output directory of the Robot run,
        i.e. the directory where output and log files are generated.
        """
        # FlaUI init
        self.mode = FlaUILibrary.RobotMode.TEST_NOT_RUNNING
        self.builtin = BuiltIn()
        if uia == "UIA2":
            self.module = UIA2()
        else:
            self.module = UIA3()

        self.screenshots = Screenshot(screenshot_dir, screenshot_on_failure == 'True')

        self.keyword_modules = {
            FlaUILibrary.KeywordModules.APPLICATION: ApplicationKeywords(self.module),
            FlaUILibrary.KeywordModules.CHECKBOX: CheckBoxKeywords(self.module),
            FlaUILibrary.KeywordModules.COMBOBOX: ComboBoxKeywords(self.module),
            FlaUILibrary.KeywordModules.DEBUG: DebugKeywords(self.module),
            FlaUILibrary.KeywordModules.ELEMENT: ElementKeywords(self.module),
            FlaUILibrary.KeywordModules.GRID: GridKeywords(self.module),
            FlaUILibrary.KeywordModules.MOUSE: MouseKeywords(self.module),
            FlaUILibrary.KeywordModules.KEYBOARD: KeyboardKeywords(self.module),
            FlaUILibrary.KeywordModules.SCREENSHOT: ScreenshotKeywords(self.module, self.screenshots),
            FlaUILibrary.KeywordModules.TEXTBOX: TextBoxKeywords(self.module),
            FlaUILibrary.KeywordModules.WINDOW: WindowKeywords(self.module),
            FlaUILibrary.KeywordModules.RADIOBUTTON: RadioButtonKeywords(self.module),
            FlaUILibrary.KeywordModules.LISTBOX: ListBoxKeywords(self.module),
            FlaUILibrary.KeywordModules.TAB: TabKeywords(self.module),
        }

        # Robot init
        self.ROBOT_LIBRARY_LISTENER = self  # pylint: disable=invalid-name
        self.libraries = self.keyword_modules.values()
        DynamicCore.__init__(self, self.libraries)

    def _start_test(self, name, attrs):  # pylint: disable=unused-argument
        self.mode = FlaUILibrary.RobotMode.TEST_RUNNING
        self.screenshots.name = name.replace(" ", "_").lower()
        self.screenshots.execute_action(Screenshot.Action.RESET)

    def _end_test(self, name, attrs): # pylint: disable=unused-argument
        self.mode = FlaUILibrary.RobotMode.TEST_NOT_RUNNING
        if attrs['status'] == 'PASS' and self.screenshots.is_enabled:
            if not self.screenshots.execute_action(Screenshot.Action.DELETE_ALL_SCREENSHOTS):
                robotlog.log("Not all files were deleted")

    def _end_keyword(self, name, attrs):  # pylint: disable=unused-argument
        if attrs['status'] == 'FAIL' \
                and self.mode == FlaUILibrary.RobotMode.TEST_RUNNING \
                and self.screenshots.is_enabled:
            # Keyword usage here to include to robot reporting log
            self.keyword_modules[FlaUILibrary.KeywordModules.SCREENSHOT].take_screenshot()
