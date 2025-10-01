*** Settings ***
Documentation       Test suite for screenshot keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Process
Library             String
Library             OperatingSystem
Library             StringFormat
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=True    screenshot_suffix=png
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource


*** Variables ***
${SCREENSHOT_FOLDER}    screenshots/default


*** Test Cases ***
Take Screenshot Of Window As Png From Library Import
    [Setup]    Start Application
    ${PID}    Attach Application By Name    ${TEST_APP}
    Set Screenshot Directory    ${SCREENSHOT_FOLDER}
    ${FILENAME}    Get Expected Filename    ${TEST_NAME}    png
    File Should Not Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshot    ${MAIN_WINDOW}
    File Should Exist    ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    [Teardown]    Run Keyword And Ignore Error    Stop Application    ${PID}


*** Keywords ***
Get Expected Filename
    [Arguments]    ${TEST_FILENAME}    ${SUFFIX}=jpg
    ${FILENAME}    Convert To Lowercase    ${TEST_FILENAME}
    ${HOSTNAME}    Convert To Lowercase    %{COMPUTERNAME}

    Should Be Lowercase    ${FILENAME}

    ${FILENAME}    Replace String    ${FILENAME}    ${space}    _
    ${FILENAME}    Catenate    SEPARATOR=_    ${HOSTNAME}    ${FILENAME}
    ${FILENAME}    Catenate    SEPARATOR=_    test    ${FILENAME}
    ${FILENAME}    Catenate    SEPARATOR=_    ${FILENAME}    [0-9]*
    ${FILENAME}    Catenate    SEPARATOR=.    ${FILENAME}    ${SUFFIX}

    RETURN    ${FILENAME}
