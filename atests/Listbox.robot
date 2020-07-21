*** Settings ***
Documentation   Test Cases for Component keywords.

Library         FlaUILibrary  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${XPATH_LISTBOX}  ${MAIN_WINDOW_SIMPLE_CONTROLS}/List[@AutomationId='ListBox']


*** Test Cases ***
Get Listbox Items Count
    ${COUNT}  Get Listbox Items Count  ${XPATH_LISTBOX}
    Should Be Equal As Integers  ${COUNT}  2

Get Listbox Items Count Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Get Listbox Items Count  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Get Listbox Items Count XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Get Listbox Items Count  ${XPATH_NOT_EXISTS}

Listbox Should Contain
	Listbox Should Contain  ${XPATH_LISTBOX}  ListBox Item #2

Listbox Should Contain Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Listbox Should Contain  ${XPATH_NOT_EXISTS}  No Such Item  ${CUSTOM_ERR_MSG}

Listbox Should Contain XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Listbox Should Contain  ${XPATH_NOT_EXISTS}  No Such Item
	 
Listbox Should Contain Item Not Exist
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_CONTROL_DOES_NOT_CONTAIN_ITEM}  No Such Item
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Listbox Should Contain  ${XPATH_LISTBOX}  No Such Item

Select Listbox Item By Index
    Select Listbox Item By Index  ${XPATH_LISTBOX}  1
    Listbox Selection Should Be  ${XPATH_LISTBOX}  ListBox Item #2

Select Listbox Item By Index Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Select Listbox Item By Index  ${XPATH_NOT_EXISTS}  0  ${CUSTOM_ERR_MSG}

Select Listbox Item By Index XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Select Listbox Item By Index  ${XPATH_NOT_EXISTS}  0

Select Listbox Item By Index Negative Number
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ARRAY_OUT_OF_BOUND}  -2000  ${XPATH_LISTBOX}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Listbox Item By Index  ${XPATH_LISTBOX}  -2000

Select Listbox Item By Index String Usage
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  NOT_AN_ARRAY  ${XPATH_LISTBOX}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Listbox Item By Index  ${XPATH_LISTBOX}  NOT_AN_ARRAY

Listbox Selection Should Be
    Select Listbox Item By Index  ${XPATH_LISTBOX}  1
    Listbox Selection Should Be  ${XPATH_LISTBOX}  ListBox Item #2

Listbox Selection Should Be Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Listbox Selection Should Be  ${XPATH_NOT_EXISTS}  No Such Item  ${CUSTOM_ERR_MSG}

Listbox Selection Should Be XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Listbox Selection Should Be  ${XPATH_NOT_EXISTS}  No Such Item

Listbox Selection Should Be Item Not Exist
    Select Listbox Item By Index  ${XPATH_LISTBOX}  1
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ITEM_NOT_SELECTED}  No Such Item
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Listbox Selection Should Be  ${XPATH_LISTBOX}  No Such Item
    