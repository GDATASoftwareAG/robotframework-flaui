*** Settings ***
Documentation   Test suite for screenshot keywords.

Library         FlaUILibrary  screenshot_on_failure=True
Library         StringFormat
Library         Process
Library         String
Library         OperatingSystem

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Test Application
Test Teardown   Close Test Application

*** Variables ***
${SCREENSHOT_FOLDER} =  screenshots

*** Test Cases ***
Take No Screenshot If Module Is Disabled
    ${FILENAME}  Get Expected Filename  ${TEST_NAME}

    Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}

    ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}

    Take Screenshots On Failure  False
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}

    File Should Not Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}

Take Screenshot If XPath Not Found Multiple Times No Setup Usage
    [Setup]  NONE
    Start Test Application

    Set Screenshot Directory  screenshots
    FOR    ${INDEX}    IN RANGE    1    10
        ${FILENAME}  Get Expected Filename  ${TEST_NAME}  ${INDEX}
        Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
        ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
        File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    END
    Set Screenshot Directory

Take Screenshot If XPath Not Found Multiple Times No Teardown Usage
    [Teardown]  NONE

    Set Screenshot Directory  screenshots
    FOR    ${INDEX}    IN RANGE    1    10
        ${FILENAME}  Get Expected Filename  ${TEST_NAME}  ${INDEX}
        Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
        ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
        File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    END
    Set Screenshot Directory
    Close Test Application

Take Screenshot If XPath Not Found Multiple Times No Teardown And Setup Usage
    [Setup]  NONE
    [Teardown]  NONE

    Start Test Application
    Set Screenshot Directory  screenshots
    FOR    ${INDEX}    IN RANGE    1    10
        ${FILENAME}  Get Expected Filename  ${TEST_NAME}  ${INDEX}
        Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
        ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
        File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    END
    Set Screenshot Directory
    Close Test Application

Take Screenshot If XPath Not Found Multiple Times
    Set Screenshot Directory  screenshots
    FOR    ${INDEX}    IN RANGE    1    10
        ${FILENAME}  Get Expected Filename  ${TEST_NAME}  ${INDEX}
        Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
        ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
        File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    END
    Set Screenshot Directory

Take Screenshot If XPath Not Found Multiple Times Default Folder
    FOR    ${INDEX}    IN RANGE    1    10
        ${FILENAME}  Get Expected Filename  ${TEST_NAME}  ${INDEX}
        Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
        ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
        File Should Exist  ${OUTPUT DIR}/${FILENAME}
    END

Take Screenshot If XPath Not Found
    Set Screenshot Directory  screenshots
    ${FILENAME}  Get Expected Filename  ${TEST_NAME}

    Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
    File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory

Take Manual Screenshot By Keyword
    Set Screenshot Directory  screenshots
    ${FILENAME}  Get Expected Filename  ${TEST_NAME}

    Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshots On Failure  False
    ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
    File Should Not Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshot
    File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory

Set Screenshot Directory
    ${SCREENSHOT_FOLDER}  Set Variable  screenshots_test
    ${FILENAME}  Get Expected Filename  ${TEST_NAME}

    Set Screenshot Directory  ${SCREENSHOT_FOLDER}
    Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    ${EXP_ERR_MSG} =  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
    File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}

    ${SCREENSHOT_FOLDER} =  Set Variable  screenshots
    Set Screenshot Directory  ${SCREENSHOT_FOLDER}

Create Screenshot From Desktop By A Setup Fail
    [Setup]    Force To Fail
    [Teardown]  NONE
    Log  Test should fail in setup

Create Screenshot From Desktop By A Teardown Fail
    [Setup]    NONE
    [Teardown]  Force To Fail
    Log  Test should fail in teardown

*** Keywords ***
Close Test Application
    Stop Application
    Take Screenshots On Failure  False

Start Test Application
    Take Screenshots On Failure  False
    Start Application
    Take Screenshots On Failure  True

Get Expected Filename
    [Arguments]   ${TEST_NAME}  ${INDEX}=1
    ${FILENAME} =  Convert To Lowercase  ${TEST_NAME}
    ${HOSTNAME} =  Convert To Lowercase  %{COMPUTERNAME}

    Should Be Lowercase  ${FILENAME}

    ${FILENAME} =  Replace String  ${FILENAME}  ${space}  _
    ${FILENAME} =  Catenate  SEPARATOR=_  ${HOSTNAME}   ${FILENAME}
    ${FILENAME} =  Catenate  SEPARATOR=_  test   ${FILENAME}
    ${FILENAME} =  Catenate  SEPARATOR=_  ${FILENAME}  ${INDEX}
    ${FILENAME} =  Catenate  SEPARATOR=.  ${FILENAME}   jpg

    [Return]  ${FILENAME}

Force To Fail
    Take Screenshots On Failure  True
    ${FILENAME} =  Get Expected Filename  ${TEST_NAME}
    Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    File Should Not Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Run Keyword And Ignore Error  Fail  You Shall Not Pass

    ${FILENAME} =  Get Expected Filename  ${TEST_NAME}
    File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshots On Failure  False
