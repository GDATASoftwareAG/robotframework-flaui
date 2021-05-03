*** Settings ***
Documentation   Error handling test suite for all common flaui keywords.

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False  timeout=0
Library         StringFormat

Resource        util/Error.robot
Resource        util/XPath.robot

Test Template   Execute Keyword And Expect Error Message

*** Variables ***
${EXP_VALUE_INPUT_TEXT}            Type text
@{KEYBOARD_INPUT_TEXT_SHORTCUT}    t'${EXP_VALUE_INPUT_TEXT}'  s'CTRL+A'  s'CTRL+C'  s'END'  s'CTRL+V'

*** Test Cases ***
Attach Application By Name        Attach Application By Name  ${EXP_ERR_MSG_APP_NAME_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Attach Application By PID         Attach Application By PID  ${EXP_ERR_MSG_PID_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Click                             Click  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Drag And Drop FirstElement        Drag And Drop  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  /Window
Drag And Drop SecondElement       Drag And Drop  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  /Window  ${XPATH_NOT_EXISTS}
Close Application                 Close Application  ${EXP_ERR_MSG_APP_NOT_ATTACHED}
Close Window                      Close Window  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Combobox Should Contain           Combobox Should Contain  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  Item 3
Double Click                      Double Click  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Element Should Be Visible         Element Should Be Visible  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Element Should Exist              Element Should Exist  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Element Should Not Be Visible     Element Should Not Be Visible  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Element Should Not Exist          Element Should Not Be Visible  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Focus                             Focus  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Checkbox State                Get Checkbox State  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Childs From Element           Get Childs From Element  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Combobox Items Count          Get Combobox Items Count  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Listbox Items Count           Get Listbox Items Count  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Grid Rows Count               Get Grid Rows Count  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Name From Element             Get Name From Element  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Radiobutton State             Get Radiobutton State  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Selected Items From Combobox  Get Selected Items From Combobox  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Selected Grid Rows            Get Selected Grid Rows  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Tab Items Names               Get Tab Items Names  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Text From Textbox             Get Text From Textbox  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Root TreeItems Count          Get Root TreeItems Count  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get All Visible TreeItems Count   Get All Visible TreeItems Count   ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get Selected Treeitems Name       Get Selected Treeitems Name   ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Get All Visible TreeItems Names   Get All Visible TreeItems Names   ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Is Element Enabled                Is Element Enabled  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Is Element Visible                Is Element Visible  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
TreeItem Should Be Visible        TreeItem Should Be Visible  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
Launch Application                Launch Application  ${EXP_ERR_MSG_APP_NOT_EXIST}  ${XPATH_NOT_EXISTS}
Launch Application With Args      Launch Application With Args  ${EXP_ERR_MSG_APP_NOT_EXIST}  ${XPATH_NOT_EXISTS}  ARGS
Listbox Selection Should Be       Listbox Selection Should Be  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
Listbox Should Contain            Listbox Should Contain  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
Move To                           Move To  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Name Contains Text                Name Contains Text  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${MAIN_WINDOW}  ${XPATH_NOT_EXISTS}
Name Should Be                    Name Should Be  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${MAIN_WINDOW}  ${XPATH_NOT_EXISTS}
Press Keys                        Press Keys  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${KEYBOARD_INPUT_TEXT_SHORTCUT}  ${XPATH_NOT_EXISTS}
Right Click                       Right Click  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Select Combobox Item By Index     Select Combobox Item By Index  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  -2000
Select Listbox Item By Index      Select Listbox Item By Index  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  0
Select Listbox Item By Name       Select Listbox Item By Name   ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
Select Grid Row By Index          Select Grid Row By Index  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  2
Select Grid Row By Name           Select Grid Row By Name  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  2  Simple item 1
Select Tab Item By Name           Select Tab Item By Name  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  Other Controls
Select Radiobutton                Select Radiobutton  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
Select TreeItem                   Select TreeItem  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
Select Visible TreeItem By Name   Select Visible TreeItem By Name  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
Set Checkbox State                Set Checkbox State  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  ${False}
Set Text To Textbox               Set Text To Textbox  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  ${XPATH_NOT_EXISTS}
Wait Until Element Is Hidden      Wait Until Element Is Hidden  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  10
Collapse TreeItem                 Collapse TreeItem  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
Expand TreeItem                   Expand TreeItem  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
TreeItem Should Be Visible        TreeItem Should Be Visible  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}  No Such Item
Collapse All TreeItems            Collapse All TreeItems  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}

*** Keywords ***
Execute Keyword And Expect Error Message
    [Arguments]  ${keyword}  ${expected_default_error_msg}  @{args}
    ${EXP_ERR_MSG}  Format String  ${expected_default_error_msg}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Run Keyword  ${keyword}  @{args}
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Run Keyword  ${keyword}  @{args}  ${CUSTOM_ERR_MSG}
