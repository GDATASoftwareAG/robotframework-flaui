*** Settings ***
Documentation   Test suite for mouse keywords.
...             XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...             Keyword                               Test Case Names
...             Click                                 Left Click
...             Double Click                          Double Click
...             Right Click                           Right Click
...             Move To                               Move To
...             Drag And Drop                         Drag And Drop
...

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Suite Setup      Init Main Application
Suite Teardown   Stop Application  ${MAIN_PID}

*** Variables ***
${EXPECTED_CONTEXT_MENU}   ${MAIN_WINDOW}/Window/Menu
${CLICK_BUTTON}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='InvokableButton']
${RIGHT_CLICK_BUTTON}      ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ContextMenu']
${DOUBLE_CLICK_BUTTON}     ${MAIN_WINDOW_SIMPLE_CONTROLS}/CheckBox[@Name='3-Way Test Checkbox']
${XPATH_GRID_VIEW}         ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group[@Name='Grid']/DataGrid[@AutomationId='dataGridView']
${DRAG_FROM}               ${XPATH_GRID_VIEW}/Header/HeaderItem[3]/Text
${DRAG_TO}                 ${XPATH_GRID_VIEW}/Header/HeaderItem[1]/Text

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

Drag And Drop
    Click      ${MAIN_WINDOW_COMPLEX_CONTROLS}
    Select Grid Row By Index  ${XPATH_GRID_VIEW}  1
    ${DATA}  Get Selected Grid Rows  ${XPATH_GRID_VIEW}
    Should Contain    ${DATA}  : 2
    Drag And Drop  ${DRAG_FROM}      ${DRAG_TO}
    Select Grid Row By Index  ${XPATH_GRID_VIEW}  1
    ${DATA}  Get Selected Grid Rows  ${XPATH_GRID_VIEW}
    Should Contain    ${DATA}   : 1
