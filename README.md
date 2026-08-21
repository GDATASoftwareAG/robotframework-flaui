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

[py313x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.13%20x86/main?label=3.13&style=flat-square
[py313x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.13%20x64/main?label=3.13&style=flat-square

[py314x86]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.14%20x86/main?label=3.14&style=flat-square
[py314x64]: https://img.shields.io/appveyor/job/build/GDATACyberDefenseAG/robotframework-flaui/Python%203.14%20x64/main?label=3.14&style=flat-square

[tests]: https://img.shields.io/appveyor/tests/GDATACyberDefenseAG/robotframework-flaui/main?style=flat-square
[tests_url]: https://ci.appveyor.com/project/GDATACyberDefenseAG/robotframework-flaui/build/tests

[pypi]: https://img.shields.io/pypi/v/robotframework-flaui?style=flat-square
[pypi_url]: https://pypi.org/pypi/robotframework-flaui

[python_38]: https://img.shields.io/badge/Python-3.8-blue
[python_39]: https://img.shields.io/badge/Python-3.9-blue
[python_310]: https://img.shields.io/badge/Python-3.10-blue
[python_311]: https://img.shields.io/badge/Python-3.11-blue
[python_312]: https://img.shields.io/badge/Python-3.12-blue
[python_313]: https://img.shields.io/badge/Python-3.13-blue
[python_314]: https://img.shields.io/badge/Python-3.14-blue

[rf3]: https://img.shields.io/badge/3-Supported-blue
[rf4]: https://img.shields.io/badge/4-Supported-blue
[rf5]: https://img.shields.io/badge/5-Supported-blue
[rf6]: https://img.shields.io/badge/6-Supported-blue
[rf7]: https://img.shields.io/badge/7-Supported-blue

|                     |                                                                                                         |
|---------------------|---------------------------------------------------------------------------------------------------------|
| License             | ![][license]                                                                                            |
| Python Builds (x86) | ![][py38x86] ![][py39x86] ![][py310x86] ![][py311x86] ![][py312x86] ![][py313x86] ![][py314x86]         |
| Python Builds (x64) | ![][py38x64] ![][py39x64] ![][py310x64] ![][py311x64] ![][py312x64] ![][py313x64] ![][py314x64]         |
| Tests               | [![][tests]][tests_url]                                                                                 |
| Python              | ![][python_38] ![][python_39] ![][python_310] ![][python_311] ![][python_312] ![][python_313] ![][python_314] |
| Robotframework      | ![][rf3] ![][rf4] ![][rf5] ![][rf6] ![][rf7]                                                            |
| PyPi                | [![][pypi]][pypi_url]                                                                                   |

## Introduction

Robotframework-FlaUI is a keyword based user interface automation testing library for Windows applications like Win32, WinForms, WPF or Store Apps.
It's based on the [FlaUI](https://github.com/FlaUI/FlaUI) user interface automation library.

The library supports Microsoft UI Automation interfaces UIA2 and UIA3 (default). Elements are located by XPath.
Mouse keywords also accept absolute screen coordinates or X/Y offsets from an element's clickable point.
Keyboard keywords can send input globally when no XPath is given.

## Installation

Install the latest stable release:

```
pip install --upgrade robotframework-flaui
```

## Usage

```robotframework
*** Settings ***
Library    FlaUILibrary    uia=UIA3    screenshot_on_failure=True    screenshot_mode=FILE    screenshot_suffix=jpg    timeout=1000
```

Library import arguments:

| Argument                | Default | Description                                                                 |
|-------------------------|---------|-----------------------------------------------------------------------------|
| `uia`                   | `UIA3`  | Microsoft UI Automation interface: `UIA2` or `UIA3`                         |
| `screenshot_on_failure` | `True`  | Take a screenshot when a keyword fails                                      |
| `screenshot_dir`        | output  | Screenshot directory relative to the Robot output directory                 |
| `timeout`               | `1000`  | Default element find timeout in milliseconds                                |
| `screenshot_mode`       | `FILE`  | Persist screenshots as `FILE` or `BASE64`                                   |
| `screenshot_suffix`     | `jpg`   | Screenshot file type when mode is `FILE`: `png`, `jpg` or `jpeg`            |

Mouse examples:

```robotframework
Click    ${XPATH}
Click    x=100    y=200
Click    ${XPATH}    x=10    y=20
```

Keyboard examples:

```robotframework
Press Key    t'Text'    ${XPATH}
Press Key    t'Text'
Press Keys    ${KEYS}
```

A full keyword reference is available in the [keyword documentation](https://gdatasoftwareag.github.io/robotframework-flaui).

## Dependencies and python support

The robot framework FlaUI is supposed to support the current Python 3 versions.

### Required dependencies

See dependencies from [Documentation](https://gdatasoftwareag.github.io/robotframework-flaui)

Runtime dependencies are listed in `requirements.txt`:

* Robot Framework 3.2.2 or newer
* Python.Net 3.0.0 or newer
* robotframework-pythonlibcore
* typing-extensions

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

Keyword HTML and XML docs are generated by `libdoc.py` during the `build` blueprint stage and published from the `documentation` GitHub branch to GitHub Pages.

### RFHUB2

[RFHUB2](https://pypi.org/project/rfhub2/) is an opensource project aimed to provide nice and easy way of collecting, browsing and sharing documentation of existing keywords written in RobotFramework and python. Built with Material-UI and FastAPI, served by Uvicorn.

Keyword XML files live on the `documentation` branch under `docs/keywords/`. Check out that branch and import them with RFHUB2-CLI:

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
* Python 3.8 or newer is supported (CI covers 3.8–3.14, x86 and x64).

#### Requirement files

| File                                  | Purpose                                              |
|---------------------------------------|------------------------------------------------------|
| `requirements.txt`                    | Runtime dependencies of the library                  |
| `requirements-dev.txt`                | Local build, lint and test tools                     |
| `requirements-buildsystem.txt`        | [Builddrone](https://pypi.org/project/builddrone/)   |
| `requirements-artifact-upload.txt`    | Twine, used by the `pypi` blueprint stage            |

#### Dependency installation by Builddrone

Install Builddrone, then run stages from `blueprint.json`:

```
python -m pip install -r requirements-buildsystem.txt
python -m builddrone <stage>
```

Builddrone documentation: [https://nepitwin.github.io/Builddrone/latest/](https://nepitwin.github.io/Builddrone/latest/)

### Test-Applications

Two test projects were used for the UI automation:

* FlaUI WPF Test App 'Standard application that contains all common UI elements'
* Notifier Test App 'Application which closes automatically after a time'

### Testing locally TLDR

```powershell
python -m venv .venv
.venv/Scripts/pip install -r requirements-dev.txt

cd ./atests
../.venv/Scripts/robot -v UIA:UIA3 -d ../result -P ../src -t "Element Should Be Offscreen" Element.robot
```

### Building and testing with Builddrone

Local CI is defined in `blueprint.json` and executed by [Builddrone](https://pypi.org/project/builddrone/):

```
python -m builddrone <stage>
```

Builddrone loads `blueprint.json` from the working directory, selects the named stage and runs its module steps in order. Relative paths are resolved from the directory that contains `blueprint.json`.

| Stage                               | Purpose                                                                                          |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| `build`                             | Create `.build.venv`, install `requirements-dev.txt`, build the package into `dist/`, generate keyword docs into `keywords/` |
| `cleanup`                           | Remove generated folders and local virtual environments                                          |
| `robocop`                           | Run Robot Framework lint checks via `robocop_lint.py` in `.testing.venv`                         |
| `pylint`                            | Run pylint for the Python sources in `src`                                                       |
| `test`                              | Run UIA2 and UIA3 acceptance tests, merge reports into `result/`                                 |
| `pypi`                              | Upload `dist/*.whl` and `dist/*.tar.gz` to PyPI (AppVeyor, git tags only)                        |
| `appveyor_upload_tests`             | Upload JUnit results to AppVeyor                                                                 |
| `appveyor_upload_failure_artifacts` | Zip `result/` and upload it as an AppVeyor artifact on failure                                   |

The `build` stage writes:

* Wheel and source distribution under `dist/`
* Keyword documentation `keywords/keywords.html` and `keywords/keywords.xml` (generated by `libdoc.py`)

The `test` stage runs `atests` twice (`UIA2` and `UIA3`), merges the Robot outputs with rebot into `result/`, copies screenshots and converts the merged report with `parsly.py`.

`robocop`, `pylint` and `test` share `.testing.venv`. `build` uses `.build.venv`. `pypi` uses `.upload.venv`.

Example full local CI run:

```powershell
python -m pip install -r requirements-buildsystem.txt
python -m builddrone build
python -m builddrone robocop
python -m builddrone pylint
python -m builddrone test
```

AppVeyor (`appveyor.yml`) runs the same four stages on every branch except `documentation`. The `pypi` stage runs only when the build is triggered by a git tag.

### Contributing

Code changes are welcome via pull request. Release tagging, PyPI upload and keyword documentation publishing are not part of this workflow.

- add or update keywords in folders
  - `src/FlaUILibrary/flaui/module`
  - `src/FlaUILibrary/keywords`
- add or update tests in folder `atests`
- update `CHANGELOG.md` under `[Unreleased]`
- open a pull request against `main`

## Acknowledgements

### FlaUI

* Thanks to [@Roemer](https://github.com/Roemer) for the passion to create and maintain the FlaUI project.
* Thanks to [FlaUI](https://github.com/FlaUI/FlaUI) developers and maintainers for this project.
