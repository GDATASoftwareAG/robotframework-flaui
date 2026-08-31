*** Variables ***
${EXP_WINDOW_TITLE}     FlaUI WPF Test App
${WRONG_PID}            99989
${TEST_APP}             atests\\apps\\WpfApplication
${TEST_APP_NOTIFIER}    atests\\apps\\Notifier
${TEST_APP_MFC}         atests\\apps\\MFCApplication
${FAST_RETRY}           20x
${FAST_RETRY_INTERVAL}    100ms
${APP_RETRY}            10s
${APP_RETRY_INTERVAL}   200ms
${SHORT_RETRY}          3x
${SHORT_RETRY_INTERVAL}    50ms
${MISSING_APPLICATION}    ApplicationDoesNotExist


*** Keywords ***
Init Main Application
    ${PID}    Start Application
    VAR    ${MAIN_PID}    ${PID}    scope=GLOBAL

Stop Main Application If Running
    Run Keyword And Ignore Error    Close Application By Name    WpfApplication
    Run Keyword And Ignore Error
    ...    Wait Until Element Does Not Exist
    ...    ${MAIN_WINDOW}
    ...    ${APP_RETRY}
    ...    ${APP_RETRY_INTERVAL}

Restore Main Application
    Stop Main Application If Running
    ${PID}    Start Application
    VAR    ${MAIN_PID}    ${PID}    scope=GLOBAL

Stop Application
    [Arguments]    ${pid}=${INTERNAL_PID}    ${xpath}=${MAIN_WINDOW}
    Close Application    ${pid}
    Wait Until Element Does Not Exist    ${xpath}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}

Start Application
    [Arguments]    ${application}=${TEST_APP}    ${xpath}=${MAIN_WINDOW}
    ${PID}    Launch Application    ${application}
    Should Not Be Equal As Integers    ${PID}    0
    Wait Until Element Exist    ${xpath}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Focus    ${xpath}
    RETURN    ${PID}

Start Application With Args
    [Arguments]    ${application}=${TEST_APP}    ${xpath}=${MAIN_WINDOW}    ${arguments}=${EXP_WINDOW_TITLE}
    ${PID}    Launch Application With Args    ${application}    ${arguments}
    Should Not Be Equal As Integers    ${PID}    0
    Wait Until Element Exist    ${xpath}    ${APP_RETRY}    ${APP_RETRY_INTERVAL}
    Focus    ${xpath}
    RETURN    ${PID}

Assert Elapsed Seconds
    [Arguments]    ${elapsed}    ${minimum}    ${maximum}
    Should Be True    ${elapsed} >= ${minimum}    Elapsed ${elapsed}s is below ${minimum}s
    Should Be True    ${elapsed} < ${maximum}    Elapsed ${elapsed}s is not below ${maximum}s

Open Simple Tab
    ${XPATH_TAB}    Set Variable    ${MAIN_WINDOW}/Tab
    ${TAB_ITEM_LIST_CONTROLS}    Set Variable    Simple Controls
    Select Tab Item By Name    ${XPATH_TAB}    ${TAB_ITEM_LIST_CONTROLS}

Open Complex Tab
    ${XPATH_TAB}    Set Variable    ${MAIN_WINDOW}/Tab
    ${TAB_ITEM_LIST_CONTROLS}    Set Variable    Complex Controls
    Select Tab Item By Name    ${XPATH_TAB}    ${TAB_ITEM_LIST_CONTROLS}

Open Keyboard Tab
    ${XPATH_TAB}    Set Variable    ${MAIN_WINDOW}/Tab
    ${TAB_ITEM_LIST_CONTROLS}    Set Variable    Keyboard Controls
    Select Tab Item By Name    ${XPATH_TAB}    ${TAB_ITEM_LIST_CONTROLS}

Open Drag And Drop Tab
    ${XPATH_TAB}    Set Variable    ${MAIN_WINDOW}/Tab
    ${TAB_ITEM_DRAG_AND_DROP}    Set Variable    Drag And Drop
    Select Tab Item By Name    ${XPATH_TAB}    ${TAB_ITEM_DRAG_AND_DROP}

Open Data Grid Tab
    ${XPATH_TAB}    Set Variable    ${MAIN_WINDOW}/Tab
    ${TAB_ITEM_DATA_GRID}    Set Variable    Data Grid
    Select Tab Item By Name    ${XPATH_TAB}    ${TAB_ITEM_DATA_GRID}

Open Dynamic Properties Tab
    ${XPATH_TAB}    Set Variable    ${MAIN_WINDOW}/Tab
    ${TAB_ITEM_DYNAMIC_PROPERTIES}    Set Variable    Dynamic Properties
    Select Tab Item By Name    ${XPATH_TAB}    ${TAB_ITEM_DYNAMIC_PROPERTIES}

Ready To Take Off
    [Arguments]    ${xpath}
    Click    ${xpath}
    Name Should Be    Ready to take off    ${xpath}
