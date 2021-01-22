*** Settings ***
Documentation   Test suite for debug keywords.

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/XPath.robot

Suite Setup      Start Application
Suite Teardown   Stop Application

*** Test Cases ***
Get Childs From Element
    ${CHILDS}  Get Childs From Element  ${MAIN_WINDOW}
    Should Contain  ${CHILDS}  AutomationId:, Name:FlaUI WPF Test App
    Should Contain  ${CHILDS}  ------> AutomationId:TitleBar, Name:
    Should Contain X Times  ${CHILDS}  ------>  4
    Should Contain X Times  ${CHILDS}  AutomationId  5

Get UIA Identifier
   ${IDENTIFIER}  Get Uia Identifier
   Should Be Equal  ${IDENTIFIER}  ${UIA}