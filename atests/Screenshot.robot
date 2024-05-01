*** Settings ***
Documentation       Test suite for screenshot keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Process
Library             String
Library             OperatingSystem
Library             StringFormat
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=True
Resource            util/Error.resource
Resource            util/XPath.resource


*** Variables ***
${SCREENSHOT_FOLDER}    screenshots


*** Test Cases ***
Take No Screenshot If Module Is Disabled
    ${FILENAME}    Get Expected Filename    ${TEST_NAME}
    Remove File    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
    Take Screenshots On Failure    False
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshots On Failure    True

Take Screenshot If XPath Not Found Multiple Times Default Folder
    FOR    ${_}    IN RANGE    1    3
        ${FILENAME}    Get Expected Filename    ${TEST_NAME}
        ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
        Wait Until Created    ${OUTPUT DIR}/${FILENAME}    1s
    END

Take Screenshot If XPath Not Found Multiple Times By Specific Folder
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    FOR    ${_}    IN RANGE    1    3
        ${FILENAME}    Get Expected Filename    ${TEST_NAME}
        ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
        Wait Until Created    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}    1s
    END
    Set Screenshot Directory

Take Manual Screenshot By Keyword
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    ${TEST_NAME}
    Remove File    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshots On Failure    False
    ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshot
    File Should Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory
    Take Screenshots On Failure    True

Test Case 1234: Something to Test
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    Test Case 1234 Something to Test
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshot
    File Should Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory

No Screenshots Should Created For No Library Keywords
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    No Screenshots Should Created For No Library Keywords
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Run Keyword And Ignore Error    Fail    You Should Not Pass
    Run Keyword And Ignore Error    Wait Until Keyword Succeeds    5x    10ms    Fail    You Should Not Pass
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory


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
    ${FILENAME}    Catenate    SEPARATOR=_    ${FILENAME}    [0-9]*
    ${FILENAME}    Catenate    SEPARATOR=.    ${FILENAME}    jpg

    RETURN    ${FILENAME}
