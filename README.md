# Robotframework-FlaUI Library

[license]: https://img.shields.io/github/license/GDATASoftwareAG/robotframework-flaui?style=flat-square
[py37x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.7%20x86/main?label=3.7&style=flat-square
[py37x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.7%20x64/main?label=3.7&style=flat-square
[py38x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.8%20x86/main?label=3.8&style=flat-square
[py38x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.8%20x64/main?label=3.8&style=flat-square
[py39x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.9%20x86/main?label=3.9&style=flat-square
[py39x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.9%20x64/main?label=3.9&style=flat-square
[tests]: https://img.shields.io/appveyor/tests/GDATACyberDefenseAG/robotframework-flaui/main?style=flat-square"
[tests_url]: https://ci.appveyor.com/project/GDATACyberDefenseAG/robotframework-flaui/build/tests
[pypi]: https://img.shields.io/pypi/v/robotframework-flaui?style=flat-square
[pypi_url]: https://pypi.org/pypi/robotframework-flaui

| | |
|---| --- |
| License  | ![][license]  |
| Python Builds (x86) | ![][py37x86] ![][py38x86] ![][py39x86]  |
| Python Builds (x64) | ![][py37x64] ![][py38x64] ![][py39x64]  |
| Tests    | [![][tests]][tests_url] |
| PyPi     | [![][pypi]][pypi_url] |

## Introduction

Robotframework-FlaUI is a keyword based user interface automation testing library for Windows applications like Win32, WinForms, WPF or Store Apps.
It's based on the [FlaUI](https://github.com/FlaUI/FlaUI) user interface automation library.

## Installation

Install the latest stable release:

```
pip install --upgrade robotframework-flaui
```

## Dependencies and python support

The robot framework FlaUI is supposed to support the current Python 3 versions.

### Required dependencies

See dependencies from [Documentation](https://gdatasoftwareag.github.io/robotframework-flaui)

### Additonal information about Python.Net

* With the release of Python.Net version 2.5.2, Python 3.9 support was implemented for the first time.
* However, no official support for Python 3.9 has been released yet.
  * For more information see the issue [#1389](https://github.com/pythonnet/pythonnet/issues/1389)
* If there are problems installing the Python.Net library, please use Python 3.8 instead.

## Documentation

*  [Keyword documentation](https://gdatasoftwareag.github.io/robotframework-flaui)
*  [XPath explanation](https://gdatasoftwareag.github.io/robotframework-flaui/xpath.html)

### RFHUB2

[RHUB2](https://pypi.org/project/rfhub2/) is an opensource project aimed to provide nice and easy way of collecting, browsing and sharing documentation of existing keywords written in RobotFramework and python. Built with Material-UI and FastAPI, served by Uvicorn.

Under docs/keywords are the necessary .XML files to import the keywords.

These can be imported separately according to their version with the RFHUB2-CLI tool or all versions.

```
rfhub2-cli .\docs\keywords\
rfhub2-cli .\docs\keywords\<VERSION>
```

## GUI Inspector Tools

There are various tools around which help inspecting application that should be ui tested or automated. 

Some of them are:
* [FlaUI Inspect](https://github.com/FlaUI/FlaUInspect)
* [Microsoft Accessibility Insights For Windows](https://accessibilityinsights.io)
* VisualUIAVerify
* Inspect
* UISpy

## Examples

Examples of use can be found in the atests folder.

## Development

### Preconditions

* Install [Python](https://www.python.org/downloads), if not already installed. 
* Only Python 3 is supported.
* Install Robotframework and Python.Net

#### Dependency installation by Keen.bat

```
.\keen.bat dependency
```

### Test-Applications

Two test projects were used for the UI automation:

* FlaUI WPF Test App 'Standard application that contains all common UI elements'
* Notifier Test App 'Application which closes automatically after a time'

### Building and testing locally

Use the provided 'Commander Keen' file:

```
.\keen.bat test
```

The script automatically builds the:
  * Library as a wheel file stored in the Dist folder
  * Test documentation located in the Docs folder
  * Automatically installs and runs the robot tests of the library and saves the test results in the Result folder

Following arguments are supported:
```
.\keen.bat <argument>
```
  * cleanup - Removes all build folders
  * dependency - Install all python dependencies
  * build - Build wheel file
  * install - Install wheel file
  * test - Test robotframework-flaui (UIA2 and UIA3)
  * test_uia2 - Test UIA2 interface usage
  * test_uia3 - Test UIA3 interface usage
  * pylint - Static code analysis for PEP 8. Generates pylint.html file in results.

## Acknowledgements

### FlaUI

* Thanks to [@Roemer](https://github.com/Roemer) for the passion to create and maintain the FlaUI project.
* Thanks to [FlaUI](https://github.com/FlaUI/FlaUI) developers and maintainers for this project.
