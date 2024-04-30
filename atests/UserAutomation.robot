*** Settings ***
Documentation       Test suite for user automation keywords.
...

Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Library             StringFormat
Resource            util/Error.resource


*** Test Cases ***
Switch Uia To
    ${IDENTIFIER}    Get Uia Identifier
    Should Be Equal    ${IDENTIFIER}    ${UIA}

    Switch UIA To    UIA2
    ${IDENTIFIER}    Get Uia Identifier
    Should Be Equal    ${IDENTIFIER}    UIA2

    Switch UIA To    UIA3
    ${IDENTIFIER}    Get Uia Identifier
    Should Be Equal    ${IDENTIFIER}    UIA3

Switch Uia To Should Raise Exception If Interface Not Supported
    Run Keyword And Expect Error    ${EXP_ACTION_NOT_SUPPORTED}    Run Keyword    Switch UIA To    UIA4
