*** Settings ***
Documentation       Test suite for checkbox keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Library             StringFormat
Resource            util/Common.robot
Resource            util/XPath.robot

Suite Setup         Init Main Application
Suite Teardown      Stop Application    ${MAIN_PID}


*** Variables ***
${XPATH_CHECKBOX}       ${MAIN_WINDOW_SIMPLE_CONTROLS}/CheckBox[@AutomationId='SimpleCheckBox']


*** Test Cases ***
Get Checkbox State
    ${STATE}    Get Checkbox State    ${XPATH_CHECKBOX}
    Should Be Equal    ${STATE}    ${False}

Set Checkbox State To True
    Set Checkbox State    ${XPATH_CHECKBOX}    ${True}
    ${STATE}    Get Checkbox State    ${XPATH_CHECKBOX}
    Should Be Equal    ${STATE}    ${True}

Set Checkbox State To False
    Set Checkbox State    ${XPATH_CHECKBOX}    ${False}
    ${STATE}    Get Checkbox State    ${XPATH_CHECKBOX}
    Should Be Equal    ${STATE}    ${False}
