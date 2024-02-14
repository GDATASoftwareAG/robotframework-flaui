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
${CONTEXT_MENUITEM1}       ${MAIN_WINDOW}/Window/Menu/MenuItem[@Name='Context 1']
${CONTEXT_MENUITEM2}       ${MAIN_WINDOW}/Window/Menu/MenuItem[@Name='Context 2']
${CONTEXT_MENUITEM3}       ${MAIN_WINDOW}/Window/Menu/MenuItem[@Name='Context 2']/MenuItem[@Name='Inner Context']
${CLICK_BUTTON}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='InvokableButton']
${HOLD_BUTTON}             ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ClickAndHoldButton']
${RIGHT_CLICK_BUTTON}      ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ContextMenu']
${DOUBLE_CLICK_BUTTON}     ${MAIN_WINDOW_SIMPLE_CONTROLS}/CheckBox[@Name='3-Way Test Checkbox']
${XPATH_GRID_VIEW}         ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group[@Name='Grid']/DataGrid[@AutomationId='dataGridView']
${DRAG_FROM}               ${XPATH_GRID_VIEW}/Header/HeaderItem[3]/Text
${DRAG_TO}                 ${XPATH_GRID_VIEW}/Header/HeaderItem[1]/Text
${SOME_MENUITEM}           ${EXPECTED_CONTEXT_MENU}/MenuItem[@Name='Some MenuItem']/Text[@Name='Some MenuItem']
${PopupToggle2_BUTTON}     ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='PopupToggleButton2']
${ENABLE_BUTTON}           ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='EnableButton']
${READYTOTAKEOFF_TEXT}     ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='EnableButton']/Text[@Name='Ready to take off']
${TOGGLE_BUTTON}           ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ToggleButton']
${XPATH_COMBO_BOX}         ${MAIN_WINDOW_SIMPLE_CONTROLS}/ComboBox[@AutomationId='NonEditableCombo']
${CONTEXTMENU_BUTTON}      ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ContextMenu']
${XPATH_COMBO_BOX_ITEM}    ${XPATH_COMBO_BOX}/ListItem[@Name='Item 3']/Text[@Name='Item 3']
${XPATH_TREE_PARENT}       ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group[@Name='Tree']/Tree[@AutomationId='treeView1']/TreeItem[@Name='Lvl1 a']/Text[@Name='Lvl1 a']
${XPATH_TREE_CHILD}        ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group[@Name='Tree']/Tree[@AutomationId='treeView1']/TreeItem[@Name='Lvl1 a']/TreeItem[@Name='Lvl2 a']/Text[@Name='Lvl2 a']

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

Double Click Open Double Click Close
    Double Click Open  ${XPATH_TREE_PARENT}  ${XPATH_TREE_CHILD}
    Element Should Exist    ${XPATH_TREE_CHILD}
    Double Click Close  ${XPATH_TREE_PARENT}  ${XPATH_TREE_CHILD}
    Element Should Not Exist    ${XPATH_TREE_CHILD}

Left Click Open
    Click Open  ${MAIN_WINDOW_SIMPLE_CONTROLS}  ${PopupToggle2_BUTTON}  ${MAIN_WINDOW}
    Click Open  ${PopupToggle2_BUTTON}  ${SOME_MENUITEM}
    Click Open  ${ENABLE_BUTTON}  ${READYTOTAKEOFF_TEXT}
    # Hold Button is already there. It should not be any click action
    Click Open  ${TOGGLE_BUTTON}  ${HOLD_BUTTON}
    ${state}   Get Toggle State    ${TOGGLE_BUTTON}
    Should Be True    '${state}'=='OFF'
    # Hold Button is already there but it should click it at least for once because of ignore option
    Click Open  ${TOGGLE_BUTTON}  ${HOLD_BUTTON}  ignore_if_already_open=${False}
    ${state}   Get Toggle State    ${TOGGLE_BUTTON}
    Should Be True    '${state}'=='ON'
    
Left Click Open Error
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_NOT_OPENED}  ${XPATH_NOT_EXISTS}  ${CLICK_BUTTON}
    Run Keyword and Expect Error  EQUALS: ${EXP_ERR_MSG}  Click Open  ${CLICK_BUTTON}  ${XPATH_NOT_EXISTS}

Right Click Open
    Right Click Open  ${RIGHT_CLICK_BUTTON}  ${CONTEXT_MENUITEM1}
    Element Should Exist  ${CONTEXT_MENUITEM1}
    Right Click Open    ${CONTEXT_MENUITEM1}  ${CONTEXT_MENUITEM1}  ignore_if_already_open=${True}
    Element Should Exist  ${CONTEXT_MENUITEM1}
    
Left Click Close
    Click Open   ${XPATH_COMBO_BOX}  ${XPATH_COMBO_BOX_ITEM}
    Click Close  ${XPATH_COMBO_BOX_ITEM}
    Element Should Not Exist    ${XPATH_COMBO_BOX_ITEM}

Left Click Close Error
    Click Open  ${PopupToggle2_BUTTON}  ${SOME_MENUITEM}
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_NOT_CLOSED}  ${SOME_MENUITEM}  ${PopupToggle2_BUTTON}
    Run Keyword and Expect Error  EQUALS: ${EXP_ERR_MSG}  Click Close  ${PopupToggle2_BUTTON}  ${SOME_MENUITEM}
    Element Should Exist  ${SOME_MENUITEM}

Right Click Close
    Click Open  ${PopupToggle2_BUTTON}  ${SOME_MENUITEM}
    Element Should Not Exist    ${XPATH_COMBO_BOX_ITEM}
    Right Click Close   ${PopupToggle2_BUTTON}  ${XPATH_COMBO_BOX_ITEM}
