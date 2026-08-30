*** Settings ***
Documentation       Test suite for dynamically changed automation properties.
...                 Reproduces https://github.com/GDATASoftwareAG/robotframework-flaui/issues/79
...

Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Resource            util/Common.resource
Resource            util/XPath.resource

Suite Setup         Init Main Application
Suite Teardown      Stop Application    ${MAIN_PID}
Test Setup          Open Dynamic Properties Tab


*** Variables ***
${XPATH_CHANGE_ID_ORIGIN}       ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='ChangeAutomationIdOrigin']
${XPATH_CHANGE_ID_UPDATED}      ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='ChangeAutomationIdUpdate']
${XPATH_CHANGE_NAME}            ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='ChangeNameOrigin']
${XPATH_DELAYED_ID_ORIGIN}      ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='DelayedIdButton']
${XPATH_DELAYED_ID_RINGING}     ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='DelayedIdButtonRinging']
${XPATH_START_DELAYED}          ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='StartDelayedIdChange']
${XPATH_ADD_CHILD}              ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='AddDynamicChild']
${XPATH_DYNAMIC_CHILD}          ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='DynamicChildButton']
${XPATH_REPLACE_CHILD}          ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='ReplaceDynamicChild']
${XPATH_REPLACEABLE}            ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='ReplaceableChild']
${XPATH_REPLACED}               ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='ReplacedChild']
${XPATH_DYNAMIC_GROUP}          ${MAIN_WINDOW_DYNAMIC_PROPERTIES_CONTROLS}//*[@AutomationId='DynamicAutomationGroup']


*** Test Cases ***
Element Should Be Found After Automation Id Changed
    [Documentation]    After a click updates AutomationId, the new id must be found and the old id must disappear.
    Element Should Exist    ${XPATH_CHANGE_ID_ORIGIN}
    ${UPDATED_EXISTS}    Element Should Exist    ${XPATH_CHANGE_ID_UPDATED}    ${FALSE}
    Should Be Equal    ${UPDATED_EXISTS}    ${FALSE}
    Invoke Button    ${XPATH_CHANGE_ID_ORIGIN}
    ${AFTER}    Get Childs From Element    ${XPATH_DYNAMIC_GROUP}
    Log    ${AFTER}
    Should Contain    ${AFTER}    AutomationId:ChangeAutomationIdUpdate
    Should Not Contain    ${AFTER}    AutomationId:ChangeAutomationIdOrigin
    ${OLD_EXISTS}    Element Should Exist    ${XPATH_CHANGE_ID_ORIGIN}    ${FALSE}
    Should Be Equal    ${OLD_EXISTS}    ${FALSE}
    Element Should Exist    ${XPATH_CHANGE_ID_UPDATED}

Element Should Be Found After Name Changed
    [Documentation]    After a click updates Name, Get Childs From Element and Name Should Be must see the new value.
    Name Should Be    Original Name    ${XPATH_CHANGE_NAME}
    Invoke Button    ${XPATH_CHANGE_NAME}
    ${AFTER}    Get Childs From Element    ${XPATH_DYNAMIC_GROUP}
    Log    ${AFTER}
    Should Contain    ${AFTER}    Name:Changed Name
    Should Not Contain    ${AFTER}    Name:Original Name
    Name Should Be    Changed Name    ${XPATH_CHANGE_NAME}

Element Should Be Found After Delayed Automation Id Change
    [Documentation]    Telephony-style delayed AutomationId change must be visible to Wait Until Element Exist.
    Element Should Exist    ${XPATH_DELAYED_ID_ORIGIN}
    ${RINGING_EXISTS}    Element Should Exist    ${XPATH_DELAYED_ID_RINGING}    ${FALSE}
    Should Be Equal    ${RINGING_EXISTS}    ${FALSE}
    Invoke Button    ${XPATH_START_DELAYED}
    Wait Until Element Exist    ${XPATH_DELAYED_ID_RINGING}    5x    1s
    ${CHILDS}    Get Childs From Element    ${XPATH_DYNAMIC_GROUP}
    Log    ${CHILDS}
    Should Contain    ${CHILDS}    AutomationId:DelayedIdButtonRinging
    ${OLD_EXISTS}    Element Should Exist    ${XPATH_DELAYED_ID_ORIGIN}    ${FALSE}
    Should Be Equal    ${OLD_EXISTS}    ${FALSE}

Newly Added Child Should Be Found
    [Documentation]    Children added to an already inspected panel must be found without opening another window.
    ${BEFORE}    Get Childs From Element    ${XPATH_DYNAMIC_GROUP}
    Log    ${BEFORE}
    Should Not Contain    ${BEFORE}    AutomationId:DynamicChildButton
    ${CHILD_EXISTS}    Element Should Exist    ${XPATH_DYNAMIC_CHILD}    ${FALSE}
    Should Be Equal    ${CHILD_EXISTS}    ${FALSE}
    Invoke Button    ${XPATH_ADD_CHILD}
    ${AFTER}    Get Childs From Element    ${XPATH_DYNAMIC_GROUP}
    Log    ${AFTER}
    Should Contain    ${AFTER}    AutomationId:DynamicChildButton
    Element Should Exist    ${XPATH_DYNAMIC_CHILD}

Replaced Child Should Be Found By New Automation Id
    [Documentation]    Replacing a child in an existing panel must expose the new AutomationId.
    Element Should Exist    ${XPATH_REPLACEABLE}
    ${REPLACED_EXISTS}    Element Should Exist    ${XPATH_REPLACED}    ${FALSE}
    Should Be Equal    ${REPLACED_EXISTS}    ${FALSE}
    Invoke Button    ${XPATH_REPLACE_CHILD}
    ${AFTER}    Get Childs From Element    ${XPATH_DYNAMIC_GROUP}
    Log    ${AFTER}
    Should Contain    ${AFTER}    AutomationId:ReplacedChild
    Should Not Contain    ${AFTER}    AutomationId:ReplaceableChild
    Element Should Exist    ${XPATH_REPLACED}
    ${OLD_EXISTS}    Element Should Exist    ${XPATH_REPLACEABLE}    ${FALSE}
    Should Be Equal    ${OLD_EXISTS}    ${FALSE}
