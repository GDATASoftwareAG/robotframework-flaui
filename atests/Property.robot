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
${WINDOW_ELEMENT}          ${MAIN_WINDOW}
${TEXT_ELEMENT}            ${MAIN_WINDOW_SIMPLE_CONTROLS}/Edit[@AutomationId='TextBox']
${TOGGLE_ELEMENT}          ${MAIN_WINDOW_SIMPLE_CONTROLS}/Button[@AutomationId='ToggleButton']

*** Test Cases ***

Get Background Color
    ${expected_color}  Evaluate  (0, 0, 0, 0)
    ${color}      Get Background Color  ${TEXT_ELEMENT}
    Should Be Equal    ${color}  ${expected_color}

Background Color Should Be
    ${expected_color}  Evaluate  (0, 0, 0, 0)
    Background Color Should Be  ${TEXT_ELEMENT}  ${expected_color}

Wrong Background Color Should Raise An Exception
    ${expected_color}  Evaluate  (0, 0, 0, 0)
    ${wrong_color}  Evaluate  (0, 128, 0, 0)
    ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  ${expected_color}  ${wrong_color}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Background Color Should Be  ${TEXT_ELEMENT}  ${wrong_color}

Get Foreground Color
    ${expected_color}  Evaluate  (0, 128, 0, 0)
    ${color}      Get Foreground Color  ${TEXT_ELEMENT}
    Should Be Equal    ${color}  ${expected_color}

Foreground Color Should Be
    ${expected_color}  Evaluate  (0, 128, 0, 0)
    Foreground Color Should Be  ${TEXT_ELEMENT}  ${expected_color}

Wrong Foreground Color Should Raise An Exception
    ${expected_color}  Evaluate  (0, 128, 0, 0)
    ${wrong_color}  Evaluate  (0, 0, 0, 0)
    ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  ${expected_color}  ${wrong_color}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Foreground Color Should Be  ${TEXT_ELEMENT}  ${wrong_color}

Get Font Size
    ${expected_font_size}  Convert To Number  9.0
    ${font_size}  Get Font Size  ${TEXT_ELEMENT}
    Should Be Equal    ${font_size}  ${expected_font_size}

Font Size Should Be
    ${expected_font_size}  Convert To Number  9.0
    ${font_size}  Font Size Should Be  ${TEXT_ELEMENT}  ${expected_font_size}

Wrong Font Size Should Raise An Exception
    ${expected_font_size}  Convert To Number  9.0
    ${wrong_font_size}  Convert To Number  8.9
    ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  ${expected_font_size}  ${wrong_font_size}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Font Size Should Be  ${TEXT_ELEMENT}  ${wrong_font_size}

Get Font Name
    ${expected_font_name}  Convert To String  Segoe UI
    ${font_name}  Get Font Name  ${TEXT_ELEMENT}
    Should Be Equal    ${font_name}  ${expected_font_name}

Font Name Should Be
    ${expected_font_name}  Convert To String  Segoe UI
    Font Name Should Be  ${TEXT_ELEMENT}  ${expected_font_name}

Wrong Font Name Should Raise An Exception
    ${expected_font_name}  Convert To String  Segoe UI
    ${wrong_font_name}  Convert To String  Arial
    ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  ${expected_font_name}  ${wrong_font_name}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Font Name Should Be  ${TEXT_ELEMENT}  ${wrong_font_name}

Get Font Weight
    ${expected_font_weight}  Convert To Number  400.0
    ${font_weight}  Get Font Weight  ${TEXT_ELEMENT}
    Should Be Equal    ${font_weight}  ${expected_font_weight}

Font Weight Should Be
    ${expected_font_weight}  Convert To Number  400.0
    Font Weight Should Be  ${TEXT_ELEMENT}  ${expected_font_weight}

Wrong Font Weight Should Raise An Exception
    ${expected_font_weight}  Convert To Number  400.0
    ${wrong_font_weight}  Convert To Number  399
    ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  ${expected_font_weight}  ${wrong_font_weight}
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Font Weight Should Be  ${TEXT_ELEMENT}  ${wrong_font_weight}

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

Culture Should Be
    ${UIA}  Get Variable Value    ${UIA}

    IF  '${UIA}' == 'UIA2'
        ${ERR_MSG}      Run Keyword And Expect Error   *  Get Culture  ${TEXT_ELEMENT}
        Should Be Equal As Strings  ${EXP_PROPERTY_NOT_SUPPORTED}  ${ERR_MSG}
    ELSE
        ${expected_culture}  Convert To String  en-US
        Culture Should Be  ${TEXT_ELEMENT}  ${expected_culture}
    END

Wrong Culture Should Raise An Exception
    ${UIA}  Get Variable Value    ${UIA}

    IF  '${UIA}' == 'UIA2'
        ${ERR_MSG}      Run Keyword And Expect Error   *  Get Culture  ${TEXT_ELEMENT}
        Should Be Equal As Strings  ${EXP_PROPERTY_NOT_SUPPORTED}  ${ERR_MSG}
    ELSE
        ${wrong_culture}    Convert To String  de-DE
        ${expected_culture}  Convert To String  en-US
        ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  ${expected_culture}  ${wrong_culture}
        Run Keyword and Expect Error  ${EXP_ERR_MSG}  Culture Should Be  ${TEXT_ELEMENT}  ${wrong_culture}
    END

Is Hidden
    ${is_hidden}  Is Hidden  ${TEXT_ELEMENT}
    Should Be Equal    ${is_hidden}  ${False}

Is Visible
    ${is_visible}  Is Visible  ${TEXT_ELEMENT}
    Should Be Equal    ${is_visible}  ${True}

Get Window Visual State
    ${state}  Get Window Visual State  ${WINDOW_ELEMENT}
    Should Be Equal    ${state}  Normal

Window Visual State Should Be
    Window Visual State Should Be  ${WINDOW_ELEMENT}  Normal

Wrong Window Visual State Should Raise An Exception
    ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  Normal  Maximized
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Window Visual State Should Be  ${WINDOW_ELEMENT}  Maximized

Get Window Interaction State
    Focus  ${WINDOW_ELEMENT}
    ${state}  Get Window Interaction State  ${WINDOW_ELEMENT}
    Should Be Equal    ${state}  ReadyForUserInteraction

Window Interaction State Should Be
    Focus  ${WINDOW_ELEMENT}
    Window Interaction State Should Be  ${WINDOW_ELEMENT}  ReadyForUserInteraction

Wrong Window Interaction State Should Raise An Exception
    Focus  ${WINDOW_ELEMENT}
    ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  ReadyForUserInteraction  NotResponding
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Window Interaction State Should Be  ${WINDOW_ELEMENT}  NotResponding

Get Toggle State
    ${state}  Get Toggle State  ${TOGGLE_ELEMENT}
    Should Be Equal    ${state}  OFF

Toggle State Should Be
    Toggle State Should Be  ${TOGGLE_ELEMENT}  OFF

Wrong Toggle State Should Raise An Exception
    ${EXP_ERR_MSG}  Format String  ${EXP_PROPERTY_INEQUAL}  OFF  ON
    Run Keyword and Expect Error  ${EXP_ERR_MSG}  Toggle State Should Be  ${TOGGLE_ELEMENT}  ON

Set Visual State To
    Window Visual State Should Be  ${WINDOW_ELEMENT}  Normal
    Maximize Window   ${WINDOW_ELEMENT}
    Window Visual State Should Be  ${WINDOW_ELEMENT}  Maximized
    Minimize Window   ${WINDOW_ELEMENT}
    Window Visual State Should Be  ${WINDOW_ELEMENT}  Minimized
    Normalize Window  ${WINDOW_ELEMENT}
    Window Visual State Should Be  ${WINDOW_ELEMENT}  Normal

Can Window Be Maximized
    ${result}  Can Window Be Maximized  ${WINDOW_ELEMENT}
    Should Be True  ${result}

Can Window Be Minimized
    ${result}  Can Window Be Minimized  ${WINDOW_ELEMENT}
    Should Be True  ${result}
