*** Settings ***
Documentation       Error handling test suite for all common flaui keywords.
...

Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False    timeout=0
Library             StringFormat
Resource            util/Error.resource
Resource            util/XPath.resource

Test Template       Execute Keyword And Expect Error Message


*** Variables ***
${EXP_VALUE_INPUT_TEXT}             Type text
@{KEYBOARD_INPUT_TEXT_SHORTCUT}     t'${EXP_VALUE_INPUT_TEXT}'    s'CTRL+A'    s'CTRL+C'    s'END'    s'CTRL+V'


*** Test Cases ***
Attach Application By Name    Attach Application By Name    ${EXP_ERR_MSG_APP_NAME_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Attach Application By PID    Attach Application By PID    ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}    ${XPATH_NOT_EXISTS}
Click    Click    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Close Application    Close Application    ${EXP_ERR_MSG_APP_NOT_ATTACHED}    ${0}
Close Window    Close Window    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Collapse Combobox    Collapse Combobox    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Combobox Should Contain    Combobox Should Contain    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    Item 3
Collapse TreeItem    Collapse TreeItem    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    No Such Item
Collapse All TreeItems    Collapse All TreeItems    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Drag And Drop FirstElement    Drag And Drop    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    /Window
Drag And Drop SecondElement    Drag And Drop    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    /Window    ${XPATH_NOT_EXISTS}
Double Click    Double Click    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Element Should Exist    Element Should Exist    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Expand TreeItem    Expand TreeItem    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    No Such Item
Expand Combobox    Expand Combobox    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Focus    Focus    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get All Names From Combobox    Get All Names From Combobox    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get All Names From Listbox    Get All Names From Listbox    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get All Texts From Combobox    Get All Texts From Combobox    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get All Texts From Listbox    Get All Texts From Listbox    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Checkbox State    Get Checkbox State    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Childs From Element    Get Childs From Element    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Combobox Items Count    Get Combobox Items Count    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Listbox Items Count    Get Listbox Items Count    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Grid Rows Count    Get Grid Rows Count    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Name From Element    Get Name From Element    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Radiobutton State    Get Radiobutton State    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Selected Grid Rows    Get Selected Grid Rows    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Tab Items Names    Get Tab Items Names    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Text From Textbox    Get Text From Textbox    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Root TreeItems Count    Get Root TreeItems Count    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get All Visible TreeItems Count    Get All Visible TreeItems Count    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Selected Treeitems Name    Get Selected Treeitems Name    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get All Visible TreeItems Names    Get All Visible TreeItems Names    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Rectangle Bounding From Element    Get Rectangle Bounding From Element    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Is Element Enabled    Is Element Enabled    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Is Element Offscreen    Is Element Offscreen    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
TreeItem Should Be Visible    TreeItem Should Be Visible    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    No Such Item
Launch Application    Launch Application    ${EXP_ERR_MSG_APP_NOT_EXIST}    ${XPATH_NOT_EXISTS}
Launch Application With Args    Launch Application With Args    ${EXP_ERR_MSG_APP_NOT_EXIST}    ${XPATH_NOT_EXISTS}    ARGS
Listbox Selection Should Be    Listbox Selection Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    No Such Item
Listbox Should Contain    Listbox Should Contain    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    No Such Item
Move To    Move To    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Name Contains Text    Name Contains Text    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${MAIN_WINDOW}    ${XPATH_NOT_EXISTS}
Name Should Be    Name Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${MAIN_WINDOW}    ${XPATH_NOT_EXISTS}
Press Keys    Press Keys    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${KEYBOARD_INPUT_TEXT_SHORTCUT}    ${XPATH_NOT_EXISTS}
Right Click    Right Click    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Select Combobox Item By Index    Select Combobox Item By Index    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    -2000
Select Listbox Item By Index    Select Listbox Item By Index    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    0
Select Listbox Item By Name    Select Listbox Item By Name    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    No Such Item
Select Grid Row By Index    Select Grid Row By Index    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    2
Select Grid Row By Name    Select Grid Row By Name    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    2    Simple item 1
Select Tab Item By Name    Select Tab Item By Name    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    Other Controls
Select Radiobutton    Select Radiobutton    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Select TreeItem    Select TreeItem    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    No Such Item
Select Visible TreeItem By Name    Select Visible TreeItem By Name    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    No Such Item
Set Checkbox State    Set Checkbox State    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ${False}
Set Text To Textbox    Set Text To Textbox    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ${XPATH_NOT_EXISTS}
Get Background Color    Get Background Color    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Foreground Color    Get Foreground Color    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Font Size    Get Font Size    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Font Name    Get Font Name    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Font Weight    Get Font Weight    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Culture    Get Culture    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Is Hidden    Is Hidden    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Is Visible    Is Visible    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Window Visual State    Get Window Visual State    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Window Interaction State    Get Window Interaction State    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Toggle State    Get Toggle State    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get All Data From Grid    Get All Data From Grid    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Toggle    Toggle    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Background Color Should Be    Background Color Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Foreground Color Should Be    Foreground Color Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Font Size Should Be    Font Size Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Font Name Should Be    Font Name Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Font Weight Should Be    Font Weight Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Culture Should Be    Culture Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Window Visual State Should Be    Window Visual State Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Window Interaction State Should Be    Window Interaction State Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Toggle State Should Be    Toggle State Should Be    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY
Maximize Window    Maximize Window    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Minimize Window    Minimize Window    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Normalize Window    Normalize Window    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Can Window Be Maximized    Can Window Be Maximized    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Can Window Be Minimized    Can Window Be Minimized    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
Get Property From Element    Get Property From Element    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}    ANY


*** Keywords ***
Execute Keyword And Expect Error Message
    [Arguments]    ${keyword}    ${expected_default_error_msg}    @{args}

    IF    '${keyword}' == 'Get Property From Element'
        ${EXP_ERR_MSG}    Set Variable    ${EXP_INVALID_PROPETY_ARGUMENT}
        ${EXP_CUSTOM_ERR_MSG}    Set Variable    ${EXP_INVALID_PROPETY_ARGUMENT}
    ELSE
        ${EXP_ERR_MSG}    Format String    ${expected_default_error_msg}    ${XPATH_NOT_EXISTS}
    END

    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Run Keyword    ${keyword}    @{args}
    Run Keyword And Expect Error
    ...    ${EXP_CUSTOM_ERR_MSG}
    ...    Run Keyword
    ...    ${keyword}
    ...    @{args}
    ...    msg=${CUSTOM_ERR_MSG}
