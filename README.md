# Robotframework-FlaUI Library

[license]: https://img.shields.io/github/license/GDATASoftwareAG/robotframework-flaui?style=flat-square

[py38x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.8%20x86/main?label=3.8&style=flat-square
[py38x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.8%20x64/main?label=3.8&style=flat-square

[py39x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.9%20x86/main?label=3.9&style=flat-square
[py39x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.9%20x64/main?label=3.9&style=flat-square

[py310x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.10%20x86/main?label=3.10&style=flat-square
[py310x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.10%20x64/main?label=3.10&style=flat-square

[py311x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.11%20x86/main?label=3.11&style=flat-square
[py311x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.11%20x64/main?label=3.11&style=flat-square

[py312x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.12%20x86/main?label=3.12&style=flat-square
[py312x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.12%20x64/main?label=3.12&style=flat-square


[tests]: https://img.shields.io/appveyor/tests/GDATACyberDefenseAG/robotframework-flaui/main?style=flat-square"
[tests_url]: https://ci.appveyor.com/project/GDATACyberDefenseAG/robotframework-flaui/build/tests

[pypi]: https://img.shields.io/pypi/v/robotframework-flaui?style=flat-square
[pypi_url]: https://pypi.org/pypi/robotframework-flaui

[python_37]: https://img.shields.io/badge/Python-3.7-blue
[python_38]: https://img.shields.io/badge/Python-3.8-blue
[python_39]: https://img.shields.io/badge/Python-3.9-blue
[python_310]: https://img.shields.io/badge/Python-3.10-blue
[python_311]: https://img.shields.io/badge/Python-3.11-blue
[python_312]: https://img.shields.io/badge/Python-3.12-blue

[rf3]: https://img.shields.io/badge/3-Supported-blue
[rf4]: https://img.shields.io/badge/4-Supported-blue
[rf5]: https://img.shields.io/badge/5-Supported-blue
[rf6]: https://img.shields.io/badge/6-Supported-blue
[rf7]: https://img.shields.io/badge/7-Supported-blue

|                          |                                                                             |
|---                       |-----------------------------------------------------------------------------|
| License                  | ![][license]                                                                |
| Python Builds (x86)      | ![][py38x86] ![][py39x86] ![][py310x86] ![][py311x86] ![][py312x86]         |
| Python Builds (x64)      | ![][py38x64] ![][py39x64] ![][py310x64] ![][py311x64] ![][py312x64]         |
| Tests                    | [![][tests]][tests_url]                                                     |
| Python                   | ![][python_38] ![][python_39] ![][python_310] ![][python_311] ![python_312] |
| Robotframework           | ![][rf3] ![][rf4] ![][rf5] ![][rf6] ![][rf7]                                |
| PyPi                     | [![][pypi]][pypi_url]                                                       |

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

### Python.Net Wrapper Issues

#### Robotframework-Flaui 1.x

* With the release of Python.Net version 2.5.2, Python 3.9 support was implemented for the first time.
* However, no official support for Python 3.9 has been released yet.
  * For more information see the issue [#1389](https://github.com/pythonnet/pythonnet/issues/1389)
* If there are problems installing the Python.Net library, please use Python 3.8 instead.
* This is only a potential problem by all robotframework-flaui 1.x versions which are implemented by Python.Net 2.5.2

#### Robotframework-Flaui 2.x

* Sometimes an AccessViolationException wil be occure on latest Python.Net Version v3.0.1
  * For more information see the issue [#1977](https://github.com/pythonnet/pythonnet/issues/1977)
  * A workaround is to set Python's memory allocation environment variable "PYTHONMALLOC=malloc"

## Documentation

*  [Keyword documentation](https://gdatasoftwareag.github.io/robotframework-flaui)
*  [XPath explanation](https://gdatasoftwareag.github.io/robotframework-flaui/xpath.html)

### RFHUB2

[RFHUB2](https://pypi.org/project/rfhub2/) is an opensource project aimed to provide nice and easy way of collecting, browsing and sharing documentation of existing keywords written in RobotFramework and python. Built with Material-UI and FastAPI, served by Uvicorn.

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
* Alternatively [FlaUInspectStable](https://github.com/noubar/FlaUInspectStable) more stable version
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
