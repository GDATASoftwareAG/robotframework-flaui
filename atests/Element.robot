*** Settings ***
Documentation       Test suite for element keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Process
Library             String
Library             Collections
Library             DateTime
Library             StringFormat
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource

Suite Setup         Init Main Application
Suite Teardown      Stop Application    ${MAIN_PID}


*** Variables ***
${XPATH_ELEMENT}                ${MAIN_WINDOW_SIMPLE_CONTROLS}/Text[@Name='Test Label']
${XPATH_ENABLE_ELEMENT}         ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='EnableButton']
${XPATH_DISABLED_ELEMENT}       ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='DisabledButton']
${XPATH_OFFSCREEN_ELEMENT}      ${MAIN_WINDOW_SIMPLE_CONTROLS}/Text[@AutomationId='OffscreenTextBlock']
${XPATH_SCROLL_DATAGRID}        ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane[@ClassName='ScrollViewer']/Group[@Name='Large List with Scroll']/DataGrid[@AutomationId='LargeListView']

${XPATH_MFC_APP_MENU_FILE}      ${MAIN_WINDOW_MFC}/Pane[@AutomationId='59419']/Pane[@AutomationId='59398']/MenuItem[@Name='File']


*** Test Cases ***
Focus
    Focus    ${MAIN_WINDOW}

Focus Error
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_FOCUSABLE}    ${XPATH_DISABLED_ELEMENT}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Focus    ${XPATH_DISABLED_ELEMENT}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Get Name From Element By XPath
    ${TEXT}    Get Name From Element    ${XPATH_ELEMENT}
    Should Be Equal    Test Label    ${TEXT}

Get Rectangle Bounding From Element By XPath
    @{RECT}    Get Rectangle Bounding From Element    ${XPATH_ELEMENT}
    Pass Execution If    ${RECT}[0] > 0 and ${RECT}[1] > 0 and ${RECT}[2] > 0 and ${RECT}[3] > 0    Get rectangle bound

Element Should Exist
    ${EXISTS}    Element Should Exist    ${XPATH_ELEMENT}
    Should Be Equal    ${EXISTS}    ${True}

Element Should Exist Xpath Not Exists
    ${EXISTS}    Element Should Exist    ${XPATH_NOT_EXISTS}    ${FALSE}
    Should Be Equal    ${EXISTS}    ${False}

Element Should Not Exist
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_EXISTS}    ${XPATH_ELEMENT}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Element Should Not Exist    ${XPATH_ELEMENT}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Element Should Not Exist Xpath Not Exists
    ${NOT_EXISTS}    Element Should Not Exist    ${XPATH_NOT_EXISTS}    ${FALSE}
    Should Be Equal    ${NOT_EXISTS}    ${TRUE}

Name Should Be
    Name Should Be    ${EXP_WINDOW_TITLE}    ${MAIN_WINDOW}

Name Should Be Wrong Name
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_NAME_NOT_EQUALS}    ${EXP_WINDOW_TITLE}    ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Name Should Be    ${XPATH_NOT_EXISTS}    ${MAIN_WINDOW}

Name Contains Text
    Name Contains Text    Fla    ${MAIN_WINDOW}
    Name Contains Text    WPF    ${MAIN_WINDOW}
    Name Contains Text    Test    ${MAIN_WINDOW}

Name Contains Text Wrong Name
    ${EXP_ERR_MSG}    Format String
    ...    ${EXP_ERR_MSG_NAME_DOES_NOT_CONTAIN}
    ...    ${EXP_WINDOW_TITLE}
    ...    ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Name Contains Text    ${XPATH_NOT_EXISTS}    ${MAIN_WINDOW}

Is Element Enabled
    ${IS_ENABLED}    Is Element Enabled    ${XPATH_ELEMENT}
    Should Be True    ${IS_ENABLED}

Is Element Not Enabled
    ${IS_ENABLED}    Is Element Enabled    ${XPATH_DISABLED_ELEMENT}
    Should Be Equal    ${IS_ENABLED}    ${FALSE}

Element Should Be Enabled
    Element Should Be Enabled    ${XPATH_ELEMENT}

Element Should Be Enabled Error
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_ENABLED}    ${XPATH_DISABLED_ELEMENT}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Element Should Be Enabled    ${XPATH_DISABLED_ELEMENT}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Element Should Be Disabled
    Element Should Be Disabled    ${XPATH_DISABLED_ELEMENT}

Element Should Be Disabled Error
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_DISABLED}    ${XPATH_ELEMENT}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Element Should Be Disabled    ${XPATH_ELEMENT}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Find All Elements
    ${index}    Set Variable    ${0}
    ${elements}    Find All Elements    ${MAIN_WINDOW_CONTROLS}
    Length Should Be    ${elements}    3

    FOR    ${element}    IN    @{elements}
        ${Xpath}    Set Variable    ${element.Xpath}
        ${Id}    Set Variable    ${element.AutomationId}
        ${Name}    Set Variable    ${element.Name}
        ${ClassName}    Set Variable    ${element.ClassName}

        IF    ${index} == ${0}
            Should Contain    ${Xpath}    /Tab/TabItem[1]
            Should Contain    ${Id}    /Tab/TabItem[@AutomationId="SimpleControl"]
            Should Contain    ${Name}    /Tab/TabItem[@Name="Simple Controls"]
            Should Contain    ${ClassName}    /Tab/TabItem[@ClassName="TabItem"]
        END

        IF    ${index} == ${1}
            Should Contain    ${Xpath}    /Tab/TabItem[2]
            Should Contain    ${Id}    ${EMPTY}
            Should Contain    ${Name}    /Tab/TabItem[@Name="Complex Controls"]
            Should Contain    ${ClassName}    /Tab/TabItem[@ClassName="TabItem"]
        END

        IF    ${index} == ${2}
            Should Contain    ${Xpath}    /Tab/TabItem[3]
            Should Contain    ${Id}    ${EMPTY}
            Should Contain    ${Name}    /Tab/TabItem[@Name="Keyboard Controls"]
            Should Contain    ${ClassName}    /Tab/TabItem[@ClassName="TabItem"]
        END

        ${index}    Set Variable    ${index + 1}
    END

Find All Elements Xpath Usage Can Be Used To Any Keyword
    ${elements}    Find All Elements    ${MAIN_WINDOW_CONTROLS}
    Length Should Be    ${elements}    3

    FOR    ${element}    IN    @{elements}
        Element Should Exist    ${element}
    END

Find All Elements Not Supported Exception Should Return Empty String
    ${PID}    Start Application    ${TEST_APP_MFC}
    VAR    ${GLOBAL_VAR}    ${PID}    scope=GLOBAL
    Wait Until Element Exist    ${XPATH_MFC_APP_MENU_FILE}

    ${index}    Set Variable    ${0}
    ${elements}    Find All Elements    ${XPATH_MFC_APP_MENU_FILE}
    Length Should Be    ${elements}    1

    FOR    ${element}    IN    @{elements}
        ${Xpath}    Set Variable    ${element.Xpath}
        ${Id}    Set Variable    ${element.AutomationId}
        ${Name}    Set Variable    ${element.Name}
        ${ClassName}    Set Variable    ${element.ClassName}

        IF    ${index} == ${0}
            Should Not Be Empty    ${Xpath}
            Should Be Empty    ${Id}
            Should Not Be Empty    ${Name}
            Should Be Empty    ${ClassName}
        END

        ${index}    Set Variable    ${index + 1}
    END
    [Teardown]    Stop Application    ${PID}    ${TEST_APP_MFC}

Find All Elements If Xpath Is Wrong
    ${elements}    Find All Elements    /NOT_A_XPATH
    Length Should Be    ${elements}    0

Find One Element
    ${element}   Find One Element    ${XPATH_ENABLE_ELEMENT}

    ${window_xpath}    Fetch From Left    ${element.Xpath}    /Tab

    Should Be Equal    ${element.AutomationId}   ${window_xpath}/Tab/TabItem[1]/Button[@AutomationId="EnableButton"]
    Should Be Equal    ${element.ClassName}    ${window_xpath}/Tab/TabItem[1]/Button[@ClassName="Button"]
    Should Be Equal    ${element.Name}   ${window_xpath}/Tab/TabItem[1]/Button[@Name="Enable Button"]
    Should Be Equal    ${element.Xpath}    ${window_xpath}/Tab/TabItem[1]/Button[6]

Find One Element Not Supported Exception Should Return Empty String
    ${element}   Find One Element    ${XPATH_ELEMENT}

    ${window_xpath}    Fetch From Left    ${element.Xpath}    /Tab

    Should Be Empty    ${element.AutomationId}
    Should Be Equal    ${element.ClassName}    ${window_xpath}/Tab/TabItem[1]/Text[@ClassName="Text"]
    Should Be Equal    ${element.Name}   ${window_xpath}/Tab/TabItem[1]/Text[@Name="Test Label"]
    Should Be Equal    ${element.Xpath}    ${window_xpath}/Tab/TabItem[1]/Text[2]

Find One Element Xpath Usage Can Be Used To Any Keyword
    ${element}   Find One Element    ${XPATH_ENABLE_ELEMENT}
    Element Should Exist    ${element}
    
Find One Element If Xpath Is Wrong
    TRY
        Find One Element    /NOT_A_XPATH
        Fail    'Find One Element' was supposed to fail because the xpath does NOT exist
    EXCEPT    FlaUiError: Element from XPath '/NOT_A_XPATH' could not be found
        Log   'Find One Element' failed as expected
    END

Is Element Offscreen
    ${IS_OFFSCREEN}    Is Element Offscreen    ${XPATH_ELEMENT}
    Should Be Equal    ${IS_OFFSCREEN}    ${False}

Is Element Not Offscreen
    ${IS_OFFSCREEN}    Is Element Offscreen    ${XPATH_OFFSCREEN_ELEMENT}
    Should Be True    ${IS_OFFSCREEN}

Wait Until Element Is Offscreen
    ${PID}    Start Application    ${TEST_APP_NOTIFIER}    ${MAIN_WINDOW_NOTIFIER}
    VAR    ${GLOBAL_VAR}    ${PID}    scope=GLOBAL
    Wait Until Element Is Offscreen    ${MAIN_WINDOW_NOTIFIER}
    Element Should Not Exist    ${MAIN_WINDOW_NOTIFIER}

Wait Until Element Is Offscreen Default Timeout Reached
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_OFFSCREEN}    ${MAIN_WINDOW}
    ${TIME_BEFORE}    Get Current Date
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Is Offscreen    ${MAIN_WINDOW}
    ${TIME_AFTER}    Get Current Date
    ${TOTAL_MS}    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True    ${TOTAL_MS} >= 10
    Should Be True    ${TOTAL_MS} < 11
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Is Offscreen Timeout Reached After One Second
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_OFFSCREEN}    ${MAIN_WINDOW}
    ${TIME_BEFORE}    Get Current Date
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Is Offscreen    ${MAIN_WINDOW}    1
    ${TIME_AFTER}    Get Current Date
    ${TOTAL_MS}    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True    ${TOTAL_MS} >= 1
    Should Be True    ${TOTAL_MS} < 2
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Is Offscreen Wrong Argument
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}    "I'm not a number"
    ${ERR_MSG}    Run Keyword And Expect Error
    ...    *
    ...    Wait Until Element Is Offscreen
    ...    ${MAIN_WINDOW}
    ...    "I'm not a number"
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Is Enabled
    Wait Until Keyword Succeeds    5x    200ms    Ready To Take Off    ${XPATH_ENABLE_ELEMENT}
    Wait Until Element Is Enabled    ${XPATH_DISABLED_ELEMENT}

Wait Until Element Is Enabled Default Timeout Reached
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_ENABLED}    ${XPATH_ENABLE_ELEMENT}
    ${TIME_BEFORE}    Get Current Date
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Is Enabled    ${XPATH_ENABLE_ELEMENT}
    ${TIME_AFTER}    Get Current Date
    ${TOTAL_MS}    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True    ${TOTAL_MS} >= 10
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Is Enabled Timeout Reached After One Second
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_ENABLED}    ${XPATH_ENABLE_ELEMENT}
    ${TIME_BEFORE}    Get Current Date
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Is Enabled    ${XPATH_ENABLE_ELEMENT}    1
    ${TIME_AFTER}    Get Current Date
    ${TOTAL_MS}    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True    ${TOTAL_MS} >= 1
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Is Enabled Timeout Wrong Number
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}    "I'm not a number"
    ${ERR_MSG}    Run Keyword And Expect Error
    ...    *
    ...    Wait Until Element Is Enabled
    ...    ${XPATH_ENABLE_ELEMENT}
    ...    "I'm not a number"
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Does Not Exists
    ${PID}    Start Application    ${TEST_APP_NOTIFIER}    ${MAIN_WINDOW_NOTIFIER}
    VAR    ${GLOBAL_VAR}    ${PID}    scope=GLOBAL
    Wait Until Element Does Not Exist    ${MAIN_WINDOW_NOTIFIER}
    Element Should Not Exist    ${MAIN_WINDOW_NOTIFIER}

Wait Until Element Does Not Exists DeFault Timeout
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_EXISTS}    ${MAIN_WINDOW}
    ${TIME_BEFORE}    Get Current Date
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Does Not Exist    ${MAIN_WINDOW}
    ${TIME_AFTER}    Get Current Date
    ${TOTAL_MS}    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True    ${TOTAL_MS} >= 10
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Does Not Exists Timeout Reached After One Second
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_EXISTS}    ${MAIN_WINDOW}
    ${TIME_BEFORE}    Get Current Date
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Does Not Exist    ${MAIN_WINDOW}    1
    ${TIME_AFTER}    Get Current Date
    ${TOTAL_MS}    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True    ${TOTAL_MS} >= 1
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Does Not Exists Timeout Is Reached By Wrong Number
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}    "I'm not a number"
    ${ERR_MSG}    Run Keyword And Expect Error
    ...    *
    ...    Wait Until Element Does Not Exist
    ...    ${MAIN_WINDOW}
    ...    "I'm not a number"
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Exist
    ${PID}    Start Application With Args    ${TEST_APP_NOTIFIER}    ${MAIN_WINDOW_NOTIFIER}    Delayed
    Wait Until Element Exist    ${MAIN_WINDOW_NOTIFIER}
    Element Should Exist    ${MAIN_WINDOW_NOTIFIER}
    [Teardown]    Stop Application    ${PID}    ${MAIN_WINDOW_NOTIFIER}

Wait Until Element Exist Default Timeout
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_DOES_NOT_EXISTS}    ${MAIN_WINDOW_NOTIFIER}
    ${TIME_BEFORE}    Get Current Date
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Exist    ${MAIN_WINDOW_NOTIFIER}
    ${TIME_AFTER}    Get Current Date
    ${TOTAL_MS}    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True    ${TOTAL_MS} >= 10
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Exist Timeout Reached After One Second
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_DOES_NOT_EXISTS}    ${MAIN_WINDOW_NOTIFIER}
    ${TIME_BEFORE}    Get Current Date
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Exist    ${MAIN_WINDOW_NOTIFIER}    1
    ${TIME_AFTER}    Get Current Date
    ${TOTAL_MS}    Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True    ${TOTAL_MS} >= 1
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait Until Element Exist Timeout Is Reached By Wrong Number
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}    "I'm not a number"
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait Until Element Exist    ${MAIN_WINDOW}    "I'm not a number"
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Element Should Be Offscreen
    [Setup]    Open Complex Tab
    Element Should Be Offscreen    ${XPATH_SCROLL_DATAGRID}/DataItem[4]

Element Should Be Offscreen Error
    [Setup]    Open Complex Tab
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_OFFSCREEN}    ${XPATH_SCROLL_DATAGRID}/Header
    ${ERR_MSG}    Run Keyword And Expect Error    *    Element Should Be Offscreen    ${XPATH_SCROLL_DATAGRID}/Header
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Element Should Not Be Offscreen
    [Setup]    Open Complex Tab
    Element Should Not Be Offscreen    ${XPATH_SCROLL_DATAGRID}/Header

Element Should Not Be Offscreen Error
    [Setup]    Open Complex Tab
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_OFFSCREEN}    ${XPATH_SCROLL_DATAGRID}/DataItem[4]
    ${ERR_MSG}    Run Keyword And Expect Error
    ...    *
    ...    Element Should Not Be Offscreen
    ...    ${XPATH_SCROLL_DATAGRID}/DataItem[4]
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
