*** Settings ***
Documentation   Test suite for checkbox keywords.

Library         FlaUILibrary
Library         StringFormat

Resource        util/Common.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${XPATH_CHECKBOX}  ${MAIN_WINDOW_SIMPLE_CONTROLS}/CheckBox[@AutomationId='SimpleCheckBox']

*** Test Cases ***
Get Checkbox State
    ${STATE}  Get Checkbox State  ${XPATH_CHECKBOX}
    Should Be Equal  ${STATE}  ${False}

Set Checkbox State To False
    Set Checkbox State  ${XPATH_CHECKBOX}  ${False}
    ${STATE}   Get Checkbox State  ${XPATH_CHECKBOX}
    Should Be Equal  ${STATE}  ${False}

Set Checkbox State To True
    Set Checkbox State  ${XPATH_CHECKBOX}  ${True}
    ${STATE}   Get Checkbox State  ${XPATH_CHECKBOX}
    Should Be Equal  ${STATE}  ${True}
