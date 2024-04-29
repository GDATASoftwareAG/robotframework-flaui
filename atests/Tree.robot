*** Settings ***
Documentation       Test suite for list box keywords.
...                 XPath not found error handling for all keywords must be implemented under ErrorHandling.robot
...

Library             Process
Library             FlaUILibrary    uia=${UIA}    screenshot_on_failure=False
Library             StringFormat
Resource            util/Common.resource
Resource            util/Error.resource
Resource            util/XPath.resource

Suite Setup         Run Keywords    Init Main Application
...                     AND    Open Complex Tab
Suite Teardown      Stop Application    ${MAIN_PID}
Test Teardown       Set Tree Item Seperator    ->


*** Variables ***
${XPATH_TREE}       ${MAIN_WINDOW_COMPLEX_CONTROLS}/Pane/Group/Tree[@AutomationId='treeView1']


*** Test Cases ***
Get Selected Treeitems Name No Item Selected
    Run Keyword And Expect Error    ${EXP_ERR_MSG_NO_ITEM_SELECTED}    Get Selected Treeitems Name    ${XPATH_TREE}

Get Root TreeItems Count
    ${COUNT}    Get Root TreeItems Count    ${XPATH_TREE}
    Should Be Equal As Integers    ${COUNT}    2

Get All Visible TreeItems Count
    ${COUNT}    Get All Visible TreeItems Count    ${XPATH_TREE}
    Should Be Equal As Integers    ${COUNT}    2

Get All Visible TreeItems Names
    ${Names}    Get All Visible TreeItems Names    ${XPATH_TREE}
    VAR    @{COMPARE_VALUE}    Lvl1 a    Lvl1 b
    Should Be Equal    ${Names}    ${COMPARE_VALUE}

Select Visible TreeItem By Name
    Select Visible TreeItem By Name    ${XPATH_TREE}    Lvl1 a
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl1 a
    Select Visible TreeItem By Name    ${XPATH_TREE}    Lvl1 b
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl1 b

Select Visible TreeItem By Name Wrong Element
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NAME_NOT_FOUND}    Lvl3 a
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Select Visible TreeItem By Name    ${XPATH_TREE}    Lvl3 a

Selected TreeItem Should Be Item Not Exist
    Select Visible TreeItem By Name    ${XPATH_TREE}    Lvl1 a
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ITEM_NOT_SELECTED}    No Such Item
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Selected TreeItem Should Be    ${XPATH_TREE}    No Such Item

Expand All TreeItems
    Expand All TreeItems    ${XPATH_TREE}
    ${COUNT}    Get All Visible TreeItems Count    ${XPATH_TREE}
    Should Be Equal As Integers    ${COUNT}    6

TreeItem Should Be Visible After Expand
    TreeItem Should Be Visible    ${XPATH_TREE}    Lvl3 a

Get All Visible TreeItems Names After Expand
    ${Names}    Get All Visible TreeItems Names    ${XPATH_TREE}
    VAR    @{COMPARE_VALUE}    Lvl1 a    Lvl2 a    Lvl2 b    Lvl3 a    Lvl2 b    Lvl1 b
    Should Be Equal    ${Names}    ${COMPARE_VALUE}

Select Visible TreeItem By Name After Expand
    Select Visible TreeItem By Name    ${XPATH_TREE}    Lvl3 a
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl3 a

Collapse TreeItem
    Collapse TreeItem    ${XPATH_TREE}    I:0->I:1
    ${COUNT}    Get All Visible TreeItems Count    ${XPATH_TREE}
    Should Be Equal As Integers    ${COUNT}    5

Expand TreeItem
    Expand TreeItem    ${XPATH_TREE}    I:0->I:1
    ${COUNT}    Get All Visible TreeItems Count    ${XPATH_TREE}
    Should Be Equal As Integers    ${COUNT}    6

Collapse All TreeItems
    Collapse All TreeItems    ${XPATH_TREE}
    ${COUNT}    Get All Visible TreeItems Count    ${XPATH_TREE}
    Should Be Equal As Integers    ${COUNT}    2

Expand TreeItem Not Expandable
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_EXPANDABLE}    Lvl1 b
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Expand TreeItem    ${XPATH_TREE}    I:1

Collapse TreeItem Not Expandable
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_EXPANDABLE}    Lvl1 b
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Collapse TreeItem    ${XPATH_TREE}    I:1

TreeItem Should Not Be Visible After Collapse
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NOT_VISIBLE}    Lvl3 a
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    TreeItem Should Be Visible    ${XPATH_TREE}    Lvl3 a

Get Selected Treeitems Name
    Select Visible TreeItem By Name    ${XPATH_TREE}    Lvl1 a
    ${Name}    Get Selected Treeitems Name    ${XPATH_TREE}
    Should Be Equal    ${Name}    Lvl1 a

Select TreeItem
    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a->I:1->N:Lvl3 a
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl3 a
    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a->N:Lvl2 a
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl2 a
    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl1 a
    Select TreeItem    ${XPATH_TREE}    I:0
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl1 a

Select TreeItem Wrong Element Name
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ELEMENT_NAME_NOT_FOUND}    Lvl3 b
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a->I:1->N:Lvl3 b

Select TreeItem Wrong Filter Name False Syntax
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_FALSESYNTAX}    n:Lvl3 b
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a->I:1->n:Lvl3 b
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_FALSESYNTAX}    ILvl3 b
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a->I:1->ILvl3 b

Select TreeItem By Index
    Select TreeItem    ${XPATH_TREE}    I:0->I:1->I:0
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl3 a

Select TreeItem By Index Wrong Index
    ${EXP_ERR_MSG}    Format String    ${EXP_ERR_MSG_ARRAY_OUT_OF_BOUND}    1
    Run Keyword And Expect Error    ${EXP_ERR_MSG}    Select TreeItem    ${XPATH_TREE}    I:0->I:1->I:1
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl2 b

Select TreeItem With Custom Seperator
    Set Tree Item Seperator    ${SPACE}->${SPACE}
    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a -> I:1 -> N:Lvl3 a
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl3 a
    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a -> N:Lvl2 a
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl2 a
    Select TreeItem    ${XPATH_TREE}    N:Lvl1 a
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl1 a
    Select TreeItem    ${XPATH_TREE}    I:0
    Selected TreeItem Should Be    ${XPATH_TREE}    Lvl1 a

Expand TreeItem With Custom Seperator
    Set Tree Item Seperator    ${SPACE}->${SPACE}
    Expand TreeItem    ${XPATH_TREE}    I:0 -> I:1
    ${COUNT}    Get All Visible TreeItems Count    ${XPATH_TREE}
    Should Be Equal As Integers    ${COUNT}    6

Collapse TreeItem With Custom Seperator
    Set Tree Item Seperator    ${SPACE}->${SPACE}
    Collapse TreeItem    ${XPATH_TREE}    I:0 -> I:1
    ${COUNT}    Get All Visible TreeItems Count    ${XPATH_TREE}
    Should Be Equal As Integers    ${COUNT}    5
