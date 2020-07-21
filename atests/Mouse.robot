*** Settings ***
Documentation   Test Cases for Mouse keywords.

Library         FlaUILibrary
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${EXPECTED_CONTEXT_MENU}   ${MAIN_WINDOW}/Window/Menu
${CLICK_BUTTON}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='InvokableButton']
${RIGHT_CLICK_BUTTON}      ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ContextMenu']
${DOUBLE_CLICK_BUTTON}     ${MAIN_WINDOW_SIMPLE_CONTROLS}/CheckBox[@Name='3-Way Test Checkbox']

*** Test Cases ***

Left Click
    Click  ${CLICK_BUTTON}
    Name Should Be  Invoked!  ${CLICK_BUTTON}

Left Click Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Left Click XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}

Double Click
    Click  ${DOUBLE_CLICK_BUTTON}
    ${STATE}   Get Checkbox State  ${DOUBLE_CLICK_BUTTON}
    Should Be Equal  ${STATE}  ${True}
    Double Click  ${DOUBLE_CLICK_BUTTON}
    ${STATE}   Get Checkbox State  ${DOUBLE_CLICK_BUTTON}
    Should Be Equal  ${STATE}  ${False}

Double Click Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Double Click  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Double Click XPath Not Found
    ${EXP_ERR_MSG} =  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Double Click  ${XPATH_NOT_EXISTS}

Right Click
    Right Click  ${RIGHT_CLICK_BUTTON}
    Element Should Exist  ${EXPECTED_CONTEXT_MENU}

Right Click Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Right Click  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Right Click XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Right Click  ${XPATH_NOT_EXISTS}

Move To
    Move To  ${RIGHT_CLICK_BUTTON}
    Right Click  ${RIGHT_CLICK_BUTTON}
    Element Should Exist  ${EXPECTED_CONTEXT_MENU}

Move To Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Move To  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Move To XPath Not Found
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Move To  ${XPATH_NOT_EXISTS}
