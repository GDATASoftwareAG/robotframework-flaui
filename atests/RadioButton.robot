*** Settings ***
Documentation   Test suite for radio button keywords.

Library         FlaUILibrary  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${XPATH_RADIO_BUTTON_ONE}  ${MAIN_WINDOW_SIMPLE_CONTROLS}/RadioButton[@AutomationId='RadioButton1']

*** Test Cases ***
Get Radiobutton State
    ${STATE}  Get Radiobutton State  ${XPATH_RADIO_BUTTON_ONE}
    Should Be Equal  ${STATE}  ${False}

Set Radiobutton State To False
    Set Radiobutton State  ${XPATH_RADIO_BUTTON_ONE}  ${False}
    ${STATE}   Get Radiobutton State  ${XPATH_RADIO_BUTTON_ONE}
    Should Be Equal  ${STATE}  ${False}

Set Radiobutton State To True
    Set Radiobutton State  ${XPATH_RADIO_BUTTON_ONE}  ${True}
    ${STATE}   Get Radiobutton State  ${XPATH_RADIO_BUTTON_ONE}
    Should Be Equal  ${STATE}  ${True}
