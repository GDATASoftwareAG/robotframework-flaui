*** Variables ***
# Default common xpath usage
${MAIN_WINDOW}                      /Window[@Name='FlaUI WPF Test App']
${MAIN_WINDOW_NOTIFIER}             /Window[@AutomationId='Notifier']
${MAIN_WINDOW_MFC}                  /Window[@Name='MFCApplication1 - MFCApplication']
${XPATH_NOT_EXISTS}                 /NotExists
${MAIN_WINDOW_CONTROLS}             ${MAIN_WINDOW}/Tab/TabItem
${MAIN_WINDOW_SIMPLE_CONTROLS}      ${MAIN_WINDOW}/Tab/TabItem[@Name='Simple Controls']
${MAIN_WINDOW_COMPLEX_CONTROLS}     ${MAIN_WINDOW}/Tab/TabItem[@Name='Complex Controls']
${MAIN_WINDOW_KEYBOARD_CONTROLS}    ${MAIN_WINDOW}/Tab/TabItem[@Name='Keyboard Controls']
