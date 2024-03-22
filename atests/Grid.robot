*** Settings ***
Documentation   Test suite for grid ui keyword usage.
...

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         Process
Library         StringFormat
Library         Collections

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Suite Setup      Run Keywords  Init Main Application
...              AND           Open Complex Tab
Suite Teardown   Stop Application  ${MAIN_PID}

*** Variables ***
${XPATH_GRID_VIEW}  ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group[@Name='Grid']/DataGrid[@AutomationId='dataGridView']

*** Test Cases ***
Get All Data From Grid
    ${DATA}  Get All Data From Grid  ${XPATH_GRID_VIEW}
    List Should Contain Value    ${DATA}[0]  Name
    List Should Contain Value    ${DATA}[0]  Number
    List Should Contain Value    ${DATA}[0]  IsChecked
    List Should Contain Value    ${DATA}[1]  John
    List Should Contain Value    ${DATA}[1]  12
    List Should Contain Value    ${DATA}[2]  Doe
    List Should Contain Value    ${DATA}[2]  24

Get Header From Grid
    ${DATA}  Get Header From Grid  ${XPATH_GRID_VIEW}
    Should Be Equal    ${DATA}[0]  Name
    Should Be Equal    ${DATA}[1]  Number
    Should Be Equal    ${DATA}[2]  IsChecked


Get Selected Grid Rows If Nothing Is Selected
    ${DATA}  Get Selected Grid Rows  ${XPATH_GRID_VIEW}
    Should Be Empty  ${DATA}

Get Grid Rows Count
    ${COUNT}  Get Grid Rows Count  ${XPATH_GRID_VIEW}
    Should Be Equal As Integers  ${COUNT}  3

Select Grid Row By Index
    Element Should Exist  ${XPATH_GRID_VIEW}
    Select Grid Row By Index  ${XPATH_GRID_VIEW}  1
    ${DATA}  Get Selected Grid Rows  ${XPATH_GRID_VIEW}
    Should Contain  ${DATA}  | Doe | 24 |

Select Grid Row By Index With Wrong Index Number
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ARRAY_OUT_OF_BOUND}  -2000  ${XPATH_GRID_VIEW}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Grid Row By Index  ${XPATH_GRID_VIEW}  -2000

Select Grid Row By Index With Wrong Index Usage
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  NOT_AN_ARRAY  ${XPATH_GRID_VIEW}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Grid Row By Index  ${XPATH_GRID_VIEW}  NOT_AN_ARRAY

Select Grid Row By Name
    Select Grid Row By Name  ${XPATH_GRID_VIEW}  0  Doe
    ${DATA}  Get Selected Grid Rows  ${XPATH_GRID_VIEW}
    Should Contain  ${DATA}  | Doe | 24 |

Select Grid Row By Name Wrong Name Or Index
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_LISTVIEW_ITEM_NOT_FOUND}   Simple item which does not exist  -2000
    Run Keyword and Expect Error   ${EXP_ERR_MSG}  Select Grid Row By Name  ${XPATH_GRID_VIEW}  -2000  Simple item which does not exist

Select Grid Row By Name Wrong Index Usage
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  NOT_AN_ARRAY  ${XPATH_GRID_VIEW}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Grid Row By Name  ${XPATH_GRID_VIEW}   NOT_AN_ARRAY   Simple item 1

Select Multiple Grid Items
    Select Grid Row By Name   ${XPATH_GRID_VIEW}  0  Doe
    Select Grid Row By Index  ${XPATH_GRID_VIEW}  0
    ${DATA}  Get Selected Grid Rows  ${XPATH_GRID_VIEW}
    Should Contain  ${DATA}  | John | 12 |
    Should Contain  ${DATA}  | Doe | 24 |
