*** Settings ***
Documentation   Test suite for mouse keywords.

Library         FlaUILibrary
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${EXPECTED_CONTEXT_MENU}   ${MAIN_WINDOW}/Window/Menu
${CLICK_BUTTON}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='InvokableButton']
${RIGHT_CLICK_BUTTON}      ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ContextMenu']
${DOUBLE_CLICK_BUTTON}     ${MAIN_WINDOW_SIMPLE_CONTROLS}/CheckBox[@Name='3-Way Test Checkbox']

*** Test Cases ***

Left Click
    Click  ${CLICK_BUTTON}
    Name Should Be  Invoked!  ${CLICK_BUTTON}

Double Click
    Click  ${DOUBLE_CLICK_BUTTON}
    ${STATE}   Get Checkbox State  ${DOUBLE_CLICK_BUTTON}
    Should Be Equal  ${STATE}  ${True}
    Double Click  ${DOUBLE_CLICK_BUTTON}
    ${STATE}   Get Checkbox State  ${DOUBLE_CLICK_BUTTON}
    Should Be Equal  ${STATE}  ${False}

Right Click
    Right Click  ${RIGHT_CLICK_BUTTON}
    Element Should Exist  ${EXPECTED_CONTEXT_MENU}

Move To
    Move To  ${RIGHT_CLICK_BUTTON}
    Right Click  ${RIGHT_CLICK_BUTTON}
    Element Should Exist  ${EXPECTED_CONTEXT_MENU}
