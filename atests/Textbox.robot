*** Settings ***
Documentation   Test suite for textbox keywords.

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/XPath.robot

Suite Setup      Start Application
Suite Teardown   Stop Application

*** Variables ***
${XPATH_EDIT_BOX}          ${MAIN_WINDOW_SIMPLE_CONTROLS}/Edit[@AutomationId='TextBox']
${EDIT_BOX_TEXT}           Hello I'm Rick
${EDIT_BOX_TEXT_ESCAPED}   Hello I'm Rick\nEscaped
${DEFAULT_VALUE_TEXT_BOX}  Test TextBox

*** Test Cases ***
Get Text From Textbox
    ${TEXT}  Get Text From Textbox  ${XPATH_EDIT_BOX}
    Should Be Equal  ${TEXT}  ${DEFAULT_VALUE_TEXT_BOX}

Set Text To Textbox
    Set Text To Textbox  ${XPATH_EDIT_BOX}   ${EDIT_BOX_TEXT}
    ${TEXT}  Get Text From Textbox  ${XPATH_EDIT_BOX}
    Should Be Equal  ${EDIT_BOX_TEXT}  ${TEXT}

    Set Text To Textbox  ${XPATH_EDIT_BOX}  ${EDIT_BOX_TEXT_ESCAPED}
    ${TEXT}  Get Text From Textbox  ${XPATH_EDIT_BOX}
    Should Be Equal  ${EDIT_BOX_TEXT_ESCAPED}  ${TEXT}
