*** Variables ***
${EXP_WINDOW_TITLE}                                FlaUI WPF Test App
${WRONG_PID}                                       99989
${TEST_APP}                                        apps\\WpfApplication
${TEST_APP_NOTIFIER}                               apps\\Notifier

*** Keywords ***
Close Window Application
    [Arguments]   ${xpath}=${MAIN_WINDOW}
    Run Keyword and Ignore Error  Close Application
    Run Keyword and Ignore Error  Close Window  ${xpath}
    Wait Until Keyword Succeeds  5x  100ms  Element Should Not Exist  ${xpath}

Stop Application
    [Arguments]   ${xpath}=${MAIN_WINDOW}
    Wait Until Keyword Succeeds  5x  1s  Close Window Application  ${xpath}

Start Application
    [Arguments]   ${application}=${TEST_APP}  ${xpath}=${MAIN_WINDOW}
    ${PID}  Launch Application  ${application}
    Should Not Be Equal As Integers  ${PID}  0
    Wait Until Keyword Succeeds  10x  200ms  Element Should Exist  ${xpath}
    Focus  ${xpath}

Start Application With Args
    [Arguments]   ${application}=${TEST_APP}  ${xpath}=${MAIN_WINDOW}  ${arguments}=${EXP_WINDOW_TITLE}
    ${PID}  Launch Application With Args  ${application}  ${arguments}
    Should Not Be Equal As Integers  ${PID}  0
    Wait Until Keyword Succeeds  10x  200ms  Element Should Exist  ${xpath}
    Focus  ${xpath}

Open Complex Tab
    ${XPATH_TAB}                Set Variable  ${MAIN_WINDOW}/Tab
    ${TAB_ITEM_LIST_CONTROLS}   Set Variable  Complex Controls
    Select Tab Item By Name     ${XPATH_TAB}  ${TAB_ITEM_LIST_CONTROLS}
