*** Settings ***
Documentation   Test Cases for Windows keywords.

Library         FlaUILibrary
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application


*** Test Cases ***
Close Window
    [Teardown]  NONE
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${MAIN_WINDOW}
    Close Window  ${MAIN_WINDOW}
    ${ERR_MSG} =  Run Keyword And Expect Error  *  Element Should Exist  ${MAIN_WINDOW}
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Close Window Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Close Window  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Close Window XPath Not Found
    [Setup]    NONE
    [Teardown]  NONE

    ${EXP_ERR_MSG} =  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${MAIN_WINDOW}
    ${ERR_MSG} =  Run Keyword And Expect Error  *  Close Window  ${MAIN_WINDOW}
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}
