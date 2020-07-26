*** Settings ***
Documentation   Test suite for application keywords.

Library         FlaUILibrary
Library         StringFormat

Resource        util/Common.robot
Resource        util/XPath.robot

*** Test Cases ***
Attach Application By Name
    [Setup]    Start Application
    [Teardown]  Stop Application
    Attach Application By Name   ${TEST_APP}

Attach Application By PID
    [Teardown]  Stop Application
    ${PID}  Launch Application  ${TEST_APP}
    Wait Until Keyword Succeeds  10x  200ms  Element Should Exist  ${MAIN_WINDOW}
    Should Not Be Equal As Integers  ${PID}  0
    Attach Application By PID    ${PID}

Close Application If Application Is Attached
    [Setup]    Start Application
    Close Application

Launch Application
    [Teardown]  Stop Application
    ${PID}  Launch Application  ${TEST_APP}
    Should Not Be Equal As Integers  ${PID}  0
