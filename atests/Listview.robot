*** Settings ***
Documentation   Test suite for list view keywords.

Library         FlaUILibrary  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Suite Setup      Run Keywords  Start Application
...              AND           Click  ${MAIN_WINDOW_COMPLEX_CONTROLS}
Suite Teardown   Stop Application

*** Variables ***
${XPATH_LIST_VIEW}  ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group[@Name='ListView']/DataGrid[@AutomationId='listView1']

*** Test Cases ***
Get Selected Listview Rows If Nothing Is Selected
    ${DATA}  Get Selected Listview Rows  ${XPATH_LIST_VIEW}
    Should Be Empty  ${DATA}

Get Listview Rows Count
    ${COUNT}  Get Listview Rows Count  ${XPATH_LIST_VIEW}
    Should Be Equal As Integers  ${COUNT}  3

Select Listview Row By Index
    Element Should Exist  ${XPATH_LIST_VIEW}
    Select Listview Row By Index  ${XPATH_LIST_VIEW}  1
    ${DATA}  Get Selected Listview Rows  ${XPATH_LIST_VIEW}
    Should Contain  ${DATA}  | 2 | 20 |

Select Listview Item Wrong Index Number
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ARRAY_OUT_OF_BOUND}  -2000  ${XPATH_LIST_VIEW}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Listview Row By Index  ${XPATH_LIST_VIEW}  -2000

Select Listview Item Wrong Index Usage
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  NOT_AN_ARRAY  ${XPATH_LIST_VIEW}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Listview Row By Index  ${XPATH_LIST_VIEW}  NOT_AN_ARRAY

Select Listview Row By Name
    Select Listview Row By Name  ${XPATH_LIST_VIEW}  0  1
    ${DATA}  Get Selected Listview Rows  ${XPATH_LIST_VIEW}
    Should Contain  ${DATA}  | 1 | 10 |

Select Listview Item By Name Wrong Name Or Index
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_LISTVIEW_ITEM_NOT_FOUND}   Simple item which does not exist  -2000
    Run Keyword and Expect Error   ${EXP_ERR_MSG}  Select Listview Row By Name  ${XPATH_LIST_VIEW}  -2000  Simple item which does not exist

Select Listview Item By Name Wrong Index Usage
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  NOT_AN_ARRAY  ${XPATH_LIST_VIEW}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Listview Row By Name  ${XPATH_LIST_VIEW}   NOT_AN_ARRAY   Simple item 1

Select Multiple Listview Row
    Select Listview Row By Name   ${XPATH_LIST_VIEW}  0  1
    Select Listview Row By Index  ${XPATH_LIST_VIEW}  1
    ${DATA}  Get Selected Listview Rows  ${XPATH_LIST_VIEW}
    Should Contain  ${DATA}  | 1 | 10 |
    Should Contain  ${DATA}  | 2 | 20 |
