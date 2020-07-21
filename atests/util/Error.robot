*** Variables ***
${CUSTOM_ERR_MSG}                               You shall not pass
${EXP_GENERIC_ERR_MSG}                          FlaUiError: {0}
${EXP_CUSTOM_ERR_MSG}                           FlaUiError: You shall not pass
${EXP_ERR_MSG_VALUE_SHOULD_BE_A_NUMBER}         FlaUiError: Given value '{0}' should be number
${EXP_ERR_MSG_ARRAY_OUT_OF_BOUND}               FlaUiError: Given index '{0}' could not be found by element
${EXP_ERR_MSG_NO_ELEMENT_ATTACHED}              FlaUiError: No element attached
${EXP_ERR_MSG_XPATH_NOT_FOUND}                  FlaUiError: Element from XPath '{0}' could not be found
${EXP_ERR_MSG_NO_WINDOW_FOUND}                  FlaUiError: No window with name '{0}' found
${EXP_ERR_MSG_PID_NOT_FOUND}                    FlaUiError: Application with pid {0} could not be found
${EXP_ERR_MSG_APP_NAME_NOT_FOUND}               FlaUiError: Application with name '{0}' could not be found
${EXP_ERR_MSG_APP_NOT_EXIST}                    FlaUiError: Application '{0}' could not be found
${EXP_ERR_MSG_APP_NOT_ATTACHED}                 FlaUiError: Application is not attached
${EXP_ERR_MSG_NAME_DOES_NOT_CONTAIN}            FlaUiError: Name from element '{0}' does not contains to '{1}'
${EXP_ERR_MSG_NAME_NOT_EQUALS}                  FlaUiError: Name from element '{0}' is not equals to '{1}'
${EXP_ERR_MSG_WRONG_ELEMENT_TYPE}               FlaUiError: '{0}' could not be cast as '{1}'
${EXP_ERR_MSG_ELEMENT_DOES_NOT_EXISTS}          FlaUiError: Element does not exists
${EXP_ERR_MSG_ELEMENT_EXISTS}                   FlaUiError: Element '{0}' exists
${EXP_ERR_MSG_ELEMENT_VISIBLE}                  FlaUiError: Element '{0}' is visible
${EXP_ERR_MSG_ELEMENT_NOT_VISIBLE}              FlaUiError: Element '{0}' is not visible
${EXP_ERR_MSG_CONTROL_DOES_NOT_CONTAIN_ITEM}    FlaUiError: Control does not contain item '{0}'
${EXP_ERR_MSG_ITEM_NOT_SELECTED}                FlaUiError: Item '{0}' is not selected
${EXP_ERR_MSG_LISTVIEW_ITEM_NOT_FOUND}          FlaUiError: Item name '{0}' could not be found in column with index '{1}'