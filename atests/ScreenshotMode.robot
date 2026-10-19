*** Settings ***
Documentation       Test suite for screenshot keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             OperatingSystem
Library             Process
Library             String
Library             StringFormat
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=True    screenshot_mode=BASE64
Library             util/screenshotlog.py
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
    Log Should Contain Screenshot    data:image/png;base64,
    [Teardown]    Run Keyword And Ignore Error    Stop Application    ${PID}

Failure Screenshot Is Embedded In The Log
    ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
    Log Should Contain Screenshot    data:image/png;base64,
