*** Settings ***
Documentation       Test suite for property keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Collections
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Library             StringFormat
Resource            util/Common.resource
Resource            util/XPath.resource

Suite Setup         Init Main Application
Suite Teardown      Stop Application    ${MAIN_PID}


*** Variables ***
${TOGGLE_ELEMENT}       ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ToggleButton']


*** Test Cases ***
Toggle State
    ${state}    Get Toggle State    ${TOGGLE_ELEMENT}
    Should Be Equal    ${state}    OFF
    Toggle    ${TOGGLE_ELEMENT}

    ${state}    Get Toggle State    ${TOGGLE_ELEMENT}
    Should Be Equal    ${state}    ON

    Toggle    ${TOGGLE_ELEMENT}
    ${state}    Get Toggle State    ${TOGGLE_ELEMENT}
    Should Be Equal    ${state}    OFF
