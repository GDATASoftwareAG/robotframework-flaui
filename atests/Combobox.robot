*** Settings ***
Documentation   Test cases for combobox keywords.

Library         FlaUILibrary
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${XPATH_COMBO_BOX}          ${MAIN_WINDOW_SIMPLE_CONTROLS}/ComboBox[@AutomationId='NonEditableCombo']
${COMBO_BOX_ITEM}           Item 3
${COMBO_BOX_NO_ITEM}        No Such Item
${COMBO_BOX_COUNT}          4
${COMBO_BOX_ITEM_SELECT}    2

*** Test Cases ***
Combobox Should Contain
    Combobox Should Contain  ${XPATH_COMBO_BOX}  ${COMBO_BOX_ITEM}

Combobox Should Contain Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Combobox Should Contain  ${XPATH_NOT_EXISTS}  ${COMBO_BOX_ITEM}  ${CUSTOM_ERR_MSG}

Combobox Should Contain Wrong XPath
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error  ${EXP_ERR_MSG}  Combobox Should Contain  ${XPATH_NOT_EXISTS}  ${COMBO_BOX_ITEM}

Combobox Should Contain Wrong Item
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_CONTROL_DOES_NOT_CONTAIN_ITEM}  ${COMBO_BOX_NO_ITEM}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Combobox Should Contain  ${XPATH_COMBO_BOX}  ${COMBO_BOX_NO_ITEM}

Get Combobox Items Count
    ${COUNT}  Get Combobox Items Count  ${XPATH_COMBO_BOX}
    Should Be Equal As Integers  ${COUNT}  ${COMBO_BOX_COUNT}

Get Combobox Items Count Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Get Combobox Items Count  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}

Select Combobox Item By Index
    Select Combobox Item By Index  ${XPATH_COMBO_BOX}  ${COMBO_BOX_ITEM_SELECT}
    ${DATA}  Get Selected Items From Combobox  ${XPATH_COMBO_BOX}
    Should Contain  ${DATA}  Item 3

Select Combobox Item By Index Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Select Combobox Item By Index  -2000  ${XPATH_COMBO_BOX}  ${CUSTOM_ERR_MSG}

Select Combobox Item Wrong Index Number
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_ARRAY_OUT_OF_BOUND}  -2000  ${XPATH_COMBO_BOX}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Combobox Item By Index  ${XPATH_COMBO_BOX}  -2000

Select Combobox Item Wrong Index Usage
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}  NOT_AN_ARRAY  ${XPATH_COMBO_BOX}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Select Combobox Item By Index  ${XPATH_COMBO_BOX}  NOT_AN_ARRAY

Get Selected Items From Combobox If Nothing Is Selected
    ${DATA}  Get Selected Items From Combobox  ${XPATH_COMBO_BOX}
    Should Be Empty  ${DATA}

Get Selected Items From Combobox Wrong XPath
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error   ${EXP_ERR_MSG}  Get Selected Items From Combobox  ${XPATH_NOT_EXISTS}

Get Selected Items From Combobox Custom Error Message
    Run Keyword And Expect Error  ${EXP_CUSTOM_ERR_MSG}  Get Selected Items From Combobox  ${XPATH_NOT_EXISTS}  ${CUSTOM_ERR_MSG}
