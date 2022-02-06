*** Settings ***
Documentation   Test suite for application keywords.
...             XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...             Keyword                               Test Case Names
...             Attach Application By Name            Attach Application By Name
...             Attach Application By PID             Attach Application By PID
...             Close Application                     Close Application If Application Is Attached
...             Launch Application                    Launch Application
...             Launch Application With Args          Launch Application With Arguments
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
    ${PID}  Launch Application With Args  ${TEST_APP_NOTIFIER}  Hello- World
    Should Not Be Equal As Integers  ${PID}  0
    Name Contains Text  Hello-World   /Window[@Name='Hello-World']
