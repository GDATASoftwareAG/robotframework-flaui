# Changelog

All notable changes to Robotframework-FlaUI will be documented in this file. This
project adheres to [Semantic Versioning][].

This document follows the conventions laid out in [Keep a CHANGELOG][].

## [Unreleased][]

### Added

-   Data grid examples include

### Changed

-   Renamed flaui wrapper modules
    - ListView to Grid
    - ListControl to ListBox
-   Pylint usage implemented
      - Include to keen.bat pylint
      - Appveyor pylint reporting
-   Command line 'local_install.cmd' changed to 'keen.bat' with a set of supported build instructions

## [1.3.4][] - 2020-06-23

General bugfixing from keywords and improvements from artifact building and testing

### Changed

 -  Keyword 'Set Radiobutton State' changed to 'Select Radiobutton'
 -  Change build system by python matrix testing for Python 3.7, 3.8 x86/x64 testing
 -  Documentation moved to documentation branch
 -  PyPi description modified
 -  Split up from release and develop dependencies by seperate requirements files
 -  Distribution which always forces a binary package with platform name

## [1.3.3][] - 2020-08-24

Upgrade from Pythonet dependency to support Python 3.8.

### Added

-   Python 3.8 support
-   RFHUB .xml file documentation generation and include to all previous releases

### Changed

-  Test cases rewrite by Custom Error Handling and Data Driven Tests
-  Keyword documentation page contains now all .xml file documentation for RFHUB

## [1.3.2][] - 2020-06-23

Small upgrade to latest FlaUI release.

### Added

-   FlaUI upgrade to version 3.2.0

## [1.3.1][] - 2020-06-20

First release from wrapper library Robotframework-FlaUI

### Added

-   Automatic wheel package generation in appveyor and local builds
-   Keyword documentation by [github.io][]
-   Support for Python 3.7
-   First release for supported flaui wrapper modules - Application, Checkbox, Combobox, Debug, Grid, Label, Listbox, Radiobuttion, Tab, Textbox, Windows, Keyboard, Mouse

[keep a changelog]: http://keepachangelog.com/

[semantic versioning]: http://semver.org/

[github.io]: https://gdatasoftwareag.github.io/robotframework-flaui

[unreleased]: ../../compare/1.3.4...master
[1.3.4]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.4
[1.3.3]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.3
[1.3.2]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.2
[1.3.1]: https://github.com/GDATASoftwareAG/robotframework-flaui/releases/tag/1.3.1
