*** Settings ***
Documentation   Test suite for radio button keywords.

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/XPath.robot

Suite Setup      Start Application
Suite Teardown   Stop Application

*** Variables ***
${XPATH_RADIO_BUTTON_ONE}  ${MAIN_WINDOW_SIMPLE_CONTROLS}/RadioButton[@AutomationId='RadioButton1']
${XPATH_RADIO_BUTTON_TWO}  ${MAIN_WINDOW_SIMPLE_CONTROLS}/RadioButton[@AutomationId='RadioButton2']

*** Test Cases ***
Get Radiobutton State
    ${STATE}  Get Radiobutton State  ${XPATH_RADIO_BUTTON_ONE}
    Should Be Equal  ${STATE}  ${False}

Select Radiobutton State
    Select Radiobutton  ${XPATH_RADIO_BUTTON_ONE}
    ${STATE}   Get Radiobutton State  ${XPATH_RADIO_BUTTON_ONE}
    ${STATE_2}   Get Radiobutton State  ${XPATH_RADIO_BUTTON_TWO}
    Should Be Equal  ${STATE}    ${True}
    Should Be Equal  ${STATE_2}  ${False}

    Select Radiobutton  ${XPATH_RADIO_BUTTON_TWO}
    ${STATE}   Get Radiobutton State  ${XPATH_RADIO_BUTTON_ONE}
    ${STATE_2}   Get Radiobutton State  ${XPATH_RADIO_BUTTON_TWO}
    Should Be Equal  ${STATE}    ${False}
    Should Be Equal  ${STATE_2}  ${True}

