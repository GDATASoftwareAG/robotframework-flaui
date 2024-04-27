*** Settings ***
Documentation       Test suite for screenshot keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=True
Library             StringFormat
Library             Process
Library             String
Library             OperatingSystem
Resource            util/Error.robot
Resource            util/XPath.robot


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
    FOR    ${INDEX}    IN RANGE    1    3
        ${FILENAME}    Get Expected Filename    ${TEST_NAME}
        ${EXP_ERR_MSG}    StringFormat.Format String    ${EXP_ERR_MSG_XPATH_NOT_FOUND}    ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error    ${EXP_ERR_MSG}    Click    ${XPATH_NOT_EXISTS}
        Wait Until Created    ${OUTPUT DIR}/${FILENAME}    1s
    END

Take Screenshot If XPath Not Found Multiple Times By Specific Folder
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    FOR    ${INDEX}    IN RANGE    1    3
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

No Screenshots Are Created After Blacklist
    [Setup]    Reset
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    No Screenshots Are Created After Blacklist
    @{blacklist}    Create List
    ...    BuiltIn.Wait Until Keyword Succeeds
    ...    BuiltIn.Run Keyword And Ignore Error
    ...    BuiltIn.Fail
    Set Screenshot Blacklist    ${blacklist}
    Run Keyword And Ignore Error    Wait Until Keyword Succeeds    5x    10ms    Fail    You Should Not Pass
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory
    [Teardown]    Reset

Screenshots Are Persisted From Whitelist
    [Setup]    Reset
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    Screenshots Are Persisted From Whitelist
    @{whitelist}    Create List    BuiltIn.Run Keyword And Ignore Error    BuiltIn.Fail
    Set Screenshot Whitelist    ${whitelist}
    Run Keyword And Ignore Error    Fail    You Should Not Pass
    File Should Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory
    [Teardown]    Reset

Blacklist Is Prioritize From Whitelist
    [Setup]    Reset
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    Blacklist Is Prioritize From Whitelist
    @{list}    Create List
    ...    BuiltIn.Wait Until Keyword Succeeds
    ...    BuiltIn.Run Keyword And Ignore Error
    ...    BuiltIn.Fail
    Set Screenshot Whitelist    ${list}
    Set Screenshot Blacklist    ${list}
    Run Keyword And Ignore Error    Wait Until Keyword Succeeds    5x    10ms    Fail    You Should Not Pass
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory
    [Teardown]    Reset


*** Keywords ***
Reset
    Take Screenshots On Failure    True
    Clear Blacklist
    Clear Whitelist

Get Expected Filename
    [Arguments]    ${TEST_NAME}
    ${FILENAME}    Convert To Lowercase    ${TEST_NAME}
    ${HOSTNAME}    Convert To Lowercase    %{COMPUTERNAME}

    Should Be Lowercase    ${FILENAME}

    ${FILENAME}    Replace String    ${FILENAME}    ${space}    _
    ${FILENAME}    Catenate    SEPARATOR=_    ${HOSTNAME}    ${FILENAME}
    ${FILENAME}    Catenate    SEPARATOR=_    test    ${FILENAME}
    ${FILENAME}    Catenate    SEPARATOR=_    ${FILENAME}    [0-9]*
    ${FILENAME}    Catenate    SEPARATOR=_    ${FILENAME}    [0-9]*
    ${FILENAME}    Catenate    SEPARATOR=.    ${FILENAME}    jpg

    RETURN    ${FILENAME}
