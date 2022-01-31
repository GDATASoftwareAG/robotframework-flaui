*** Variables ***
${EXP_WINDOW_TITLE}                                FlaUI WPF Test App
${WRONG_PID}                                       99989
${TEST_APP}                                        apps\\WpfApplication
${TEST_APP_NOTIFIER}                               apps\\Notifier

*** Keywords ***
Init Main Application
  ${PID}  Start Application
  Set Global Variable  ${MAIN_PID}  ${PID}

Stop Application
    [Arguments]  ${pid}=${INTERNAL_PID}  ${xpath}=${MAIN_WINDOW}
    Close Application  ${pid}
    Wait Until Element Is Hidden  ${xpath}

Start Application
    [Arguments]   ${application}=${TEST_APP}  ${xpath}=${MAIN_WINDOW}
    ${PID}  Launch Application  ${application}
    Should Not Be Equal As Integers  ${PID}  0
    Wait Until Element Is Visible  ${xpath}
    Focus  ${xpath}
    [Return]  ${PID}

Start Application With Args
    [Arguments]   ${application}=${TEST_APP}  ${xpath}=${MAIN_WINDOW}  ${arguments}=${EXP_WINDOW_TITLE}
    ${PID}  Launch Application With Args  ${application}  ${arguments}
    Should Not Be Equal As Integers  ${PID}  0
    Wait Until Element Is Visible  ${xpath}
    Focus  ${xpath}
    [Return]  ${PID}

Open Complex Tab
    ${XPATH_TAB}                Set Variable  ${MAIN_WINDOW}/Tab
    ${TAB_ITEM_LIST_CONTROLS}   Set Variable  Complex Controls
    Select Tab Item By Name     ${XPATH_TAB}  ${TAB_ITEM_LIST_CONTROLS}
