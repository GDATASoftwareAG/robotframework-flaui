*** Settings ***
Documentation       Test suite for list box keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Process
Library             Collections
Library             StringFormat
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource

Suite Setup         Init Main Application
Suite Teardown      Stop Application    ${MAIN_PID}


*** Variables ***
${XPATH_LISTBOX}    ${MAIN_WINDOW_SIMPLE_CONTROLS}/List[@AutomationId='ListBox']


*** Test Cases ***
Get Listbox Items Count
    ${COUNT}    Get Listbox Items Count    ${XPATH_LISTBOX}
    Should Be Equal As Integers    ${COUNT}    2

Listbox Should Contain
    Listbox Should Contain    ${XPATH_LISTBOX}    ListBox Item #2

Listbox Should Contain Item Not Exist
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_CONTROL_DOES_NOT_CONTAIN_ITEM}    No Such Item
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Listbox Should Contain    ${XPATH_LISTBOX}    No Such Item

Listbox Should Not Contain
    Listbox Should Not Contain    ${XPATH_LISTBOX}    No Such Item

Listbox Should Not Contain Item Does Exist
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_CONTROL_CONTAINS_ITEM}    ListBox Item #2
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Listbox Should Not Contain    ${XPATH_LISTBOX}    ListBox Item #2

Select Listbox Item By Name
    Select Listbox Item By Name    ${XPATH_LISTBOX}    ListBox Item #2
    Listbox Selection Should Be    ${XPATH_LISTBOX}    ListBox Item #2
    Select Listbox Item By Name    ${XPATH_LISTBOX}    ListBox Item #1
    Listbox Selection Should Be    ${XPATH_LISTBOX}    ListBox Item #1

Select Listbox Item By Name Wrong Element
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NAME_NOT_FOUND}    ListBox Item #999
    Run Keyword And Expect Error
    ...    ${EXP_ERR_MSG}
    ...    Select Listbox Item By Name
    ...    ${XPATH_LISTBOX}
    ...    ListBox Item #999

Select Listbox Item By Index
    Select Listbox Item By Index    ${XPATH_LISTBOX}    1
    Listbox Selection Should Be    ${XPATH_LISTBOX}    ListBox Item #2
    Select Listbox Item By Index    ${XPATH_LISTBOX}    0
    Listbox Selection Should Be    ${XPATH_LISTBOX}    ListBox Item #1

Select Listbox Item By Index Negative Number
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ARRAY_OUT_OF_BOUND}    -2000    ${XPATH_LISTBOX}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Select Listbox Item By Index    ${XPATH_LISTBOX}    -2000

Select Listbox Item By Index String Usage
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}    NOT_AN_ARRAY    ${XPATH_LISTBOX}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Select Listbox Item By Index    ${XPATH_LISTBOX}    NOT_AN_ARRAY

Listbox Selection Should Be
    Select Listbox Item By Index    ${XPATH_LISTBOX}    1
    Listbox Selection Should Be    ${XPATH_LISTBOX}    ListBox Item #2

Listbox Selection Should Be Item Not Exist
    Select Listbox Item By Index    ${XPATH_LISTBOX}    1
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ITEM_NOT_SELECTED}    No Such Item
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Listbox Selection Should Be    ${XPATH_LISTBOX}    No Such Item

Get All Names By Listbox
    ${DATA}    Get All Names From Listbox    ${XPATH_LISTBOX}
    VAR    @{EXPECTED_LIST}    ListBox Item \#1    ListBox Item \#2
    Lists Should Be Equal    ${DATA}    ${EXPECTED_LIST}

Get All Texts By Listbox
    ${DATA}    Get All Texts From Listbox    ${XPATH_LISTBOX}
    VAR    @{EXPECTED_LIST}    ListBox Item \#1    ListBox Item \#2
    Lists Should Be Equal    ${DATA}    ${EXPECTED_LIST}
