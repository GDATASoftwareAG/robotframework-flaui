*** Settings ***
Documentation       Test suite for screenshot keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Process
Library             String
Library             OperatingSystem
Library             StringFormat
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=True    AS    FLA
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource


*** Variables ***
${SCREENSHOT_FOLDER}    screenshots/alias


*** Test Cases ***
Take No Screenshot If Module Is Disabled
    ${FILENAME}    Get Expected Filename    ${TEST_NAME}
    Remove File    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
    Take Screenshots On Failure    ${False}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    [Teardown]    Reset Screenshot Environment To Default

Take Screenshot If XPath Not Found Multiple Times Default Folder
    FOR    ${_}    IN RANGE    1    3
        ${FILENAME}    Get Expected Filename    ${TEST_NAME}
        ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
        Wait Until Created    ${OUTPUT DIR}/${FILENAME}    1s
    END
    [Teardown]    Reset Screenshot Environment To Default

Take Screenshot If XPath Not Found Multiple Times By Specific Folder
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    FOR    ${_}    IN RANGE    1    3
        ${FILENAME}    Get Expected Filename    ${TEST_NAME}
        ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
        Wait Until Created    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}    1s
    END
    [Teardown]    Reset Screenshot Environment To Default

Take Manual Screenshot By Keyword
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    ${TEST_NAME}
    Remove File    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshots On Failure    ${False}
    ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshot
    File Should Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    [Teardown]    Reset Screenshot Environment To Default

Test Case 1234: Something to Test
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    Test Case 1234 Something to Test

    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshot
    File Should Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    [Teardown]    Reset Screenshot Environment To Default

No Screenshots Should Created For No Library Keywords
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    No Screenshots Should Created For No Library Keywords
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Run Keyword And Ignore Error    Fail    You Should Not Pass
    Run Keyword And Ignore Error    Wait Until Keyword Succeeds    5x    10ms    Fail    You Should Not Pass
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    [Teardown]    Reset Screenshot Environment To Default

Take Screenshot Of Window
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    ${TEST_NAME}
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshot    ${MAIN_WINDOW}
    File Should Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    [Teardown]    Reset Screenshot Environment To Default    ${PID}

Take Screenshot As Base64
    Set Screenshot Log Mode    Base64
    ${base64}    Take Screenshot
    Should Not Be Equal    ${base64}    ${None}    Returned base64 image is 'None'
    Should Not Be Empty    ${base64}    Returned base64 image is empty
    [Teardown]    Reset Screenshot Environment To Default

Take Screenshot Of Window As Base64
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    Set Screenshot Log Mode    Base64
    ${base64}    Take Screenshot    ${MAIN_WINDOW}
    Should Not Be Equal    ${base64}    ${None}    Returned base64 image is 'None'
    Should Not Be Empty    ${base64}    Returned base64 image is empty
    [Teardown]    Reset Screenshot Environment To Default    ${PID}


*** Keywords ***
Get Expected Filename
    [Arguments]    ${TEST_FILENAME}
    ${FILENAME}    Convert To Lowercase    ${TEST_FILENAME}
    ${HOSTNAME}    Convert To Lowercase    %{COMPUTERNAME}

    Should Be Lowercase    ${FILENAME}

    ${FILENAME}    Replace String    ${FILENAME}    ${space}    _
    ${FILENAME}    Catenate    SEPARATOR=_    ${HOSTNAME}    ${FILENAME}
    ${FILENAME}    Catenate    SEPARATOR=_    test    ${FILENAME}
    ${FILENAME}    Catenate    SEPARATOR=_    ${FILENAME}    [0-9]*
    ${FILENAME}    Catenate    SEPARATOR=.    ${FILENAME}    jpg

    RETURN    ${FILENAME}

Reset Screenshot Environment To Default
    [Documentation]    Reset screenshot environment to default and initial settings.
    [Arguments]    ${pid}=${None}
    Set Screenshot Log Mode    File
    Take Screenshots On Failure    ${True}
    Set Screenshot Directory
    Run Keyword And Ignore Error    Stop Application    ${pid}
