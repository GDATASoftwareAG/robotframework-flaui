*** Settings ***
Documentation   Test Cases for Component keywords.

Library         FlaUILibrary
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${XPATH_EDIT_BOX}          ${MAIN_WINDOW_SIMPLE_CONTROLS}/Edit[@AutomationId='TextBox']
${EDIT_BOX_TEXT}           Hello I'm Rick
${EDIT_BOX_TEXT_ESCAPED}   Hello I'm Rick\nEscaped
${DEFAULT_VALUE_TEXT_BOX}  Test TextBox

*** Test Cases ***
Get Text From Textbox
    ${TEXT}  Get Text From Textbox  ${XPATH_EDIT_BOX}
    Should Be Equal  ${TEXT}  ${DEFAULT_VALUE_TEXT_BOX}

Get Text From Textbox XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Get Text From Textbox  ${XPATH_NOT_EXISTS}

Set Text To Textbox
    Set Text To Textbox  ${XPATH_EDIT_BOX}   ${EDIT_BOX_TEXT}
    ${TEXT}  Get Text From Textbox  ${XPATH_EDIT_BOX}
    Should Be Equal  ${EDIT_BOX_TEXT}  ${TEXT}

    Set Text To Textbox  ${XPATH_EDIT_BOX}  ${EDIT_BOX_TEXT_ESCAPED}
    ${TEXT}  Get Text From Textbox  ${XPATH_EDIT_BOX}
    Should Be Equal  ${EDIT_BOX_TEXT_ESCAPED}  ${TEXT}

Set Text To Textbox XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Set Text To Textbox  ${XPATH_NOT_EXISTS}  ${EDIT_BOX_TEXT}
