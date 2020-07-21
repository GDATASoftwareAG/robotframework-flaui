*** Settings ***
Documentation   Test cases for combobox keywords.

Library         FlaUILibrary
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Test Cases ***
Get Childs From Element
    ${CHILDS}  Get Childs From Element  ${MAIN_WINDOW}
    Should Contain  ${CHILDS}  AutomationId:, Name:FlaUI WPF Test App
    Should Contain  ${CHILDS}  ------> AutomationId:TitleBar, Name:
    Should Contain X Times  ${CHILDS}  ------>  4
    Should Contain X Times  ${CHILDS}  AutomationId  5

Get Childs From Element Wrong XPATH
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Get Childs From Element  ${XPATH_NOT_EXISTS}