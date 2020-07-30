# Robotframework-FlaUI Library

| Badges |
|---|
| <img src="https://img.shields.io/github/license/GDATASoftwareAG/robotframework-flaui?style=flat-square">  |
| [<img src="https://img.shields.io/appveyor/tests/GDATACyberDefenseAG/robotframework-flaui?style=flat-square">](https://ci.appveyor.com/project/GDATACyberDefenseAG/robotframework-flaui/build/tests) |
| [![](https://img.shields.io/pypi/wheel/robotframework-flaui?style=flat-square)](https://pypi.org/pypi/robotframework-flaui/) |

## Introduction

Robotframework-FlaUI is a keyword based user interface automation testing library for Windows applications like Win32, WinForms, WPF or Store Apps.
It's based on the [FlaUI](https://github.com/FlaUI/FlaUI) user interface automation library.

## Installation

Install the latest stable release:

```
pip install --upgrade robotframework-flaui
```

## Documentation

*  [Keyword documentation](https://gdatasoftwareag.github.io/robotframework-flaui)

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
* VisualUIAVerify
* Inspect
* UISpy

## Examples

Examples of use can be found in the atests folder.

## Development

### Preconditions

* Install [Python](https://www.python.org/downloads/), if not already installed. Only Python 3 is supported.
* To install Robot Framework and Python for .NET, run
```
pip install pythonnet
pip install robotframework
pip install robotframework-stringformat
pip install wheel
```

Alternatively you could use the provided requirements file:
```
pip install -r requirements.txt
```

### Test-Applications

Two test projects were used for the UI automation:

* FlaUI WPF Test App 'Standard application that contains all common UI elements'
* Notifier Test App 'Application which closes automatically after a time'

### Building and testing locally

Use the provided local_install file:

```
.\local_install.cmd
```

The script automatically builds the:
  * library as a wheel file stored in the Dist folder
  * Test documentation located in the Docs folder
  * Automatically installs and runs the robot tests of the library and saves the test results in the Result folder

## Acknowledgements

### FlaUI

* Thanks to [@Roemer](https://github.com/Roemer) for the passion to create and maintain the FlaUI project.
* Thanks to [FlaUI](https://github.com/FlaUI/FlaUI) developers and maintainers for this project.
