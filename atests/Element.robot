*** Settings ***
Documentation   Test suite for element keywords.
...             XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...             Keyword                                       Test Case Names
...             Element Should Exist                          Element Should Exist
...                                                           Element Should Exist Xpath Not Exists
...             Element Should Not Exist                      Element Should Not Exist
...                                                           Element Should Not Exist Xpath Not Exists
...             Focus                                         Focus
...             Get Name From Element                         Get Name From Element By XPath
...             Get Rectangle Bounding From Element           Get Rectangle Bounding From Element By XPath
...             Name Should Be                                Name Should Be
...                                                           Name Should Be Wrong Name
...             Name Contains Text                            Name Contains Text
...                                                           Name Contains Text Wrong Name
...             Is Element Enabled                            Is Element Enabled
...                                                           Is Element Not Enabled
...             Is Element Visible                            Is Element Visible
...                                                           Is Element Visible When Element Is Offscreen And Not Visible
...             Element Should Be Visible                     Element Should Be Visible
...             Element Should Not Be Visible                 Element Should Not Be Visible
...                                                           Element Should Not Be Visible Error
...             Wait Until Element Is Hidden                  Wait Until Element Is Hidden
...                                                           Wait Until Element Is Hidden Timeout Reached By Default
...                                                           Wait Until Element Is Hidden Timeout Reached After One Second
...                                                           Wait Until Element Is Hidden Timeout Is Reached By Wrong Number
...             Wait Until Element Is VISIBLE                 Wait Until Element Is Visible
...                                                           Wait Until Element Is Hidden Timeout Reached By Default
...                                                           Wait Until Element Is Visible Timeout Reached After Amount Of Time
...                                                           Wait Until Element Is Visible Timeout Is Reached By Wrong Number
...

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         Process
Library         StringFormat
Library         DateTime
Library         Collections

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Suite Setup      Init Main Application
Suite Teardown   Stop Application  ${MAIN_PID}

*** Variables ***
${XPATH_ELEMENT}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/Text[@Name='Test Label']
${XPATH_DISABLED_ELEMENT}   ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='DisabledButton']
${XPATH_OFFSCREEN_ELEMENT}  ${MAIN_WINDOW_SIMPLE_CONTROLS}/Text[@AutomationId='OffscreenTextBlock']

*** Test Cases ***
Focus
    Focus  ${MAIN_WINDOW}

Get Name From Element By XPath
    ${TEXT}  Get Name From Element  ${XPATH_ELEMENT}
    Should Be Equal  Test Label  ${TEXT}

Get Rectangle Bounding From Element By XPath
    @{RECT}  Get Rectangle Bounding From Element  ${XPATH_ELEMENT}
    Pass Execution If  ${RECT}[0] > 0 and ${RECT}[1] > 0 and ${RECT}[2] > 0 and ${RECT}[3] > 0  Get rectangle bound

Element Should Exist
    ${EXISTS}  Element Should Exist  ${XPATH_ELEMENT}
    Should Be Equal  ${EXISTS}  ${True}

Element Should Exist Xpath Not Exists
    ${EXISTS}  Element Should Exist  ${XPATH_NOT_EXISTS}  ${FALSE}
    Should Be Equal  ${EXISTS}  ${False}

Element Should Not Exist
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_EXISTS}  ${XPATH_ELEMENT}
    ${ERR_MSG}      Run Keyword And Expect Error   *  Element Should Not Exist  ${XPATH_ELEMENT}
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Element Should Not Exist Xpath Not Exists
    ${NOT_EXISTS}  Element Should Not Exist  ${XPATH_NOT_EXISTS}  ${FALSE}
    Should Be Equal  ${NOT_EXISTS}  ${TRUE}

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

Is Element Visible When Element Is Offscreen And Not Visible
    ${IS_VISIBLE}  Is Element Visible  ${XPATH_OFFSCREEN_ELEMENT}
    Should Be Equal  ${IS_VISIBLE}  ${False}

Element Should Be Visible
    Element Should Be Visible  ${XPATH_ELEMENT}

Element Should Not Be Visible
    Element Should Not Be Visible  ${XPATH_OFFSCREEN_ELEMENT}

Element Should Not Be Visible Error
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_VISIBLE}  ${XPATH_ELEMENT}
    ${ERR_MSG}      Run Keyword And Expect Error   *  Element Should Not Be Visible  ${XPATH_ELEMENT}
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Hidden
    ${PID}  Start Application       ${TEST_APP_NOTIFIER}  ${MAIN_WINDOW_NOTIFIER}
    Wait Until Element Is Hidden    ${MAIN_WINDOW_NOTIFIER}
    Element Should Not Exist        ${MAIN_WINDOW_NOTIFIER}

Wait Until Element Is Hidden Timeout Reached By Default
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_VISIBLE}  ${MAIN_WINDOW}
    ${TIME_BEFORE}  Get Current Date
    ${ERR_MSG}      Run Keyword And Expect Error   *  Wait Until Element Is Hidden  ${MAIN_WINDOW}
    ${TIME_AFTER}   Get Current Date
    ${TOTAL_MS}     Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True  ${TOTAL_MS} >= 10
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Hidden Timeout Reached After One Second
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_VISIBLE}  ${MAIN_WINDOW}
    ${TIME_BEFORE}  Get Current Date
    ${ERR_MSG}      Run Keyword And Expect Error   *  Wait Until Element Is Hidden  ${MAIN_WINDOW}  1
    ${TIME_AFTER}   Get Current Date
    ${TOTAL_MS}     Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True  ${TOTAL_MS} >= 1
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Hidden Timeout Is Reached By Wrong Number
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  "I'm not a number"
    ${ERR_MSG}      Run Keyword And Expect Error   *  Wait Until Element Is Hidden  ${MAIN_WINDOW}  "I'm not a number"
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Visible
    [Teardown]  Stop Application  ${PID}  ${MAIN_WINDOW_NOTIFIER}
    ${PID}  Start Application With Args  ${TEST_APP_NOTIFIER}  ${MAIN_WINDOW_NOTIFIER}  Delayed
    Wait Until Element Is Visible    ${MAIN_WINDOW_NOTIFIER}
    Element Should Exist             ${MAIN_WINDOW_NOTIFIER}

Wait Until Element Is Visible Timeout Reached By Default
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_NOT_VISIBLE}  ${MAIN_WINDOW_NOTIFIER}
    ${TIME_BEFORE}  Get Current Date
    ${ERR_MSG}      Run Keyword And Expect Error   *  Wait Until Element Is Visible  ${MAIN_WINDOW_NOTIFIER}
    ${TIME_AFTER}   Get Current Date
    ${TOTAL_MS}     Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True  ${TOTAL_MS} >= 10
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Visible Timeout Reached After Amount Of Time
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ELEMENT_NOT_VISIBLE}  ${MAIN_WINDOW_NOTIFIER}
    ${TIME_BEFORE}  Get Current Date
    ${ERR_MSG}      Run Keyword And Expect Error   *  Wait Until Element Is Visible  ${MAIN_WINDOW_NOTIFIER}  1
    ${TIME_AFTER}   Get Current Date
    ${TOTAL_MS}     Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True  ${TOTAL_MS} >= 1
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

Wait Until Element Is Visible Timeout Is Reached By Wrong Number
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  "I'm not a number"
    ${ERR_MSG}      Run Keyword And Expect Error   *  Wait Until Element Is Visible  ${MAIN_WINDOW}  "I'm not a number"
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}
