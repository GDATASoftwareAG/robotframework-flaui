*** Settings ***
Documentation   Test suite for window keywords.

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

*** Test Cases ***
Close Window
    Start Application
    Close Window    ${MAIN_WINDOW}
    Wait Until Element Is Hidden  ${MAIN_WINDOW}
