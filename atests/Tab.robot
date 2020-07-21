*** Settings ***
Documentation   Test Cases for Component keywords.

Library         FlaUILibrary
Library         StringFormat
Library         Collections

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${XPATH_TAB}                                   ${MAIN_WINDOW}/Tab
${TAB_ITEM_LIST_CONTROLS}                      Complex Controls
${TAB_ITEM_LIST_CONTROLS_WITH_NO_BREAK_SPACE}  Complex\xa0Controls
${TAB_ITEM_NOT_PRESENT}                        Not Present

*** Test Cases ***
Tab Should Contain List Controls TabItem
    @{CHILD_TAB_ITEMS}  Get Tab Items Names  ${XPATH_TAB}
    List Should Contain Value   ${CHILD_TAB_ITEMS}   ${TAB_ITEM_LIST_CONTROLS}

Tab Should Not Contain List Controls With No Break Space TabItem
    @{CHILD_TAB_ITEMS}  Get Tab Items Names  ${XPATH_TAB}
    List Should Not Contain Value   ${CHILD_TAB_ITEMS}   ${TAB_ITEM_LIST_CONTROLS_WITH_NO_BREAK_SPACE}

Tab Should Not Contain Not Present TabItem
    @{CHILD_TAB_ITEMS}  Get Tab Items Names  ${XPATH_TAB}
    List Should Not Contain Value   ${CHILD_TAB_ITEMS}   ${TAB_ITEM_NOT_PRESENT}

Get Tab Items Names Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Get Tab Items Names  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Get Tab Items Names Count XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Get Tab Items Names  ${XPATH_NOT_EXISTS}

Select Tab Item By Name
    Select Tab Item By Name   ${XPATH_TAB}  ${TAB_ITEM_LIST_CONTROLS}
    Element Should Exist      ${MAIN_WINDOW_COMPLEX_CONTROLS}

Select Tab Itemt By Name Not Exist
    ${EXP_ERR_MSG}  Format String  ${EXP_GENERIC_ERR_MSG}  No TabItem found with text 'Tab Not Exist'
    ${ERR_MSG} =  Run Keyword And Expect Error   *  Select Tab Item By Name  ${XPATH_TAB}  Tab Not Exist
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Select Tab Item By Name XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    ${ERR_MSG} =  Run Keyword And Expect Error   *  Select Tab Item By Name   ${XPATH_NOT_EXISTS}  Other Controls
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Select Tab Item By Name XPath Not Found Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Select Tab Item By Name  ${XPATH_NOT_EXISTS}  Other Controls  ${CUSTOM_ERR_MSG}