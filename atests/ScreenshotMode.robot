*** Settings ***
Documentation       Test suite for screenshot keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Process
Library             String
Library             OperatingSystem
Library             StringFormat
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=True    screenshot_mode=BASE64
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource


*** Test Cases ***
Take Screenshot Of Window As Base64 From Library Import
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${base64}    Take Screenshot    ${MAIN_WINDOW}
    Should Not Be Equal    ${base64}    ${None}    Returned base64 image is 'None'
    Should Not Be Empty    ${base64}    Returned base64 image is empty
    [Teardown]    Run Keyword And Ignore Error    Stop Application    ${PID}
