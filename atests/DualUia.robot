*** Settings ***
Documentation       Test suite for using UIA2 and UIA3 together as named library instances.
...                 XPath trees must stay isolated after the other interface was used.
...

Library             FlaUILibrary    uia=UIA3    screenshot_on_failure=False    timeout=2000    AS    UIA3Lib
Library             FlaUILibrary    uia=UIA2    screenshot_on_failure=False    timeout=2000    AS    UIA2Lib
Resource            util/Common.resource
Resource            util/XPath.resource


*** Variables ***
${UIA3_TITLEBAR}        AutomationId:TitleBar, Name:,
${UIA2_TITLEBAR}        AutomationId:TitleBar, Name:FlaUI WPF Test App,
${TEXTBOX}              ${MAIN_WINDOW_SIMPLE_CONTROLS}/Edit[@AutomationId='TextBox']


*** Test Cases ***
Uia3 Tree Stays After Using Uia2
    [Documentation]    UIA3 XPaths must still resolve after a UIA2 lookup in the same run.
    ${PID}    UIA3Lib.Launch Application    ${TEST_APP}
    Should Not Be Equal As Integers    ${PID}    0
    UIA3Lib.Wait Until Element Exist    ${MAIN_WINDOW}
    UIA3Lib.Focus    ${MAIN_WINDOW}
    ${BEFORE}    UIA3Lib.Get Childs From Element    ${MAIN_WINDOW}
    Should Contain    ${BEFORE}    ${UIA3_TITLEBAR}
    Should Not Contain    ${BEFORE}    ${UIA2_TITLEBAR}
    ${EXISTS}    UIA2Lib.Element Should Exist    ${TEXTBOX}    ${FALSE}
    Should Be True    ${EXISTS}
    ${AFTER}    UIA3Lib.Get Childs From Element    ${MAIN_WINDOW}
    Should Contain    ${AFTER}    ${UIA3_TITLEBAR}
    Should Not Contain    ${AFTER}    ${UIA2_TITLEBAR}
    [Teardown]    Run Keyword And Ignore Error    UIA3Lib.Close Application    ${PID}

Uia3 Tree After Uia2 Was Used First
    [Documentation]    Using UIA2 first must not make UIA3 walk the UIA2 tree.
    ${PID}    UIA2Lib.Launch Application    ${TEST_APP}
    Should Not Be Equal As Integers    ${PID}    0
    UIA2Lib.Wait Until Element Exist    ${MAIN_WINDOW}
    UIA2Lib.Focus    ${MAIN_WINDOW}
    ${UIA2_CHILDS}    UIA2Lib.Get Childs From Element    ${MAIN_WINDOW}
    Should Contain    ${UIA2_CHILDS}    ${UIA2_TITLEBAR}
    ${EXISTS}    UIA3Lib.Element Should Exist    ${TEXTBOX}    ${FALSE}
    Should Be True    ${EXISTS}
    ${UIA3_CHILDS}    UIA3Lib.Get Childs From Element    ${MAIN_WINDOW}
    Should Contain    ${UIA3_CHILDS}    ${UIA3_TITLEBAR}
    Should Not Contain    ${UIA3_CHILDS}    ${UIA2_TITLEBAR}
    [Teardown]    Run Keyword And Ignore Error    UIA2Lib.Close Application    ${PID}
