*** Variables ***
${EXP_WINDOW_TITLE}                                FlaUI WPF Test App
${WRONG_PID}                                       99989
${TEST_APP}                                        apps\\WpfApplication
${TEST_APP_NOTIFIER}                               apps\\Notifier

*** Keywords ***
Stop Application
    Close Application

Start Application
    [Arguments]   ${application}=${TEST_APP}  ${xpath}=${MAIN_WINDOW}
    ${PID}  Launch Application  ${application}
    Should Not Be Equal As Integers  ${PID}  0
    Wait Until Keyword Succeeds  10x  200ms  Element Should Exist  ${xpath}
    Focus  ${xpath}
