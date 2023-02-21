*** Settings ***
Documentation   Test suite for property keywords.
...

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         StringFormat
Library         Collections

Resource        util/Error.robot
Resource        util/Common.robot
Resource        util/XPath.robot

Suite Setup      Init Main Application
Suite Teardown   Stop Application  ${MAIN_PID}

*** Variables ***
${WINDOW_ELEMET}           ${MAIN_WINDOW}
${TEXT_ELEMENT}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/Edit[@AutomationId='TextBox']

*** Test Cases ***

Get Background Color
    ${expected_color}  Evaluate  (0, 0, 0, 0)
    ${color}      Get Background Color  ${TEXT_ELEMENT}
    Should Be Equal    ${color}  ${expected_color}

Get Foreground Color
    ${expected_color}  Evaluate  (0, 128, 0, 0)
    ${color}      Get Foreground Color  ${TEXT_ELEMENT}
    Should Be Equal    ${color}  ${expected_color}

Get Font Size
    ${expected_font_size}  Convert To Number  9.0
    ${font_size}  Get Font Size  ${TEXT_ELEMENT}
    Should Be Equal    ${font_size}  ${expected_font_size}

Get Font Name
    ${expected_font_size}  Convert To String  Segoe UI
    ${font_name}  Get Font Name  ${TEXT_ELEMENT}
    Should Be Equal    ${font_name}  ${expected_font_size}

Get Font Weight
    ${expected_font_weight}  Convert To Number  400.0
    ${font_weight}  Get Font Weight  ${TEXT_ELEMENT}
    Should Be Equal    ${font_weight}  ${expected_font_weight}

Get Culture
    ${UIA}  Get Variable Value    ${UIA}

    IF  '${UIA}' == 'UIA2'
        ${ERR_MSG}      Run Keyword And Expect Error   *  Get Culture  ${TEXT_ELEMENT}
        Should Be Equal As Strings  ${EXP_PROPERTY_NOT_SUPPORTED}  ${ERR_MSG}
    ELSE
        ${expected_culture}  Convert To String  en-US
        ${culture}  Get Culture  ${TEXT_ELEMENT}
        Should Be Equal    ${culture}  ${expected_culture}
    END

Is Hidden
    ${is_hidden}  Is Hidden  ${TEXT_ELEMENT}
    Should Be Equal    ${is_hidden}  ${False}

Is Visible
    ${is_visible}  Is Visible  ${TEXT_ELEMENT}
    Should Be Equal    ${is_visible}  ${True}

Get Window Visual State
    ${state}  Get Window Visual State  ${WINDOW_ELEMET}
    Should Be Equal    ${state}  Normal
