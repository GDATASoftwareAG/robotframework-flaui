*** Settings ***
Documentation   Test suite for window keywords.

Library         FlaUILibrary
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application

*** Test Cases ***
Close Window
    [Teardown]  NONE
    Close Window  ${MAIN_WINDOW}
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${MAIN_WINDOW}
    ${ERR_MSG} =  Run Keyword And Expect Error  *  Element Should Exist  ${MAIN_WINDOW}
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}
