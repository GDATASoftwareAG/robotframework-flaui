*** Settings ***
Documentation       Test suite for property keywords.
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
${WINDOW_ELEMENT}               ${MAIN_WINDOW}
${TEXT_ELEMENT}                 ${MAIN_WINDOW_SIMPLE_CONTROLS}/Edit[@AutomationId='TextBox']
${TOGGLE_ELEMENT}               ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ToggleButton']
${XPATH_COMBO_BOX}              ${MAIN_WINDOW_SIMPLE_CONTROLS}/ComboBox[@AutomationId='NonEditableCombo']
${EDITABLE_COMBOX}              ${MAIN_WINDOW_SIMPLE_CONTROLS}/ComboBox[@AutomationId='EditableCombo']
${EDITABLE_COMBOX_EDIT}         ${EDITABLE_COMBOX}/Edit
${XPATH_TREE}                   ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group/Tree[@AutomationId='treeView1']
${XPATH_TAB}                    ${MAIN_WINDOW}/Tab
${XPATH_RADIO_BUTTON_ONE}       ${MAIN_WINDOW_SIMPLE_CONTROLS}/RadioButton[@AutomationId='RadioButton1']
${XPATH_RADIO_BUTTON_TWO}       ${MAIN_WINDOW_SIMPLE_CONTROLS}/RadioButton[@AutomationId='RadioButton2']
${XPATH_PROGRESSBAR}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/ProgressBar[@AutomationId='ProgressBar']
${XPATH_GRID_VIEW}              ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group[@Name='Grid']/DataGrid[@AutomationId='dataGridView']


*** Test Cases ***
Get Background Color
    ${expected_color}    Evaluate    (0, 0, 0, 0)
    ${color}    Get Background Color    ${TEXT_ELEMENT}
    Should Be Equal    ${color}    ${expected_color}

Get Background Color From Element
    ${expected_color}    Evaluate    (0, 0, 0, 0)
    ${color}    Get Property From Element    ${TEXT_ELEMENT}    BACKGROUND_COLOR
    Should Be Equal    ${color}    ${expected_color}

Background Color Should Be
    ${expected_color}    Evaluate    (0, 0, 0, 0)
    Background Color Should Be    ${TEXT_ELEMENT}    ${expected_color}

Wrong Background Color Should Raise An Exception
    ${expected_color}    Evaluate    (0, 0, 0, 0)
    ${wrong_color}    Evaluate    (0, 128, 0, 0)
    ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    ${expected_color}    ${wrong_color}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Background Color Should Be    ${TEXT_ELEMENT}    ${wrong_color}

Get Foreground Color
    ${expected_color}    Evaluate    (0, 128, 0, 0)
    ${color}    Get Foreground Color    ${TEXT_ELEMENT}
    Should Be Equal    ${color}    ${expected_color}

Get Foreground Color From Element
    ${expected_color}    Evaluate    (0, 128, 0, 0)
    ${color}    Get Property From Element    ${TEXT_ELEMENT}    FOREGROUND_COLOR
    Should Be Equal    ${color}    ${expected_color}

Foreground Color Should Be
    ${expected_color}    Evaluate    (0, 128, 0, 0)
    Foreground Color Should Be    ${TEXT_ELEMENT}    ${expected_color}

Wrong Foreground Color Should Raise An Exception
    ${expected_color}    Evaluate    (0, 128, 0, 0)
    ${wrong_color}    Evaluate    (0, 0, 0, 0)
    ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    ${expected_color}    ${wrong_color}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Foreground Color Should Be    ${TEXT_ELEMENT}    ${wrong_color}

Get Font Size
    ${expected_font_size}    Convert To Number    9.0
    ${font_size}    Get Font Size    ${TEXT_ELEMENT}
    Should Be Equal    ${font_size}    ${expected_font_size}

Get Font Size From Element
    ${expected_font_size}    Convert To Number    9.0
    ${font_size}    Get Property From Element    ${TEXT_ELEMENT}    FONT_SIZE
    Should Be Equal    ${font_size}    ${expected_font_size}

Font Size Should Be
    ${expected_font_size}    Convert To Number    9.0
    Font Size Should Be    ${TEXT_ELEMENT}    ${expected_font_size}

Wrong Font Size Should Raise An Exception
    ${expected_font_size}    Convert To Number    9.0
    ${wrong_font_size}    Convert To Number    8.9
    ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    ${expected_font_size}    ${wrong_font_size}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Font Size Should Be    ${TEXT_ELEMENT}    ${wrong_font_size}

Get Font Name
    ${expected_font_name}    Convert To String    Segoe UI
    ${font_name}    Get Font Name    ${TEXT_ELEMENT}
    Should Be Equal    ${font_name}    ${expected_font_name}

Get Font Name From Element
    ${expected_font_name}    Convert To String    Segoe UI
    ${font_name}    Get Property From Element    ${TEXT_ELEMENT}    FONT_NAME
    Should Be Equal    ${font_name}    ${expected_font_name}

Font Name Should Be
    ${expected_font_name}    Convert To String    Segoe UI
    Font Name Should Be    ${TEXT_ELEMENT}    ${expected_font_name}

Wrong Font Name Should Raise An Exception
    ${expected_font_name}    Convert To String    Segoe UI
    ${wrong_font_name}    Convert To String    Arial
    ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    ${expected_font_name}    ${wrong_font_name}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Font Name Should Be    ${TEXT_ELEMENT}    ${wrong_font_name}

Get Font Weight
    ${expected_font_weight}    Convert To Number    400.0
    ${font_weight}    Get Font Weight    ${TEXT_ELEMENT}
    Should Be Equal    ${font_weight}    ${expected_font_weight}

Get Font Weight From Element
    ${expected_font_weight}    Convert To Number    400.0
    ${font_weight}    Get Property From Element    ${TEXT_ELEMENT}    FONT_WEIGHT
    Should Be Equal    ${font_weight}    ${expected_font_weight}

Font Weight Should Be
    ${expected_font_weight}    Convert To Number    400.0
    Font Weight Should Be    ${TEXT_ELEMENT}    ${expected_font_weight}

Wrong Font Weight Should Raise An Exception
    ${expected_font_weight}    Convert To Number    400.0
    ${wrong_font_weight}    Convert To Number    399
    ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    ${expected_font_weight}    ${wrong_font_weight}
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Font Weight Should Be    ${TEXT_ELEMENT}    ${wrong_font_weight}

Get Culture
    ${UIA}    Get Variable Value    ${UIA}

    IF    '${UIA}' == 'UIA2'
        ${ERR_MSG}    Run Keyword And Expect Error    *    Get Culture    ${TEXT_ELEMENT}
        Should Be Equal As Strings    ${EXP_PROPERTY_NOT_SUPPORTED}    ${ERR_MSG}
    ELSE
        ${expected_culture}    Convert To String    en-US
        ${culture}    Get Culture    ${TEXT_ELEMENT}
        Should Be Equal    ${culture}    ${expected_culture}
    END

Get Culture From Element
    ${UIA}    Get Variable Value    ${UIA}

    IF    '${UIA}' == 'UIA2'
        ${ERR_MSG}    Run Keyword And Expect Error    *    Get Property From Element    ${TEXT_ELEMENT}    CULTURE
        Should Be Equal As Strings    ${EXP_PROPERTY_NOT_SUPPORTED}    ${ERR_MSG}
    ELSE
        ${expected_culture}    Convert To String    en-US
        ${culture}    Get Property From Element    ${TEXT_ELEMENT}    CULTURE
        Should Be Equal    ${culture}    ${expected_culture}
    END

Culture Should Be
    ${UIA}    Get Variable Value    ${UIA}

    IF    '${UIA}' == 'UIA2'
        ${ERR_MSG}    Run Keyword And Expect Error    *    Get Culture    ${TEXT_ELEMENT}
        Should Be Equal As Strings    ${EXP_PROPERTY_NOT_SUPPORTED}    ${ERR_MSG}
    ELSE
        ${expected_culture}    Convert To String    en-US
        Culture Should Be    ${TEXT_ELEMENT}    ${expected_culture}
    END

Wrong Culture Should Raise An Exception
    ${UIA}    Get Variable Value    ${UIA}

    IF    '${UIA}' == 'UIA2'
        ${ERR_MSG}    Run Keyword And Expect Error    *    Get Culture    ${TEXT_ELEMENT}
        Should Be Equal As Strings    ${EXP_PROPERTY_NOT_SUPPORTED}    ${ERR_MSG}
    ELSE
        ${wrong_culture}    Convert To String    de-DE
        ${expected_culture}    Convert To String    en-US
        ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    ${expected_culture}    ${wrong_culture}
        Run Keyword And Expect Error    ${EXP_ERR_MSG}    Culture Should Be    ${TEXT_ELEMENT}    ${wrong_culture}
    END

Is Hidden
    ${is_hidden}    Is Hidden    ${TEXT_ELEMENT}
    Should Be Equal    ${is_hidden}    ${False}

Is Visible
    ${is_visible}    Is Visible    ${TEXT_ELEMENT}
    Should Be Equal    ${is_visible}    ${True}

Get Window Visual State
    ${state}    Get Window Visual State    ${WINDOW_ELEMENT}
    Should Be Equal    ${state}    Normal

Get Window Visual State From Element
    ${state}    Get Property From Element    ${WINDOW_ELEMENT}    WINDOW_VISUAL_STATE
    Should Be Equal    ${state}    Normal

Window Visual State Should Be
    Window Visual State Should Be    ${WINDOW_ELEMENT}    Normal

Wrong Window Visual State Should Raise An Exception
    ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    Normal    Maximized
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Window Visual State Should Be    ${WINDOW_ELEMENT}    Maximized

Get Window Interaction State
    Focus    ${WINDOW_ELEMENT}
    ${state}    Get Window Interaction State    ${WINDOW_ELEMENT}
    Should Be Equal    ${state}    ReadyForUserInteraction

Get Window Interaction State From Element
    ${state}    Get Property From Element    ${WINDOW_ELEMENT}    WINDOW_INTERACTION_STATE
    Should Be Equal    ${state}    ReadyForUserInteraction

Window Interaction State Should Be
    Focus    ${WINDOW_ELEMENT}
    Window Interaction State Should Be    ${WINDOW_ELEMENT}    ReadyForUserInteraction

Wrong Window Interaction State Should Raise An Exception
    Focus    ${WINDOW_ELEMENT}
    ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    ReadyForUserInteraction    NotResponding
    Run Keyword And Expect Error
    ...    ${EXP_ERR_MSG}
    ...    Window Interaction State Should Be
    ...    ${WINDOW_ELEMENT}
    ...    NotResponding

Get Toggle State
    ${state}    Get Toggle State    ${TOGGLE_ELEMENT}
    Should Be Equal    ${state}    OFF

Get Toggle State From Element
    ${state}    Get Property From Element    ${TOGGLE_ELEMENT}    TOGGLE_STATE
    Should Be Equal    ${state}    OFF

Toggle State Should Be
    Toggle State Should Be    ${TOGGLE_ELEMENT}    OFF

Wrong Toggle State Should Raise An Exception
    ${EXP_ERR_MSG}    Format String    ${EXP_PROPERTY_INEQUAL}    OFF    ON
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Toggle State Should Be    ${TOGGLE_ELEMENT}    ON

Set Visual State To
    Window Visual State Should Be    ${WINDOW_ELEMENT}    Normal
    Maximize Window    ${WINDOW_ELEMENT}
    Window Visual State Should Be    ${WINDOW_ELEMENT}    Maximized
    Minimize Window    ${WINDOW_ELEMENT}
    Window Visual State Should Be    ${WINDOW_ELEMENT}    Minimized
    Normalize Window    ${WINDOW_ELEMENT}
    Window Visual State Should Be    ${WINDOW_ELEMENT}    Normal

Can Window Be Maximized
    ${result}    Can Window Be Maximized    ${WINDOW_ELEMENT}
    Should Be True    ${result}

Can Window Be Maximized From Element
    ${result}    Get Property From Element    ${WINDOW_ELEMENT}    CAN_WINDOW_MAXIMIZE
    Should Be True    ${result}

Can Window Be Minimized
    ${result}    Can Window Be Minimized    ${WINDOW_ELEMENT}
    Should Be True    ${result}

Can Window Be Minimized From Element
    ${result}    Get Property From Element    ${WINDOW_ELEMENT}    CAN_WINDOW_MINIMIZE
    Should Be True    ${result}

Is Read Only
    ${result}    Get Property From Element    ${TEXT_ELEMENT}    IS_READ_ONLY
    Should Be Equal    ${result}    ${False}

Is Window Pattern Supported From Element
    ${result}    Get Property From Element    ${WINDOW_ELEMENT}    IS_WINDOW_PATTERN_SUPPORTED
    Should Be True    ${result}
    ${result}    Get Property From Element    ${TOGGLE_ELEMENT}    IS_WINDOW_PATTERN_SUPPORTED
    Should Be Equal    ${result}    ${False}

Is Text Pattern Supported From Element
    ${result}    Get Property From Element    ${TEXT_ELEMENT}    IS_TEXT_PATTERN_SUPPORTED
    Should Be True    ${result}
    ${result}    Get Property From Element    ${WINDOW_ELEMENT}    IS_TEXT_PATTERN_SUPPORTED
    Should Be Equal    ${result}    ${False}

Is Toggle Pattern Supported From Element
    ${result}    Get Property From Element    ${TOGGLE_ELEMENT}    IS_TOGGLE_PATTERN_SUPPORTED
    Should Be True    ${result}
    ${result}    Get Property From Element    ${TEXT_ELEMENT}    IS_TOGGLE_PATTERN_SUPPORTED
    Should Be Equal    ${result}    ${False}

Is Value Pattern Supported From Element
    ${result}    Get Property From Element    ${TEXT_ELEMENT}    IS_VALUE_PATTERN_SUPPORTED
    Should Be True    ${result}
    ${result}    Get Property From Element    ${TOGGLE_ELEMENT}    IS_VALUE_PATTERN_SUPPORTED
    Should Be Equal    ${result}    ${False}

Value Pattern Value From Element
    Select Combobox Item By Index    ${EDITABLE_COMBOX}    0
    ${value}    Get Property From Element    ${EDITABLE_COMBOX_EDIT}    VALUE
    Should Be Equal As Strings    ${value}    Item 1

    Select Combobox Item By Index    ${EDITABLE_COMBOX}    1
    ${value}    Get Property From Element    ${EDITABLE_COMBOX_EDIT}    VALUE
    Should Be Equal As Strings    ${value}    Item 2

    Select Combobox Item By Index    ${EDITABLE_COMBOX}    2
    ${value}    Get Property From Element    ${EDITABLE_COMBOX_EDIT}    VALUE
    Should Be Equal As Strings    ${value}    Item 3

Is RangeValue Pattern Supported From Element
    ${result}    Get Property From Element    ${XPATH_PROGRESSBAR}    IS_RANGEVALUE_PATTERN_SUPPORTED
    Should Be True    ${result}
    ${result}    Get Property From Element    ${TEXT_ELEMENT}    IS_RANGEVALUE_PATTERN_SUPPORTED
    Should Be Equal    ${result}    ${False}

RangeValue Pattern Value From Element
    ${value}    Get Property From Element    ${XPATH_PROGRESSBAR}    RANGEVALUE
    Should Be Equal    ${value}    50

RangeValue Pattern Minimum From Element
    ${value}    Get Property From Element    ${XPATH_PROGRESSBAR}    RANGEMINIMUM
    Should Be Equal    ${value}    0

RangeValue Pattern Maximum From Element
    ${value}    Get Property From Element    ${XPATH_PROGRESSBAR}    RANGEMAXIMUM
    Should Be Equal    ${value}    100

Is Expand Collapse Pattern Supported
    ${result}    Get Property From Element    ${XPATH_COMBO_BOX}    IS_EXPAND_COLLAPSE_PATTERN_SUPPORTED
    Should Be True    ${result}
    ${result}    Get Property From Element    ${TOGGLE_ELEMENT}    IS_EXPAND_COLLAPSE_PATTERN_SUPPORTED
    Should Be Equal    ${result}    ${False}

Expand Collapse State From Element
    ${origin_state}    Get Property From Element    ${XPATH_COMBO_BOX}    EXPAND_COLLAPSE_STATE
    Should Be Equal As Strings    ${origin_state}    Collapsed

    Expand Combobox    ${XPATH_COMBO_BOX}
    ${first_state}    Get Property From Element    ${XPATH_COMBO_BOX}    EXPAND_COLLAPSE_STATE
    Should Be Equal As Strings    ${first_state}    Expanded

    Collapse Combobox    ${XPATH_COMBO_BOX}
    ${second_state}    Get Property From Element    ${XPATH_COMBO_BOX}    EXPAND_COLLAPSE_STATE
    Should Be Equal As Strings    ${second_state}    Collapsed

Is Selection Item Pattern Supported
    [Setup]    Open Complex Tab
    Wait Until Element Is Enabled    ${XPATH_TREE}
    ${state}    Get Property From Element    ${XPATH_TREE}    IS_SELECTION_ITEM_PATTERN_SUPPORTED
    Should Not Be True    ${state}

    Wait Until Element Is Enabled    ${XPATH_TREE}/TreeItem[1]
    ${state}    Get Property From Element    ${XPATH_TREE}/TreeItem[1]    IS_SELECTION_ITEM_PATTERN_SUPPORTED
    Should Be True    ${state}

Is Selected From TreeItem Element
    [Setup]    Open Complex Tab
    ${EXP_ERR_MSG}    Format String    ${EXP_PATTERN_NOT_SUPPORTED}    SelectionItem
    Wait Until Element Is Enabled    ${XPATH_TREE}
    ${ERR_MSG}    Run Keyword And Expect Error    *    Get Property From Element    ${XPATH_TREE}    IS_SELECTED
    Should Be Equal As Strings    ${EXP_ERR_MSG}    ${ERR_MSG}

    Wait Until Element Is Enabled    ${XPATH_TREE}/TreeItem[1]
    ${state}    Get Property From Element    ${XPATH_TREE}/TreeItem[1]    IS_SELECTED
    Should Not Be True    ${state}

    Click    ${XPATH_TREE}/TreeItem[1]/Text
    ${state}    Get Property From Element    ${XPATH_TREE}/TreeItem[1]    IS_SELECTED
    Should Be True    ${state}

Is Selected From TabItem Element
    [Setup]    Open Simple Tab
    Wait Until Element Is Enabled    ${XPATH_TAB}
    ${state}    Get Property From Element    ${XPATH_TAB}/TabItem[1]    IS_SELECTED
    Should Be True    ${state}
    ${state}    Get Property From Element    ${XPATH_TAB}/TabItem[2]    IS_SELECTED
    Should Not Be True    ${state}

Is Selected From RadioButton Element
    [Setup]    Open Simple Tab
    Wait Until Element Is Enabled    ${XPATH_RADIO_BUTTON_ONE}
    ${state}    Get Property From Element    ${XPATH_RADIO_BUTTON_ONE}    IS_SELECTED
    Should Not Be True    ${state}

    Click    ${XPATH_RADIO_BUTTON_ONE}
    ${state}    Get Property From Element    ${XPATH_RADIO_BUTTON_ONE}    IS_SELECTED
    Should Be True    ${state}
    ${state}    Get Property From Element    ${XPATH_RADIO_BUTTON_TWO}    IS_SELECTED
    Should Not Be True    ${state}

Is Selected From DataGrid DataItem Element
    [Setup]    Open Complex Tab
    Wait Until Element Is Enabled    ${XPATH_GRID_VIEW}
    ${state}    Get Property From Element    ${XPATH_GRID_VIEW}/DataItem[1]    IS_SELECTED
    Should Not Be True    ${state}

    Click    ${XPATH_GRID_VIEW}/DataItem[1]/Custom
    ${state}    Get Property From Element    ${XPATH_GRID_VIEW}/DataItem[1]    IS_SELECTED
    Should Be True    ${state}

Is Selected From Combobox ListItem Element
    [Setup]    Open Simple Tab
    Wait Until Element Is Enabled    ${EDITABLE_COMBOX}
    Select Combobox Item By Index    ${EDITABLE_COMBOX}    0
    ${state}    Get Property From Element    ${EDITABLE_COMBOX}/ListItem[1]    IS_SELECTED
    Should Be True    ${state}
    ${state}    Get Property From Element    ${EDITABLE_COMBOX}/ListItem[2]    IS_SELECTED
    Should Not Be True    ${state}
