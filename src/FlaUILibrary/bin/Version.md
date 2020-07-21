# Library Version Table

| Library | Version | Date       | .Net Framework | Dependency                     | License | Revision                                   |
|---------|---------|------------| -------------- | -------------------------------|---------|--------------------------------------------|
| Core    | 3.1.0   | 19.05.2019 | 4.5            | Interop.UIAutomationClient.dll | MIT     | 48f94a076e7db1ee822958a779a38cad09a7c70f   |
| UIA3    | 3.1.0   | 19.05.2019 | 4.5            |                                | MIT     | 48f94a076e7db1ee822958a779a38cad09a7c70f   |

## Changelog

| Date       | To Revision                              | Description                                                                                                                              |
|------------|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 25.05.2020 | 48f94a076e7db1ee822958a779a38cad09a7c70f | Core, UIA3 will be updated to latest stable release version 3.1.0. |
| 04.03.2020 | 038ae4cc74cc3a3369150a6dc442017bb2a37f69 | Core, UIA3 will be updated to latest stable release version 3.0.0. Unused UIA2 dll is removed.                      |
| 26.07.2019 | f81909229d0fdce86c8148864a1a40aa464c8579 | Core, UIA2 and UIA3 will be updated to pull request from 5 Jun 2018 because of PropertyNotSupportedException issue. |

## Known Issues

### PropertyNotSupportedException when searching by XPath

   * [Github Issue 172](https://github.com/Roemer/FlaUI/issues/172)
   * Fixed since [pull request](https://github.com/Roemer/FlaUI/pull/173) from 5 Jun 2018
   
Issue throws an PropertyNotSupportedException for XPath Automation ID usage.

#### Steps to reproduce
```
${item} =  Get Item  /Pane[@Name='Taskbar']/Pane[@AutomationId='303']
```
