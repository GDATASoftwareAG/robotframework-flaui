*** Settings ***
Documentation       Test suite for tab keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Collections
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Library             StringFormat
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource

Suite Setup         Init Main Application
Suite Teardown      Stop Application    ${MAIN_PID}


*** Variables ***
${XPATH_TAB}                                        ${MAIN_WINDOW}/Tab
${TAB_ITEM_LIST_CONTROLS}                           Complex Controls
${TAB_ITEM_LIST_CONTROLS_WITH_NO_BREAK_SPACE}       Complex\xa0Controls
${TAB_ITEM_NOT_PRESENT}                             Not Present


*** Test Cases ***
Tab Should Contain List Controls TabItem
    @{CHILD_TAB_ITEMS}    Get Tab Items Names    ${XPATH_TAB}
    List Should Contain Value    ${CHILD_TAB_ITEMS}    ${TAB_ITEM_LIST_CONTROLS}

Tab Should Not Contain List Controls With No Break Space TabItem
    @{CHILD_TAB_ITEMS}    Get Tab Items Names    ${XPATH_TAB}
    List Should Not Contain Value    ${CHILD_TAB_ITEMS}    ${TAB_ITEM_LIST_CONTROLS_WITH_NO_BREAK_SPACE}

Tab Should Not Contain Not Present TabItem
    @{CHILD_TAB_ITEMS}    Get Tab Items Names    ${XPATH_TAB}
    List Should Not Contain Value    ${CHILD_TAB_ITEMS}    ${TAB_ITEM_NOT_PRESENT}

Select Tab Item By Name
    Select Tab Item By Name    ${XPATH_TAB}    ${TAB_ITEM_LIST_CONTROLS}
    Element Should Exist    ${MAIN_WINDOW_COMPLEX_CONTROLS}

Select Tab Item By Name Not Exist
    ${EXP_ERR_MSG}    Format String    ${EXP_GENERIC_ERR_MSG}    No TabItem found with text 'Tab Not Exist'
    ${ERR_MSG}    Run Keyword And Expect Error    *    Select Tab Item By Name    ${XPATH_TAB}    Tab Not Exist
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}
