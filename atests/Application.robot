*** Settings ***
Documentation   Test suite for application keywords.
...             XPath not found error handling for all keywords must be implemented under ErrorHandling.robo
...

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         StringFormat

Resource        util/Common.robot
Resource        util/XPath.robot

*** Test Cases ***
Attach Application By Name
    [Setup]     Start Application
    [Teardown]  Stop Application  ${PID}
    ${PID}  Attach Application By Name   ${TEST_APP}
    Should Not Be Equal As Integers  ${PID}  0

Attach Application By PID
    [Teardown]  Stop Application  ${PID}
    ${PID}  Launch Application  ${TEST_APP}
    Wait Until Keyword Succeeds  10x  200ms  Element Should Exist  ${MAIN_WINDOW}
    Should Not Be Equal As Integers  ${PID}  0
    Attach Application By PID    ${PID}

Close Application If Application Is Attached
    ${PID}  Start Application
    Close Application  ${PID}

Launch Application
    [Teardown]  Stop Application  ${PID}
    ${PID}  Launch Application  ${TEST_APP}
    Should Not Be Equal As Integers  ${PID}  0

Launch Application With Arguments
    [Teardown]  Stop Application  ${PID}
    ${PID}  Launch Application With Args  ${TEST_APP_NOTIFIER}  Hello-World
    Should Not Be Equal As Integers  ${PID}  0
    Wait Until Keyword Succeeds  20x  100ms  Name Contains Text  Hello-World   /Window[@Name='Hello-World']
