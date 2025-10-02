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

Resize Window
    Start Application
    ${_}    ${_}    ${width_before}    ${height_before}    Get Rectangle Bounding From Element    ${MAIN_WINDOW}
    Resize Window    ${MAIN_WINDOW}  ${width_before+50}  ${height_before+50}
    ${_}    ${_}    ${width}    ${height}    Get Rectangle Bounding From Element    ${MAIN_WINDOW}
    Should Be Equal As Numbers    ${width}    ${width_before+50}
    Should Be Equal As Numbers    ${height}    ${height_before+50}
    [Teardown]    Close Window    ${MAIN_WINDOW}
