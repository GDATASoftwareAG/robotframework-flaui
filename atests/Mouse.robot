*** Settings ***
Documentation   Test suite for mouse keywords.
...             XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
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
${HOLD_BUTTON}             ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ClickAndHoldButton']
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

Left Click And Hold
    Click Hold  ${HOLD_BUTTON}  2050
    ${status1}  Run Keyword And Return Status  Name Contains Text  2,  ${HOLD_BUTTON}  #DE number
    ${status2}  Run Keyword And Return Status  Name Contains Text  2.  ${HOLD_BUTTON}  #US Number
    IF    ${status1}==${False} and ${status2}==${False}
       Fail   Click And Hold did not work
    END

Double Click And Hold
    Double Click Hold  ${HOLD_BUTTON}  3050
    ${status1}  Run Keyword And Return Status  Name Contains Text  3,  ${HOLD_BUTTON}  #DE number
    ${status2}  Run Keyword And Return Status  Name Contains Text  3.  ${HOLD_BUTTON}  #US Number
    IF    ${status1}==${False} and ${status2}==${False}
       Fail   Click And Hold did not work
    END

Right Click And Hold
    Right Click Hold  ${HOLD_BUTTON}  4050
    ${status1}  Run Keyword And Return Status  Name Contains Text  4,  ${HOLD_BUTTON}  #DE number
    ${status2}  Run Keyword And Return Status  Name Contains Text  4.  ${HOLD_BUTTON}  #US Number
    IF    ${status1}==${False} and ${status2}==${False}
       Fail   Click And Hold did not work
    END

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
