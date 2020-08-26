*** Settings ***
Documentation   Test suite for element keywords.

Library         FlaUILibrary
Library         Process
Library         StringFormat
Library         DateTime

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Suite Setup      Start Application
Suite Teardown   Stop Application

*** Variables ***
${XPATH_ELEMENT}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/Text[@Name='Test Label']
${XPATH_DISABLED_ELEMENT}   ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='DisabledButton']
${XPATH_OFFSCREEN_ELEMENT}  ${MAIN_WINDOW_SIMPLE_CONTROLS}/Text[@AutomationId='OffscreenTextBlock']

*** Test Cases ***
Focus
    Focus  ${MAIN_WINDOW}

Get Name From Element By XPath
    ${TEXT} =  Get Name From Element  ${XPATH_ELEMENT}
    Should Be Equal  Test Label  ${TEXT}

Element Should Exist
    Element Should Exist  ${XPATH_ELEMENT}

Element Should Not Exist
    Element Should Not Exist  ${XPATH_NOT_EXISTS}

Element Should Not Exist Error
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_EXISTS}  ${XPATH_ELEMENT}
    ${ERR_MSG} =  Run Keyword And Expect Error  *  Element Should Not Exist  ${XPATH_ELEMENT}
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Name Should Be
    Name Should Be    ${EXP_WINDOW_TITLE}  ${MAIN_WINDOW}

Name Should Be Wrong Name
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_NAME_NOT_EQUALS}  ${EXP_WINDOW_TITLE}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Name Should Be  ${XPATH_NOT_EXISTS}  ${MAIN_WINDOW}

Name Contains Text
    Name Contains Text  Fla   ${MAIN_WINDOW}
    Name Contains Text  WPF   ${MAIN_WINDOW}
    Name Contains Text  Test  ${MAIN_WINDOW}

Name Contains Text Wrong Name
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_NAME_DOES_NOT_CONTAIN}  ${EXP_WINDOW_TITLE}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Name Contains Text  ${XPATH_NOT_EXISTS}  ${MAIN_WINDOW}

Is Element Enabled
    ${IS_ENABLED}  Is Element Enabled  ${XPATH_ELEMENT}
    Should Be True  ${IS_ENABLED}

Is Element Not Enabled
    ${IS_ENABLED}  Is Element Enabled  ${XPATH_DISABLED_ELEMENT}
    Should Be Equal  ${IS_ENABLED}  ${FALSE}

Is Element Visible
    ${IS_VISIBLE}  Is Element Visible  ${XPATH_ELEMENT}
    Should Be True  ${IS_VISIBLE}

Is Element Offscreen And Not Visible
    ${IS_VISIBLE}  Is Element Visible  ${XPATH_OFFSCREEN_ELEMENT}
    Should Be Equal  ${IS_VISIBLE}  ${False}

Element Should Be Visible
    Element Should Be Visible  ${XPATH_ELEMENT}

Element Should Not Be Visible
    Element Should Not Be Visible  ${XPATH_OFFSCREEN_ELEMENT}

Element Should Not Be Visible Error
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_VISIBLE}  ${XPATH_ELEMENT}
    ${ERR_MSG} =  Run Keyword And Expect Error   *  Element Should Not Be Visible  ${XPATH_ELEMENT}
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Hidden
    [Setup]    Start Application    ${TEST_APP_NOTIFIER}  ${MAIN_WINDOW_NOTIFIER}
    Wait Until Element Is Hidden    ${MAIN_WINDOW_NOTIFIER}
    Element Should Not Exist        ${MAIN_WINDOW_NOTIFIER}

Wait Until Element Is Hidden Timeout Reached By Default
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_VISIBLE}  ${MAIN_WINDOW}
    ${TIME_BEFORE} =    Get Current Date
    ${ERR_MSG} =  Run Keyword And Expect Error   *  Wait Until Element Is Hidden  ${MAIN_WINDOW}
    ${TIME_AFTER} =    Get Current Date
    ${TOTAL_MS} =    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True  ${TOTAL_MS} >= 10
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Hidden Timeout Reached After One Second
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_VISIBLE}  ${MAIN_WINDOW}
    ${TIME_BEFORE} =    Get Current Date
    ${ERR_MSG} =  Run Keyword And Expect Error   *  Wait Until Element Is Hidden  ${MAIN_WINDOW}  1
    ${TIME_AFTER} =    Get Current Date
    ${TOTAL_MS} =    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True  ${TOTAL_MS} >= 1
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Hidden Timeout Reached Wrong Number Type
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  "I'm not a number"
    ${ERR_MSG} =  Run Keyword And Expect Error   *  Wait Until Element Is Hidden  ${MAIN_WINDOW}  "I'm not a number"
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}
