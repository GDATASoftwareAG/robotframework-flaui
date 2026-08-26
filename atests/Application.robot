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


*** Test Cases ***
Attach Application By Name
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    Should Not Be Equal As Integers    ${PID}    0
    [Teardown]    Stop Application    ${PID}

Attach Application By PID
    ${PID}    Launch Application    ${TEST_APP}
    Wait Until Keyword Succeeds    10x    200ms    Element Should Exist    ${MAIN_WINDOW}
    Should Not Be Equal As Integers    ${PID}    0
    Attach Application By PID    ${PID}
    [Teardown]    Stop Application    ${PID}

Close Application If Application Is Attached
    ${PID}    Start Application
    Close Application    ${PID}

Launch Application
    ${PID}    Launch Application    ${TEST_APP}
    Should Not Be Equal As Integers    ${PID}    0
    [Teardown]    Stop Application    ${PID}

Launch Application With Arguments
    ${PID}    Launch Application With Args    ${TEST_APP_NOTIFIER}    Hello-World
    Should Not Be Equal As Integers    ${PID}    0
    Wait Until Keyword Succeeds    20x    100ms    Name Contains Text    Hello-World    /Window[@Name='Hello-World']
    [Teardown]    Stop Application    ${PID}

Close Application By Name
    [Setup]    Start Application
    Close Application By Name    WpfApplication
    ${EXP_ERR_MSG}    Format String    ${EXP_APPLICATION_NOT_FOUND}    ${TEST_APP}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Attach Application By Name    ${TEST_APP}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
    [Teardown]    Run Keyword And Ignore Error    Stop Application    ${PID}

Close Application By Name Without Prior Attach
    [Documentation]    Issue #253: process started outside FlaUI can be closed by name.
    Start Process    ${TEST_APP}
    Wait Until Keyword Succeeds    10x    200ms    Element Should Exist    ${MAIN_WINDOW}
    Close Application By Name    ${TEST_APP}
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}
    [Teardown]    Run Keyword And Ignore Error    Terminate All Processes    kill=True

Attach And Close Application By Name Using Path
    [Documentation]    Issue #253: attach and close with the same path used to start the process.
    Start Process    ${TEST_APP}
    Wait Until Keyword Succeeds    10x    200ms    Element Should Exist    ${MAIN_WINDOW}
    Attach Application By Name    ${TEST_APP}
    Close Application By Name    ${TEST_APP}
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}
    [Teardown]    Run Keyword And Ignore Error    Terminate All Processes    kill=True

Attach And Close Application By Name Using Exe Suffix
    [Documentation]    Issue #253: attach and close with an .exe suffix from Task Manager.
    Start Process    ${TEST_APP}
    Wait Until Keyword Succeeds    10x    200ms    Element Should Exist    ${MAIN_WINDOW}
    Attach Application By Name    WpfApplication.exe
    Close Application By Name    WpfApplication.exe
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}
    [Teardown]    Run Keyword And Ignore Error    Terminate All Processes    kill=True

Attach And Close Application By Name Using Different Case
    [Documentation]    Issue #253: attach and close with different process name casing.
    Start Process    ${TEST_APP}
    Wait Until Keyword Succeeds    10x    200ms    Element Should Exist    ${MAIN_WINDOW}
    Attach Application By Name    wpfapplication
    Close Application By Name    WPFAPPLICATION
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}
    [Teardown]    Run Keyword And Ignore Error    Terminate All Processes    kill=True

Attach And Close Two Separate Applications By Name
    [Documentation]    Issue #253: attach and close two different executables by name.
    Start Process    ${TEST_APP}
    Start Process    ${TEST_APP_NOTIFIER}    Hello-World
    Wait Until Keyword Succeeds    10x    200ms    Element Should Exist    ${MAIN_WINDOW}
    Wait Until Keyword Succeeds    20x    100ms    Name Contains Text    Hello-World    ${MAIN_WINDOW_NOTIFIER}
    Attach Application By Name    WpfApplication
    Attach Application By Name    Notifier
    Close Application By Name    Notifier
    Wait Until Element Does Not Exist    ${MAIN_WINDOW_NOTIFIER}
    Close Application By Name    WpfApplication
    Wait Until Element Does Not Exist    ${MAIN_WINDOW}
    [Teardown]    Run Keyword And Ignore Error    Terminate All Processes    kill=True

Wait For Application While Busy By Name Without Timeout
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${RESULT}    Wait For Application While Busy By Name    WpfApplication
    Should Be True    ${RESULT}
    [Teardown]    Stop Application    ${PID}

Wait For Application While Busy By Name With Timeout
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${RESULT}    Wait For Application While Busy By Name    WpfApplication    1000
    Should Be True    ${RESULT}
    [Teardown]    Stop Application    ${PID}

Wait For Application While Busy By Name Except Error
    [Setup]    Start Application
    Close Application By Name    WpfApplication
    ${EXP_ERR_MSG}    Format String    ${EXP_APPLICATION_NOT_FOUND}    ${TEST_APP}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait For Application While Busy By Name    ${TEST_APP}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
    [Teardown]    Run Keyword And Ignore Error    Stop Application    ${PID}

Wait For Application While Busy By PID Without Timeout
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${RESULT}    Wait For Application While Busy By PID    ${PID}
    Should Be True    ${RESULT}
    [Teardown]    Stop Application    ${PID}

Wait For Application While Busy By PID With Timeout
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${RESULT}    Wait For Application While Busy By PID    ${PID}    1000
    Should Be True    ${RESULT}
    [Teardown]    Stop Application    ${PID}

Wait For Application While Busy By PID Except Error
    [Setup]    Start Application
    Close Application By Name    WpfApplication
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_APP_PID_NOT_FOUND}    -1
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait For Application While Busy By PID    -1
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
    [Teardown]    Run Keyword And Ignore Error    Stop Application    ${PID}

Wait For Application Handle By Name Without Timeout
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${RESULT}    Wait For Application Handle By Name    WpfApplication
    Should Be True    ${RESULT}
    [Teardown]    Stop Application    ${PID}

Wait For Application Handle By Name With Timeout
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${RESULT}    Wait For Application Handle By Name    WpfApplication    1000
    Should Be True    ${RESULT}
    [Teardown]    Stop Application    ${PID}

Wait For Application Handle By Name Except Error
    [Setup]    Start Application
    Close Application By Name    WpfApplication
    ${EXP_ERR_MSG}    Format String    ${EXP_APPLICATION_NOT_FOUND}    ${TEST_APP}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait For Application Handle By Name    ${TEST_APP}
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
    [Teardown]    Run Keyword And Ignore Error    Stop Application    ${PID}

Wait For Application Handle By PID Without Timeout
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${RESULT}    Wait For Application Handle By PID    ${PID}
    Should Be True    ${RESULT}
    [Teardown]    Stop Application    ${PID}

Wait For Application Handle By PID With Timeout
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    ${RESULT}    Wait For Application Handle By PID    ${PID}    1000
    Should Be True    ${RESULT}
    [Teardown]    Stop Application    ${PID}

Wait For Application Handle By PID Except Error
    [Setup]    Start Application
    Close Application By Name    WpfApplication
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_APP_PID_NOT_FOUND}    -1
    ${ERR_MSG}    Run Keyword And Expect Error    *    Wait For Application Handle By PID    -1
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
    [Teardown]    Run Keyword And Ignore Error    Stop Application    ${PID}
