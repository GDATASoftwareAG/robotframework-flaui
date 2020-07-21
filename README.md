# Robotframework-FlaUI Library

[<img src="https://img.shields.io/appveyor/tests/GDATACyberDefenseAG/robotframework-flaui">](https://ci.appveyor.com/project/GDATACyberDefenseAG/robotframework-flaui/build/tests)

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
