# Changelog

All notable changes to Robotframework-FlaUI will be documented in this file. This
project adheres to [Semantic Versioning][].

This document follows the conventions laid out in [Keep a CHANGELOG][].
## [Unreleased][]

### Added
-    New keyword 'Wait Until Element Is Visible'

## [Release][1.6.1] [1.6.1][1.6-1.6.1] - 2021-05-05

### Added
-    New keyword 'Drag And Drop'

### Changed
-    Allow timeout parameter configuration as None or 0

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
-    Keyboard documentation improved by list usage example
-    Robotframework 4.0.1 support

## [Release][1.5] [1.5][1.4-1.5] - 2021-03-11

### Added
-    New keyword 'Select Listbox By Name' implemented
-    Robotframework 4.0 support

## [Release][1.4] [1.4][1.3.6-1.4] - 2021-02-06

### Updated
-    Python 3.9 support

## [Release][1.3.6] [1.3.6][1.3.5-1.3.6] - 2021-02-02

### Updated
-    Robotframework 3.2.2 support

## [Release][1.3.5] [1.3.5][1.3.4-1.3.5] - 2021-01-25

### Added
-    Support for UIA2 Windows Automation Interface

### Changed

-   Get Element usage retries now automatic for one seconds if element will show up
    - Use case if a new window is open xpath usage will be too early to access element.


-   Renamed flaui wrapper modules
    - ListView to Grid
    - ListControl to ListBox
    

-   Renamed robotframework keyword module ListView to Grid and keywords
    - Get Selected Listview Rows --> Get Selected Grid Rows
    - Select Listview Row By Index --> Select Grid Row By Index
    - Select Listview Row By Name -->  Select Grid Row By Name
    - Get Listview Rows Count --> Get Grid Rows Count
    

-   Pylint usage implemented
      - Include to keen.bat pylint
      - Appveyor pylint reporting
    

-   Command line 'local_install.cmd' changed to 'keen.bat' with a set of supported build instructions
-   Example ListView renamed to Grid

## [Release][1.3.4] [1.3.4][1.3.3-1.3.4] - 2020-06-23

General bugfixing from keywords and improvements from artifact building and testing

### Changed

 -  Keyword 'Set Radiobutton State' changed to 'Select Radiobutton'
 -  Change build system by python matrix testing for Python 3.7, 3.8 x86/x64 testing
 -  Documentation moved to documentation branch
 -  PyPi description modified
 -  Split up from release and develop dependencies by seperate requirements files
 -  Distribution which always forces a binary package with platform name

## [Release][1.3.3] [1.3.3][1.3.2-1.3.3] - 2020-08-24

Upgrade from Pythonet dependency to support Python 3.8.

### Added

-   Python 3.8 support
-   RFHUB .xml file documentation generation and include to all previous releases

### Changed

-  Test cases rewrite by Custom Error Handling and Data Driven Tests
-  Keyword documentation page contains now all .xml file documentation for RFHUB

## [Release][1.3.2] [1.3.2][1.3.1-1.3.2] - 2020-06-23

Small upgrade to latest FlaUI release.

### Added

-   FlaUI upgrade to version 3.2.0

## [Release][1.3.1] 1.3.1 - 2020-06-20

First release from wrapper library Robotframework-FlaUI

### Added

-   Automatic wheel package generation in appveyor and local builds
-   Keyword documentation by [github.io][]
-   Support for Python 3.7
-   First release for supported flaui wrapper modules - Application, Checkbox, Combobox, Debug, Grid, Label, Listbox, Radiobuttion, Tab, Textbox, Windows, Keyboard, Mouse

[keep a changelog]: http://keepachangelog.com/

[semantic versioning]: http://semver.org/

[github.io]: https://gdatasoftwareag.github.io/robotframework-flaui

[unreleased]: ../../compare/1.6.1...main

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
