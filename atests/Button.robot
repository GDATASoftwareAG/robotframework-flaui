*** Settings ***
Documentation       Test suite for combobox keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Collections
Library             Process
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Library             StringFormat
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource

Suite Setup         Init Main Application
Suite Teardown      Stop Application    ${MAIN_PID}


*** Variables ***
${XPATH_COMBO_BOX}      ${MAIN_WINDOW_SIMPLE_CONTROLS}/ComboBox[@AutomationId='NonEditableCombo']
${BUTTON}               ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='InvokableButton']


*** Test Cases ***
Invoke Button Not Invokable
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_INVOKABLE}    ${XPATH_COMBO_BOX}
    Run Keyword And Expect Error    EQUALS: ${EXP_ERR_MSG}    Invoke Button    ${XPATH_COMBO_BOX}

Invoke Button
    Invoke Button    ${BUTTON}
