*** Settings ***
Documentation       Test suite for application keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robo
...

Library             Process
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Library             StringFormat
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource

Suite Setup         Init Main Application
Suite Teardown      Stop Main Application If Running


*** Test Cases ***
Attach Application By Name
    ${PID}    Attach Application By Name    ${TEST_APP}
    Should Not Be Equal As Integers    ${PID}    0

Attach Application By PID
    Attach Application By PID    ${MAIN_PID}

Close Application If Application Is Attached
    Close Application    ${MAIN_PID}
    [Teardown]    Restore Main Application

Launch Application
    [Setup]    Stop Main Application If Running
    ${PID}    Launch Application    ${TEST_APP}
    Should Not Be Equal As Integers    ${PID}    0
    [Teardown]    Run Keywords    Stop Application    ${PID}    AND    Restore Main Application

Launch Application With Arguments
    ${PID}    Launch Application With Args    ${TEST_APP_NOTIFIER}    Hello-World
    Should Not Be Equal As Integers    ${PID}    0
    Wait Until Element Exist    ${MAIN_WINDOW_NOTIFIER}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Name Contains Text    Hello-World    ${MAIN_WINDOW_NOTIFIER}
    [Teardown]    Stop Application    ${PID}    ${MAIN_WINDOW_NOTIFIER}

Close Application By Name
    Close Application By Name    WpfApplication
    ${EXP_ERR_MSG}    Format String    ${EXP_APPLICATION_NOT_FOUND}    ${TEST_APP}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Attach Application By Name    ${TEST_APP}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
    [Teardown]    Restore Main Application

Close Application By Name Without Prior Attach
    [Documentation]    Issue #253: process started outside FlaUI can be closed by name.
    [Setup]    Stop Main Application If Running
    Start Process    ${TEST_APP}
    Wait Until Element Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Close Application By Name    ${TEST_APP}
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    [Teardown]    Run Keywords    Terminate All Processes    kill=True    AND    Restore Main Application

Attach And Close Application By Name Using Path
    [Documentation]    Issue #253: attach and close with the same path used to start the process.
    [Setup]    Stop Main Application If Running
    Start Process    ${TEST_APP}
    Wait Until Element Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Attach Application By Name    ${TEST_APP}
    Close Application By Name    ${TEST_APP}
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    [Teardown]    Run Keywords    Terminate All Processes    kill=True    AND    Restore Main Application

Attach And Close Application By Name Using Exe Suffix
    [Documentation]    Issue #253: attach and close with an .exe suffix from Task Manager.
    [Setup]    Stop Main Application If Running
    Start Process    ${TEST_APP}
    Wait Until Element Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Attach Application By Name    WpfApplication.exe
    Close Application By Name    WpfApplication.exe
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    [Teardown]    Run Keywords    Terminate All Processes    kill=True    AND    Restore Main Application

Attach And Close Application By Name Using Different Case
    [Documentation]    Issue #253: attach and close with different process name casing.
    [Setup]    Stop Main Application If Running
    Start Process    ${TEST_APP}
    Wait Until Element Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Attach Application By Name    wpfapplication
    Close Application By Name    WPFAPPLICATION
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    [Teardown]    Run Keywords    Terminate All Processes    kill=True    AND    Restore Main Application

Attach And Close Two Separate Applications By Name
    [Documentation]    Issue #253: attach and close two different executables by name.
    [Setup]    Stop Main Application If Running
    Start Process    ${TEST_APP}
    Start Process    ${TEST_APP_NOTIFIER}    Hello-World
    Wait Until Element Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Wait Until Element Exist    ${MAIN_WINDOW_NOTIFIER}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Name Contains Text    Hello-World    ${MAIN_WINDOW_NOTIFIER}
    Attach Application By Name    WpfApplication
    Attach Application By Name    Notifier
    Close Application By Name    Notifier
    Wait Until Element Does Not Exist    ${MAIN_WINDOW_NOTIFIER}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Close Application By Name    WpfApplication
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    [Teardown]    Run Keywords    Terminate All Processes    kill=True    AND    Restore Main Application

Wait For Application While Busy By Name Without Timeout
    Wait For Application While Busy By Name    WpfApplication

Wait For Application While Busy By Name With Timeout
    Wait For Application While Busy By Name    WpfApplication    10x    200ms

Wait For Application While Busy By Name Except Error
    ${EXP_ERR_MSG}    Format String    ${EXP_APPLICATION_NOT_FOUND}    ${MISSING_APPLICATION}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait For Application While Busy By Name    ${MISSING_APPLICATION}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait For Application While Busy By PID Without Timeout
    Wait For Application While Busy By PID    ${MAIN_PID}

Wait For Application While Busy By PID With Timeout
    Wait For Application While Busy By PID    ${MAIN_PID}    10x    200ms

Wait For Application While Busy By PID Except Error
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_APP_PID_NOT_FOUND}    -1
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait For Application While Busy By PID    -1
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait For Application Handle By Name Without Timeout
    Wait For Application Handle By Name    WpfApplication

Wait For Application Handle By Name With Timeout
    Wait For Application Handle By Name    WpfApplication    10x    200ms

Wait For Application Handle By Name Except Error
    ${EXP_ERR_MSG}    Format String    ${EXP_APPLICATION_NOT_FOUND}    ${MISSING_APPLICATION}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait For Application Handle By Name    ${MISSING_APPLICATION}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

Wait For Application Handle By PID Without Timeout
    Wait For Application Handle By PID    ${MAIN_PID}

Wait For Application Handle By PID With Timeout
    Wait For Application Handle By PID    ${MAIN_PID}    10x    200ms

Wait For Application Handle By PID Except Error
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_APP_PID_NOT_FOUND}    -1
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait For Application Handle By PID    -1
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
