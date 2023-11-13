# Changelog

All notable changes to Robotframework-FlaUI will be documented in this file. This project adheres
to [Semantic Versioning][].

This document follows the conventions laid out in [Keep a CHANGELOG][].

## [Unreleased][]

## [Release][2.1.0] [2.1.0][2.0.14-2.1.0] - 2023-11-13

### Added
- Python 3.12 Support
  - Release from Python.Net 3.0.2
- [#131](https://github.com/GDATASoftwareAG/robotframework-flaui/issues/131) New Keywords
  - Wait For Application While Busy By PID
  - Wait For Application While Busy By Name
  - Wait For Application Handle By Name
  - Wait For Application Handle By PID
- [#96](https://github.com/GDATASoftwareAG/robotframework-flaui/issues/96) New Keywords
  - Is Element Offscreen
  - Wait Until Element Is Offscreen

### Changed
- [#96](https://github.com/GDATASoftwareAG/robotframework-flaui/issues/96) Multiple Keywords renamed because of misleading keyword understanding
  - 'Wait Until Element Is Visible' to 'Wait Until Element Exist'
  - 'Wait Until Element Is Hidden' to 'Wait Until Element Does Not Exist'

## [Release][2.0.14] [2.0.14][2.0.13-2.0.14] - 2023-09-12

### Added
- Keyword 'Get Property From Element Keyword'
  - Add new operation 'VALUE'
  - Add new operation 'IS_SELECTED'

- [#118](https://github.com/GDATASoftwareAG/robotframework-flaui/issues/118)
  - Keyword 'Switch UIA To' implemented to change between UIA2 or UIA3
  - Keyword 'Close Application By Name' implemented to close application
  - Keyword 'Find All Elements' implemented to close application

- [#122](https://github.com/GDATASoftwareAG/robotframework-flaui/issues/122)
  - Whitelisting and blacklisting keywords implemented for screenshot library
    - Keywords can be whitelisted to persist if failed for example
      - BuiltIn.Run Keyword And Ignore Error should track always a screenshot
    - Keywords can be blacklisted to ignore by screenshot module
      - BuiltIn.Wait Until Keyword Succeeds to avoid unecessary screenshots
    - Blacklist is prioritize before Whitelist
  - New Keywords Clear Whitelist and Clear Blacklist

- Python.Net 3.0.2 support

### Bugfix
- [#117](https://github.com/GDATASoftwareAG/robotframework-flaui/issues/117) : Combobox will not restore into Collapsed state after calling 4 related keywords. 
  - Thanks to [JimRevolutionist](https://github.com/JimRevolutionist)

- [#119](https://github.com/GDATASoftwareAG/robotframework-flaui/issues/119) : Getting Duplicate screenshots when ever script is getting failed.

## [Release][2.0.13] [2.0.13][2.0.12-2.0.13] - 2023-07-25

### Bugfix
- Screenshot module removes invalid special characters from testcase name and hostname.
  - For example 'Test Case 1234: Something to Test'

## [Release][2.0.12] [2.0.12][2.0.11-2.0.12] - 2023-07-18

### Added
- Python 3.11 Support
- Keyword Get All Data From Grid implemented to get all data values includes header as list of arrays.
- Include additional Get Property From Element parameters
  - IS_VALUE_PATTERN_SUPPORTED
  - IS_READ_ONLY

## [Release][2.0.11] [2.0.11][2.0.10-2.0.11] - 2023-06-15

### Added
- Keyword Press Key and Press Keys contains now a delay in ms usage as parameter
    - Press Key  ${KEYBOARD_INPUT_TEXT}   ${XPATH_INPUT_FIELD}  200
    - Press Keys ${KEYBOARD_INPUT_SELECT_CUT_TEXT} ${XPATH_COMBO_BOX_INPUT}  500
    - If error message parameter is in usage this parameter will be interpreted as delay now
      - Recommendation to avoid such issues is to use msg key by any keyword
        - Press Key  ${KEYBOARD_INPUT_TEXT}   ${XPATH_INPUT_FIELD}  msg=Error Message
        - Press Keys ${KEYBOARD_INPUT_SELECT_CUT_TEXT} ${XPATH_COMBO_BOX_INPUT}  msg=Error Message

### Fixed

- Take Screenshot keyword will now persist manually created screenshots
    - Automatic screenshots by failures will be still deleted
    - Screenshots contains now a timestamp
      - Required if multiple test executions are triggered by seperated names for example UIA2 and UIA3 testing
      - Screenshot has to be copied after rebot merge because paths are relative to test execution folder
         - Example usage 
         - call rebot --name ATests --outputdir result -x rebot_xunit.xml result/uia2/output.xml result/uia3/output.xml
         - call xcopy .\result\uia2\screenshots .\result\screenshots\
         - call xcopy .\result\uia3\screenshots .\result\screenshots\

## [Release][2.0.10] [2.0.10][2.0.9-2.0.10] - 2023-05-31

### Added
- New Keyword implemented
    - Get Property From Element

## [Release][2.0.9] [2.0.9][2.0.8-2.0.9] - 2023-04-04

### Changed
- Adjustments in Setup.py for correct version handling

## [Release][2.0.8] [2.0.8][2.0.7-2.0.8] - 2023-04-04

### Added
- New Keyword implemented
    - Wait until Element Is Enabled

### Changed
- Bugfix to support Python 3.7 by missing requirements.txt

## [Release][2.0.7] [2.0.7][2.0.6-2.0.7] - 2023-03-30

### Added
- New Keywords for elements implemented
    - Element Should Be Enabled
    - Element Should Be Disabled

## [Release][2.0.6] [2.0.6][2.0.5-2.0.6] - 2023-03-20

### Added
- New Keywords for click and hold implemented
    - Maximize Window
    - Minimize Window
    - Normalize Window
    - Can Window Be Maximized
    - Can Window Be Minimized

## [Release][2.0.5] [2.0.5][2.0.4-2.0.5] - 2023-03-16

### Added
- New Keywords for click and hold implemented
    - Click Hold
    - Right Click Hold
    - Double Click Hold
    - Get Window Interaction State
    - Window Interaction State Should Be

## [Release][2.0.4] [2.0.4][2.0.3-2.0.4] - 2023-03-07

### Added
- New Should Be Keywords implemented
  - Background Color Should Be
  - Foreground Color Should Be
  - Font Size Should Be
  - Font Name Should Be
  - Font Weight Should Be
  - Culture Should Be
  - Window Visual State Should Be
  - Toggle State Should Be

## [Release][2.0.3] [2.0.3][2.0.2-2.0.3] - 2023-03-04

### Added
- New Keywords for toggle button handling implemented
  - Toggle
  - Get Toggle State

## [Release][2.0.2] [2.0.2][2.0.1-2.0.2] - 2023-02-23

### Added
- New Keywords implemented
  - Get Background Color
  - Get Foreground Color
  - Get Font Size
  - Get Font Name
  - Get Font Weight
  - Get Culture 
  - Is Hidden
  - Is Visible
  - Get Window Visual State

## [Release][2.0.1] [2.0.1][2.0.0-2.0.1] - 2022-10-06

### Updated
- Upgrade Python.Net to 3.0.1

## [Release][2.0.0] [2.0.0][1.7.3-2.0.0] - 2022-10-06

### Added
- Official Python 3.9 and 3.10 support

### Changed
- Test matrix update to python 3.8, 3.9 and 3.10 testing

### Updated
- FlaUI upgrade from 3.2.0 to 4.0
- Python.Net upgrade to 3.0

### Removed
- Python 3.6 support dropped

## [Release][1.7.3] [1.7.3][1.7.2-1.7.3] - 2022-03-28

### Added
- New Keywords Get Rectangle Bounding From Element
- Helper parsly.py xml parser implemented for old robotframework reporting xml generation for appveyor to avoid wrong amount of test numbers

### Removed
- LFS file parsly.exe removed by bfg history

## [Release][1.7.2] [1.7.2][1.7.1-1.7.2] - 2022-02-13

### Added
- New Keywords Expand Combobox and Collapse Combobox implemented for combobox

### Changed

- Select Combobox Item By Index selects now the given index value and collapsed the combox automatically.

### Updated

- Support for upcoming Robotframework 5.0


## [Release][1.7.1] [1.7.1][1.7-1.7.1] - 2022-02-07

### Added
- New Keyword implemented for listbox and combobox
  - Get All Selected Names From Combobox, Get All Texts From Combobox, Get All Texts From Listbox
    - Returns a list from all selected values by names

```
${data}  Get All Selected Texts From Combobox  <XPATH>
${data}  Get All Selected Names From Combobox  <XPATH>
${data}  Get All Texts From Listbox  <XPATH>
```

### Changed

- Keyword Get Selected Items From Combobox renamed to Get All Selected Texts From Combobox
  - Get All Selected Texts From Combobox returns a List not a String anymore
- Listbox Should Contain and Combobox Should Contain keywords checks now if Text or Name is equal by input value

## [Release][1.7] [1.7][1.6.6-1.7] - 2022-02-04

### Added

- New Keywords implemented for listbox and combobox
  - Get All Names From Listbox and Get All Names From Combobox returns both a list from all values by names
  - For a list comparison use Collections library from robotframework

```
${data}  Get All Names From Listbox  <XPATH>
${data}  Get All Names From Combobox  <XPATH>
```

### Updated

- Support for upcoming Python.Net 3.0

### Fixed

- Converter bugfix for wrong value convert
- Tree module refactoring

### Changed

#### New Element Should Exist or Element Should Not Exist Syntax

- Keyword behaviour changed for Element Should Exist and Element Should Not Exist
  - Keywords contains now a use_exceptions flag to decide if an exception should be called or a return value.
    - Exception handling will be used in general to check if a ui element is closing or opened
    - If you want to check it by your own use_exception flag should be set to ${FALSE}
      - Wait Until Keyword Succeeds combination does not work anymore to check if an ui is displaying after amount of time
      - Returns now always True or False

#### Old Style
```
# This throws a flaui exception and stop test exeuction
Element Should Exist  /WRONG/XPATH
```

- You can now decide to use the old syntax or new style by using the flag parameter use_exceptions.
- This is by default ${TRUE} to avoid this breaks for checkups if a ui element is displaying delayed.

#### New Style
```
# This throws a flaui exception and stop test exeuction
Element Should Exist      /WRONG/XPATH
Element Should Not Exist  /VALID_XPATH

# Usage with Wait Until Keyword Succeeds
Wait Until Keyword Succeeds 5x  1s  Element Should Exist      /VALID_XPATH
Wait Until Keyword Succeeds 5x  1s  Element Should Not Exist  /VALID_XPATH

# If you want to check the return value by your own syntax.
# Wait Until Keyword Succeeds will not work anymore because this keyword will always Return True or False now
${RESULT}  Element Should Exist  /VALID_XPATH  ${FALSE}
${RESULT}  Element Should Not Exist  /WRONG/XPATH  ${FALSE}
```

#### New Wait Until Element Is Hidden Syntax

- Wait Until Element Is Hidden does not check anymore if element exists
  - No xpath not found exception is called anymore to avoid break tests

#### New Application Syntax

- Application keyword modified for multi gui process handling
  - Launch Application, Launch Application With Args, Attach Application By Name or PID returns always a PID.
  - PID must be used by Close Application now to stop correct application  ${PID}
  - Old syntax stores only last started application
    - It was not possible to handle multiple application processes if needed
  - Unnecessary Keywords removed Attach To Application By Pid and Name
  - If application with a wrong pid will be tried to close a FlaUI exception will be called
  - Caller has always to close all applications by Teardown or Keywords

```
# Launch multiple applications
${PID_A}  Launch Application  APPLICATION_A
${PID_B}  Launch Application  APPLICATION_B
${PID_C}  Launch Application  APPLICATION_C
${PID_D}  Attach To Process By PID  ${PID}

# Close applications
Close Application  ${PID_C}
Close Application  ${PID_A}
Close Application  ${PID_B}
Close Application  ${PID_D}
```

## [Release][1.6.6] [1.6.6][1.6.5-1.6.6] - 2021-09-01

### Added

- Robotframework support for 4.1.1 and 4.1.3

### Changed

- Timeout behavior changed
  - "desktop.FindFirstByXPath(xpath)" needs a few seconds to finds element so retry which was default 
    10 times would break testing duration.
  - Retry is removed and sleep function can be disabled now with a "timeout=0"
  - If a timeout is set then this function will now waits the amount of time and check once and do not check 
    by a periodic timer anymore
  - Default timeout is still '1000 ms' to wait for an recheck if element could not be found

## [Release][1.6.5] [1.6.5][1.6.4-1.6.5] - 2021-08-28

### Changed

- Robotframework-flaui use now PythonLibCore 3.0 package to maintain this library
- Minimum required versions
    - Python >=3.6
    - Robotframework >=3.2.2
- See for more information
  PythonLibCore [documentation](https://github.com/robotframework/PythonLibCore/blob/master/docs/PythonLibCore-3.0.0.rst)

## [Release][1.6.4] [1.6.4][1.6.3-1.6.4] - 2021-07-20

### Added

- Robotframework 4.1 support

## [Release][1.6.3] [1.6.3][1.6.2-1.6.3] - 2021-05-26

### Added

- Robotframework 4.0.3 support

## [Release][1.6.2] [1.6.2][1.6.1-1.6.2] - 2021-05-12

### Added

- New keyword 'Wait Until Element Is Visible'
- New keyword 'Press Key'
- Robotframework 4.0.2 support

## [Release][1.6.1] [1.6.1][1.6-1.6.1] - 2021-05-05

### Added

- New keyword 'Drag And Drop'

### Changed

- Allow timeout parameter configuration as None or 0

## [Release][1.6] [1.6][1.5.1-1.6] - 2021-04-26

### Added

- New Keyword 'Launch Application With Args'
- Timeout handler implemented for FlaUI Library
- New set of keywords for Tree:
    - Get Selected TreeItems Name
    - Get Root TreeItems Count
    - Get All Visible TreeItems Count
    - Get All Visible TreeItems Names
    - Tree Should Contain
    - Select Visible TreeItem By Name
    - Select TreeItem
    - Selected TreeItem Should Be
    - Collapse All TreeItems
    - Expand All TreeItems
    - Expand TreeItem
    - Collapse TreeItem
    - TreeItem Should Be Visible

## [Release][1.5.1] [1.5.1][1.5-1.5.1] - 2021-04-09

### Updated

- Keyboard documentation improved by list usage example
- Robotframework 4.0.1 support

## [Release][1.5] [1.5][1.4-1.5] - 2021-03-11

### Added

- New keyword 'Select Listbox By Name' implemented
- Robotframework 4.0 support

## [Release][1.4] [1.4][1.3.6-1.4] - 2021-02-06

### Updated

- Python 3.9 support

## [Release][1.3.6] [1.3.6][1.3.5-1.3.6] - 2021-02-02

### Updated

- Robotframework 3.2.2 support

## [Release][1.3.5] [1.3.5][1.3.4-1.3.5] - 2021-01-25

### Added

- Support for UIA2 Windows Automation Interface

### Changed

- Get Element usage retries now automatic for one seconds if element will show up
    - Use case if a new window is open xpath usage will be too early to access element.


- Renamed flaui wrapper modules
    - ListView to Grid
    - ListControl to ListBox


- Renamed robotframework keyword module ListView to Grid and keywords
    - Get Selected Listview Rows --> Get Selected Grid Rows
    - Select Listview Row By Index --> Select Grid Row By Index
    - Select Listview Row By Name -->  Select Grid Row By Name
    - Get Listview Rows Count --> Get Grid Rows Count


- Pylint usage implemented
    - Include to keen.bat pylint
    - Appveyor pylint reporting


- Command line 'local_install.cmd' changed to 'keen.bat' with a set of supported build instructions
- Example ListView renamed to Grid

## [Release][1.3.4] [1.3.4][1.3.3-1.3.4] - 2020-06-23

General bugfixing from keywords and improvements from artifact building and testing

### Changed

- Keyword 'Set Radiobutton State' changed to 'Select Radiobutton'
- Change build system by python matrix testing for Python 3.7, 3.8 x86/x64 testing
- Documentation moved to documentation branch
- PyPi description modified
- Split up from release and develop dependencies by seperate requirements files
- Distribution which always forces a binary package with platform name

## [Release][1.3.3] [1.3.3][1.3.2-1.3.3] - 2020-08-24

### Added

- Python 3.8 support
- RFHUB .xml file documentation generation and include to all previous releases

### Changed

- Test cases rewrite by Custom Error Handling and Data Driven Tests
- Keyword documentation page contains now all .xml file documentation for RFHUB

## [Release][1.3.2] [1.3.2][1.3.1-1.3.2] - 2020-06-23

- Small upgrade to latest FlaUI release.

### Added

- FlaUI upgrade to version 3.2.0

## [Release][1.3.1] 1.3.1 - 2020-06-20

- First release from wrapper library Robotframework-FlaUI

### Added

- Automatic wheel package generation in appveyor and local builds
- Keyword documentation by [github.io][]
- Support for Python 3.7
- First release for supported flaui wrapper modules - Application, Checkbox, Combobox, Debug, Grid, Label, Listbox,
  Radiobuttion, Tab, Textbox, Windows, Keyboard, Mouse

[keep a changelog]: http://keepachangelog.com/

[semantic versioning]: http://semver.org/

[github.io]: https://gdatasoftwareag.github.io/robotframework-flaui

[unreleased]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.14...main

[2.1.0]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.1.0

[2.0.14-2.1.0]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.14...2.1.0

[2.0.14]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.14

[2.0.13-2.0.14]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.13...2.0.14

[2.0.13]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.13

[2.0.12-2.0.13]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.12...2.0.13

[2.0.12]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.12

[2.0.11-2.0.12]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.11...2.0.12

[2.0.11]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.11

[2.0.10-2.0.11]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.10...2.0.11

[2.0.10]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.10

[2.0.9-2.0.10]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.9...2.0.10

[2.0.9]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.9

[2.0.8-2.0.9]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.8...2.0.9

[2.0.8]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.8

[2.0.7-2.0.8]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.7...2.0.8

[2.0.7]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.7

[2.0.6-2.0.7]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.6...2.0.7

[2.0.6]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.6

[2.0.5-2.0.6]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.5...2.0.6

[2.0.5]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.5

[2.0.4-2.0.5]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.4...2.0.5

[2.0.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.4

[2.0.3-2.0.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.3...2.0.4

[2.0.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.3

[2.0.2-2.0.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.2...2.0.3

[2.0.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.2

[2.0.1-2.0.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.1...2.0.2

[2.0.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.1

[2.0.0-2.0.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/2.0.0...2.0.1

[2.0.0]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/2.0.0

[1.7.3-2.0.0]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.7.3...2.0.0

[1.7.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.7.3

[1.7.2-1.7.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.7.2...1.7.3

[1.7.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.7.2

[1.7.1-1.7.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.7.1...1.7.2

[1.7.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.7.1

[1.7-1.7.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.7...1.7.1

[1.7]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.7

[1.6.6-1.7]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.6.6...1.7

[1.6.6]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.6.6

[1.6.5-1.6.6]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.6.5...1.6.6

[1.6.5]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.6.5

[1.6.4-1.6.5]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.6.4...1.6.5

[1.6.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.6.4

[1.6.3-1.6.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.6.3...1.6.4

[1.6.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.6.3

[1.6.2-1.6.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.6.2...1.6.3

[1.6.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.6.2

[1.6.1-1.6.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.6.1...1.6.2

[1.6.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.6.1

[1.6-1.6.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.6...1.6.1

[1.6]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.6

[1.5.1-1.6]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.5.1...1.6

[1.5.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.5.1

[1.5-1.5.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.5...1.5.1

[1.5]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.5

[1.4-1.5]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.4...1.5

[1.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.4

[1.3.6-1.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.3.6...1.4

[1.3.6]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.6

[1.3.5-1.3.6]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.3.5...1.3.6

[1.3.5]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.5

[1.3.4-1.3.5]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.3.4...1.3.5

[1.3.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.4

[1.3.3-1.3.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.3.3...1.3.4

[1.3.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.3

[1.3.2-1.3.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.3.2...1.3.3

[1.3.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.2

[1.3.1-1.3.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/compare/1.3.1...1.3.2

[1.3.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.1
