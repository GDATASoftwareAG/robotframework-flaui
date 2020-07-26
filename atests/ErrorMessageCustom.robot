*** Settings ***
Documentation   Error handling test suite for all keywords.

Library         FlaUILibrary
Library         StringFormat

Resource        util/Error.robot
Resource        util/XPath.robot

Test Template   Execute Keyword And Expect Custom Error Message

*** Variables ***
${EXP_VALUE_INPUT_TEXT}            Type text
@{KEYBOARD_INPUT_TEXT_SHORTCUT}    t'${EXP_VALUE_INPUT_TEXT}'  s'CTRL+A'  s'CTRL+C'  s'END'  s'CTRL+V'

*** Test Cases ***
Attach Application By Name        Attach Application By Name  ${XPATH_NOT_EXISTS}
Attach Application By PID         Attach Application By PID  ${XPATH_NOT_EXISTS}
Click                             Click  ${XPATH_NOT_EXISTS}
Close Application                 Close Application
Close Window                      Close Window  ${XPATH_NOT_EXISTS}
Combobox Should Contain           Combobox Should Contain  ${XPATH_NOT_EXISTS}  Item 3
Double Click                      Double Click  ${XPATH_NOT_EXISTS}
Element Should Be Visible         Element Should Be Visible  ${XPATH_NOT_EXISTS}
Element Should Exist              Element Should Exist  ${XPATH_NOT_EXISTS}
Element Should Not Be Visible     Element Should Not Be Visible  ${XPATH_NOT_EXISTS}
Element Should Not Exist          Element Should Not Be Visible  ${XPATH_NOT_EXISTS}
Focus                             Focus  ${XPATH_NOT_EXISTS}
Get Checkbox State                Get Checkbox State  ${XPATH_NOT_EXISTS}
Get Childs From Element           Get Childs From Element  ${XPATH_NOT_EXISTS}
Get Combobox Items Count          Get Combobox Items Count  ${XPATH_NOT_EXISTS}
Get Listbox Items Count           Get Listbox Items Count  ${XPATH_NOT_EXISTS}
Get Listview Rows Count           Get Listview Rows Count  ${XPATH_NOT_EXISTS}
Get Name From Element             Get Name From Element  ${XPATH_NOT_EXISTS}
Get Radiobutton State             Get Radiobutton State  ${XPATH_NOT_EXISTS}
Get Selected Items From Combobox  Get Selected Items From Combobox  ${XPATH_NOT_EXISTS}
Get Selected Listview Rows        Get Selected Listview Rows  ${XPATH_NOT_EXISTS}
Get Tab Items Names               Get Tab Items Names  ${XPATH_NOT_EXISTS}
Get Text From Textbox             Get Text From Textbox  ${XPATH_NOT_EXISTS}
Is Element Enabled                Is Element Enabled  ${XPATH_NOT_EXISTS}
Is Element Visible                Is Element Visible  ${XPATH_NOT_EXISTS}
Launch Application                Launch Application  ${XPATH_NOT_EXISTS}
Listbox Selection Should Be       Listbox Selection Should Be  ${XPATH_NOT_EXISTS}  No Such Item
Listbox Should Contain            Listbox Should Contain  ${XPATH_NOT_EXISTS}  No Such Item
Move To                           Move To  ${XPATH_NOT_EXISTS}
Name Contains Text                Name Contains Text  ${MAIN_WINDOW}  ${XPATH_NOT_EXISTS}
Name Should Be                    Name Should Be  ${XPATH_NOT_EXISTS}  ${MAIN_WINDOW}
Press Keys                        Press Keys  ${KEYBOARD_INPUT_TEXT_SHORTCUT}  ${XPATH_NOT_EXISTS}
Right Click                       Right Click  ${XPATH_NOT_EXISTS}
Select Combobox Item By Index     Select Combobox Item By Index  -2000  ${XPATH_NOT_EXISTS}
Select Listbox Item By Index      Select Listbox Item By Index  ${XPATH_NOT_EXISTS}  0
Select Listview Row By Index      Select Listview Row By Index  ${XPATH_NOT_EXISTS}  2
Select Listview Row By Name       Select Listview Row By Name  ${XPATH_NOT_EXISTS}  2  Simple item 1
Select Tab Item By Name           Select Tab Item By Name  ${XPATH_NOT_EXISTS}  Other Controls
Set Checkbox State                Set Checkbox State  ${XPATH_NOT_EXISTS}  ${False}
Set Radiobutton State             Set Radiobutton State  ${XPATH_NOT_EXISTS}  ${True}
Set Text To Textbox               Set Text To Textbox  ${XPATH_NOT_EXISTS}  ${XPATH_NOT_EXISTS}
Wait Until Element Is Hidden      Wait Until Element Is Hidden  ${XPATH_NOT_EXISTS}  10

*** Keywords ***

Execute Keyword And Expect Custom Error Message
    [Arguments]  ${keyword}  @{args}
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Run Keyword  ${keyword}  @{args}  ${CUSTOM_ERR_MSG}
