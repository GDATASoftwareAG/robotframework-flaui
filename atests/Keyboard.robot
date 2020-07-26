*** Settings ***
Documentation   Test Cases for Windows keywords.

Library         FlaUILibrary  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Test Setup      Start Application
Test Teardown   Stop Application

*** Variables ***
${XPATH_COMBO_BOX_INPUT}    ${MAIN_WINDOW_SIMPLE_CONTROLS}/ComboBox[@AutomationId='EditableCombo']

${EXP_VALUE_INPUT_TEXT} =  Type text
${EXP_VALUE_OVERRIDE_INPUT_TEXT} =  Override
${EXP_VALUE_INPUT_TEXT_SHORTCUT} =  ${EXP_VALUE_INPUT_TEXT}${EXP_VALUE_INPUT_TEXT}

@{KEYBOARD_INPUT_TEXT}             t'${EXP_VALUE_INPUT_TEXT}'
@{KEYBOARD_INPUT_OVERRIDE_TEXT}    s'CTRL+A'  t'${EXP_VALUE_OVERRIDE_INPUT_TEXT}'
@{KEYBOARD_INPUT_SELECT_CUT_TEXT}  s'CTRL+A'  s'CTRL+X'
@{KEYBOARD_INPUT_COPY_PASTE_TEXT}  s'CTRL+A'  s'CTRL+C'
@{KEYBOARD_INPUT_PASTE}            s'CTRL+V'
@{KEYBOARD_INPUT_TEXT_SHORTCUT}    t'${EXP_VALUE_INPUT_TEXT}'  s'CTRL+A'  s'CTRL+C'  s'END'  s'CTRL+V'

*** Test Cases ***
Keyboard Type Wrong XPath
    ${EXP_ERR_MSG}  Format String  ${EXP_ERR_MSG_XPATH_NOT_FOUND}  ${XPATH_NOT_EXISTS}
    Run Keyword And Expect Error   ${EXP_ERR_MSG}  Press Keys  ${KEYBOARD_INPUT_TEXT_SHORTCUT}  ${XPATH_NOT_EXISTS}

Keyboard Type Text
	Press Keys  ${KEYBOARD_INPUT_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Select All
	Press Keys  ${KEYBOARD_INPUT_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}
    Press Keys  ${KEYBOARD_INPUT_OVERRIDE_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Cut and Paste
	Press Keys  ${KEYBOARD_INPUT_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_OVERRIDE_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_SELECT_CUT_TEXT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EMPTY}  ${TEXT}

    Press Keys  ${KEYBOARD_INPUT_PASTE}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Copy and Paste
	Press Keys  ${KEYBOARD_INPUT_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_COPY_PASTE_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

    Press Keys  ${KEYBOARD_INPUT_PASTE}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

Keyboard Type Generic Key Combination
	Press Keys  ${KEYBOARD_INPUT_TEXT_SHORTCUT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT_SHORTCUT}  ${TEXT}
