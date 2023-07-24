*** Settings ***
Documentation   Test suite for screenshot keywords.
...             XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...             Keyword                               Test Case Names
...             Take Screenshot                       Take Screenshot If XPath Not Found Multiple Times Default Folder
...                                                   Take Manual Screenshot By Keyword
...             Take Screenshots On Failure           Take No Screenshot If Module Is Disabled
...             Set Screenshot Directory              Take Screenshot If XPath Not Found Multiple Times By Specific Folder
...                                                   Take Manual Screenshot By Keyword
...

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=True
Library         StringFormat
Library         Process
Library         String
Library         OperatingSystem

Resource        util/Error.robot
Resource        util/XPath.robot

*** Variables ***
${SCREENSHOT_FOLDER}  screenshots

*** Test Cases ***
Take No Screenshot If Module Is Disabled
    ${FILENAME}  Get Expected Filename  ${TEST_NAME}

    Remove File  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}

    ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}

    Take Screenshots On Failure  False
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
    File Should Not Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshots On Failure  True

Take Screenshot If XPath Not Found Multiple Times Default Folder
    FOR    ${INDEX}    IN RANGE    1    3
        ${FILENAME}  Get Expected Filename  ${TEST_NAME}
        ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
        Wait Until Created  ${OUTPUT DIR}/${FILENAME}  1s
    END

Take Screenshot If XPath Not Found Multiple Times By Specific Folder
    Set Screenshot Directory  screenshots
    FOR    ${INDEX}    IN RANGE    1    3
        ${FILENAME}  Get Expected Filename  ${TEST_NAME}
        ${EXP_ERR_MSG}  StringFormat.Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
        Run Keyword And Expect Error  ${EXP_ERR_MSG}  Click  ${XPATH_NOT_EXISTS}
        Wait Until Created  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}  1s
    END
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
    Take Screenshots On Failure  True

Test Case 1234: Something to Test
    Set Screenshot Directory  screenshots

    ${FILENAME}  Get Expected Filename  Test Case 1234 Something to Test

    File Should Not Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Take Screenshot
    File Should Exist  ${OUTPUT DIR}/${SCREENSHOT_FOLDER}/${FILENAME}
    Set Screenshot Directory

*** Keywords ***
Get Expected Filename
    [Arguments]  ${TEST_NAME}
    ${FILENAME}  Convert To Lowercase  ${TEST_NAME}
    ${HOSTNAME}  Convert To Lowercase  %{COMPUTERNAME}

    Should Be Lowercase  ${FILENAME}

    ${FILENAME}  Replace String  ${FILENAME}  ${space}  _
    ${FILENAME}  Catenate  SEPARATOR=_  ${HOSTNAME}   ${FILENAME}
    ${FILENAME}  Catenate  SEPARATOR=_  test   ${FILENAME}
    ${FILENAME}  Catenate  SEPARATOR=_  ${FILENAME}  [0-9]*
    ${FILENAME}  Catenate  SEPARATOR=_  ${FILENAME}  [0-9]*
    ${FILENAME}  Catenate  SEPARATOR=.  ${FILENAME}   jpg

    [Return]  ${FILENAME}
