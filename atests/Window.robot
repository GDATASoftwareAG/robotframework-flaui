*** Settings ***
Documentation       Test suite for window keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Process
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Library             StringFormat
Resource            util/Common.resource
Resource            util/XPath.resource


*** Test Cases ***
Close Window
    Start Application
    Close Window    ${MAIN_WINDOW}
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}
