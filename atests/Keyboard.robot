*** Settings ***
Documentation   Test suite for keyboard keywords.
...             XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...             Keyword                               Test Case Names
...             Press Key                             Keyboard Type Text
...                                                   Keyboard Type Shortcut Copy and Paste
...                                                   Delete Text
...                                                   False Argument Type
...             Press Keys                            Keyboard Type Text Multiple
...                                                   Keyboard Type Shortcut Select All
...                                                   Keyboard Type Shortcut Cut and Paste Multiple
...                                                   Keyboard Type Shortcut Copy and Paste Multiple
...                                                   Keyboard Type Generic Key Combination
...                                                   False Argument Type
...

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         Process
Library         StringFormat
Library         DateTime

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Suite Setup      Run Keywords  Init Main Application
...              AND           Open Keyboard Tab
Suite Teardown   Stop Application  ${MAIN_PID}
Test Setup       Wait Until Keyword Succeeds    5x    10ms    Reset Textbox

*** Variables ***
${XPATH_INPUT_FIELD}        ${MAIN_WINDOW_KEYBOARD_CONTROLS}/Edit[@AutomationId='KeyboardInputField']
${XPATH_RESET}              ${MAIN_WINDOW_KEYBOARD_CONTROLS}/Button[@AutomationId='ResetKeyboardInputs']
${XPATH_LABEL_INPUT_UP}     ${MAIN_WINDOW_KEYBOARD_CONTROLS}/Text[@AutomationId='lblKeyboardKeyDown']

${EXP_VALUE_INPUT_TEXT} =  Type text
${EXP_VALUE_OVERRIDE_INPUT_TEXT} =  Override
${EXP_VALUE_INPUT_TEXT_SHORTCUT} =  ${EXP_VALUE_INPUT_TEXT}${EXP_VALUE_INPUT_TEXT}

${KEYBOARD_INPUT_TEXT}             t'${EXP_VALUE_INPUT_TEXT}'
@{KEYBOARD_INPUT_TEXT_ARRAY}       t'${EXP_VALUE_INPUT_TEXT}'
@{KEYBOARD_INPUT_TEXT_X2}          t'${EXP_VALUE_INPUT_TEXT}'  t'${EXP_VALUE_INPUT_TEXT}'
@{KEYBOARD_INPUT_OVERRIDE_TEXT}    s'CTRL+A'  t'${EXP_VALUE_OVERRIDE_INPUT_TEXT}'
@{KEYBOARD_INPUT_SELECT_CUT_TEXT}  s'CTRL+A'  s'CTRL+X'
@{KEYBOARD_INPUT_COPY_PASTE_TEXT}  s'CTRL+A'  s'CTRL+C'
${KEYBOARD_INPUT_SELECTALL}        s'CTRL+A'
${KEYBOARD_INPUT_BACKSPACE}        s'BACK'
${KEYBOARD_INPUT_COPY}             s'CTRL+C'
${KEYBOARD_INPUT_PASTE}            s'CTRL+V'
@{KEYBOARD_INPUT_PASTE_ARRAY}      s'CTRL+V'
@{KEYBOARD_INPUT_TEXT_SHORTCUT}    t'${EXP_VALUE_INPUT_TEXT}'  s'CTRL+A'  s'CTRL+C'  s'END'  s'CTRL+V'

*** Test Cases ***
Keyboard Type Text By Delay
    ${TIME_BEFORE}  Get Current Date
	Press Key  ${KEYBOARD_INPUT_TEXT}   ${XPATH_INPUT_FIELD}  200
    Press Key  ${KEYBOARD_INPUT_TEXT}   ${XPATH_INPUT_FIELD}  200
	${TIME_AFTER}  Get Current Date
    ${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}${EXP_VALUE_INPUT_TEXT}  ${TEXT}
    ${TOTAL_MS}     Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True  ${TOTAL_MS} >= 0.4
    Should Be True  ${TOTAL_MS} < 0.8

Keyboard Types Text By Delay
    ${TIME_BEFORE}  Get Current Date
	Press Keys  ${KEYBOARD_INPUT_OVERRIDE_TEXT}   ${XPATH_INPUT_FIELD}  200
    Press Keys  ${KEYBOARD_INPUT_OVERRIDE_TEXT}   ${XPATH_INPUT_FIELD}  200
	${TIME_AFTER}  Get Current Date
    ${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}
    ${TOTAL_MS}     Subtract Date From Date    ${TIME_AFTER}    ${TIME_BEFORE}    result_format=number
    Should Be True  ${TOTAL_MS} >= 0.4
    Should Be True  ${TOTAL_MS} < 1.2

Keyboard Type Text
	Press Key  ${KEYBOARD_INPUT_TEXT}   ${XPATH_INPUT_FIELD}
    ${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

Keyboard Type Text Multiple
	Press Keys  ${KEYBOARD_INPUT_TEXT_X2}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT_SHORTCUT}  ${TEXT}

Keyboard Type Shortcut Select All
	Press Keys  ${KEYBOARD_INPUT_TEXT_ARRAY}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}
    Press Keys  ${KEYBOARD_INPUT_OVERRIDE_TEXT}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Cut and Paste Multiple
	Press Keys  ${KEYBOARD_INPUT_TEXT_ARRAY}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_OVERRIDE_TEXT}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_SELECT_CUT_TEXT}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EMPTY}  ${TEXT}

    Press Keys  ${KEYBOARD_INPUT_PASTE_ARRAY}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Copy and Paste Multiple
	Press Keys  ${KEYBOARD_INPUT_TEXT_ARRAY}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_COPY_PASTE_TEXT}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

    Press Keys  ${KEYBOARD_INPUT_PASTE_ARRAY}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Copy and Paste
	Press Key  ${KEYBOARD_INPUT_TEXT}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

	Press Key  ${KEYBOARD_INPUT_SELECTALL}  ${XPATH_INPUT_FIELD}
	Press Key  ${KEYBOARD_INPUT_COPY}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

    Press Key  ${KEYBOARD_INPUT_PASTE}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

Keyboard Type Generic Key Combination
	Press Keys  ${KEYBOARD_INPUT_TEXT_SHORTCUT}  ${XPATH_INPUT_FIELD}
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT_SHORTCUT}  ${TEXT}

Delete Text
	${LENGTH}  Get Length  ${EXP_VALUE_INPUT_TEXT_SHORTCUT}
	FOR   ${i}    IN RANGE  0  ${LENGTH}
		Press Key  ${KEYBOARD_INPUT_BACKSPACE}  ${XPATH_INPUT_FIELD}
	END
	${TEXT}  Get Text From Textbox  ${XPATH_INPUT_FIELD}
	Should Be Equal  ${TEXT}  ${EMPTY}

False Argument Type
    Run Keyword and Expect Error   ${EXP_ERR_MSG_ARGUMENT_ARRAY}  Press Keys  ${KEYBOARD_INPUT_TEXT}  ${XPATH_INPUT_FIELD}
    ${EXP_ERR_MSG}  Format String  ${EXP_INVALID_KEYBOARD_COMBINATION}  ${KEYBOARD_INPUT_TEXT_ARRAY}
	${ERR_MSG}      Run Keyword and Expect Error   *  Press Key   ${KEYBOARD_INPUT_TEXT_ARRAY}  ${XPATH_INPUT_FIELD}
    Should Be Equal As Strings  ${EXP_ERR_MSG}  ${ERR_MSG}

*** Keywords ***
Reset Textbox
    Click    ${XPATH_RESET}
    ${TEXT}  Get Name From Element  ${XPATH_LABEL_INPUT_UP}
    Should Be Empty  ${TEXT}
    Set Text To Textbox  ${XPATH_INPUT_FIELD}  ${EMPTY}
