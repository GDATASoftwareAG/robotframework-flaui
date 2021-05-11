*** Settings ***
Documentation   Test suite for keyboard keywords.

Library         FlaUILibrary  uia=${UIA}  screenshot_on_failure=False
Library         Process
Library         StringFormat

Resource        util/Common.robot
Resource        util/Error.robot
Resource        util/XPath.robot

Suite Setup      Start Application
Suite Teardown   Stop Application
Test Teardown  Reset Textbox

*** Variables ***
${XPATH_COMBO_BOX_INPUT}    ${MAIN_WINDOW_SIMPLE_CONTROLS}/ComboBox[@AutomationId='EditableCombo']

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
Keyboard Type Text
	Press Key  ${KEYBOARD_INPUT_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}
	
Keyboard Type Text Multiple
	Press Keys  ${KEYBOARD_INPUT_TEXT_X2}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT_SHORTCUT}  ${TEXT}

Keyboard Type Shortcut Select All
	Press Keys  ${KEYBOARD_INPUT_TEXT_ARRAY}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}
    Press Keys  ${KEYBOARD_INPUT_OVERRIDE_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Cut and Paste Multiple
	Press Keys  ${KEYBOARD_INPUT_TEXT_ARRAY}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_OVERRIDE_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_SELECT_CUT_TEXT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EMPTY}  ${TEXT}

    Press Keys  ${KEYBOARD_INPUT_PASTE_ARRAY}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_OVERRIDE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Copy and Paste Multiple
	Press Keys  ${KEYBOARD_INPUT_TEXT_ARRAY}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

	Press Keys  ${KEYBOARD_INPUT_COPY_PASTE_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

    Press Keys  ${KEYBOARD_INPUT_PASTE_ARRAY}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

Keyboard Type Shortcut Copy and Paste
	Press Key  ${KEYBOARD_INPUT_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

	Press Key  ${KEYBOARD_INPUT_SELECTALL}  ${XPATH_COMBO_BOX_INPUT}
	Press Key  ${KEYBOARD_INPUT_COPY}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

    Press Key  ${KEYBOARD_INPUT_PASTE}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT}  ${TEXT}

Keyboard Type Generic Key Combination
	Press Keys  ${KEYBOARD_INPUT_TEXT_SHORTCUT}  ${XPATH_COMBO_BOX_INPUT}
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${EXP_VALUE_INPUT_TEXT_SHORTCUT}  ${TEXT}

Delete Text
	${LENGTH}  Get Length  ${EXP_VALUE_INPUT_TEXT_SHORTCUT}
	FOR   ${i}    IN RANGE  0  ${LENGTH}
		Press Key  ${KEYBOARD_INPUT_BACKSPACE}  ${XPATH_COMBO_BOX_INPUT}
	END
	${TEXT}  Get Text From Textbox  ${XPATH_COMBO_BOX_INPUT}
	Should Be Equal  ${TEXT}  ${EMPTY}

False Argument Type
    Run Keyword and Expect Error   ${EXP_ERR_MSG_ARGUMENT_ARRAY}  Press Keys  ${KEYBOARD_INPUT_TEXT}  ${XPATH_COMBO_BOX_INPUT}
	Run Keyword and Expect Error   ${EXP_ERR_MSG_ARGUMENT_NOT_ARRAY}  Press Key   ${KEYBOARD_INPUT_TEXT_ARRAY}  ${XPATH_COMBO_BOX_INPUT}
	
*** Keywords ***
Reset Textbox
   Set Text To Textbox  ${XPATH_COMBO_BOX_INPUT}  ${EMPTY}