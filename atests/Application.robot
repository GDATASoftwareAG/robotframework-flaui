*** Settings ***
Documentation   Test cases for application keywords.

Library         FlaUILibrary
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Test Cases ***
Attach Application By Name
    Attach Application By Name   ${TEST_APP}

Attach Application Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Attach Application By Name  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Attach Application By Wrong Name
    [Setup]    NONE
    [Teardown]  NONE

    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_APP_NAME_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Attach Application By Name  ${XPATH_NOT_EXISTS}

Attach Application By PID
    [Setup]    NONE

    ${PID}  Launch Application  ${TEST_APP}
    Wait Until Keyword Succeeds  10x  200ms  Element Should Exist  ${MAIN_WINDOW}
    Should Not Be Equal As Integers  ${PID}  0
    Attach Application By PID    ${PID}

Attach Application By PID Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Attach Application By PID   ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Attach Application By Wrong PID
    [Setup]    NONE
    [Teardown]  NONE

    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_PID_NOT_FOUND}  ${WRONG_PID}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Attach Application By PID  ${WRONG_PID}

Close Application If Application Is Attached
    [Teardown]  NONE

    Close Application

Close Application Custom Error Message
    [Setup]    NONE
    [Teardown]  NONE

    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Close Application  ${CUSTOM_ERR_MSG}

Close Application If No Application Is Attached
    [Setup]    NONE
    [Teardown]  NONE

    Run Keyword And Expect Error  ${EXP_ERR_MSG_APP_NOT_ATTACHED}  Close Application

Launch Application
    [Setup]    NONE

    ${PID}  Launch Application  ${TEST_APP}
    Should Not Be Equal As Integers  ${PID}  0

Launch Application Not Exist Custom Error Message
    [Setup]    NONE
    [Teardown]  NONE

    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Launch Application   ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Launch Application Not Exist
    [Setup]    NONE
    [Teardown]  NONE

    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_APP_NOT_EXIST}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Launch Application  ${XPATH_NOT_EXISTS}
