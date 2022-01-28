*** Settings ***
Library  FlaUILibrary
Library  Process

*** Variables ***
${FULL_XPATH}         /Window[@Name="FlaUI WPF Test App"]/Tab/TabItem[@Name="Simple Controls"]/Edit[@AutomationId="TextBox"]
${XPATH_SEARCH}       //Edit[@AutomationId="TextBox"]
${XPATH_CONTAINS}     /Window[contains(@Name,"FlaUI WPF")]//Edit[@AutomationId="TextBox"]
${XPATH_STARTS_WITH}  /Window[starts-with(@Name, "FlaUI")]//Edit[@AutomationId="TextBox"]
${XPATH_CONTAINS_OR}  /Window[contains(@Name,"FlaUI WPF")]/TitleBar/Button[@Name="Schließen" or @Name="Close" or @AutomationId="Close"]

*** Keywords ***
Start Application
    ${PID}       Start Process  WpfApplication.exe
    Should Not Be Equal As Integers  ${PID}  0
    Set Global Variable   ${PID}

Stop Application
    [Arguments]   ${pid}
    Terminate Process  ${pid}  kill=true

Test XPath
    [Arguments]   ${xpath}  ${text}
    Set Text To Textbox  ${xpath}  ${text}
    Sleep  10s

*** Test Cases ***
XPath Examples
  [Documentation]  
  ...  XPath example usage by different approaches:
  ...  FULL_XPATH example
  ...  XPATH_SEARCH pattern by //
  ...  XPATH_PROPERTY starts_with by starts-with(Property, Value)
  ...  XPATH_CONTAINS pattern by contains(Property, Value)
  [Setup]  Start Application
  Test XPath  ${FULL_XPATH}      FULL_XPATH
  Test XPath  ${XPATH_SEARCH}    XPATH_SEARCH
  Test XPath  ${XPATH_STARTS_WITH}  XPATH_STARTS_WITH
  Test XPath  ${XPATH_CONTAINS}  XPATH_CONTAINS
  [Teardown]  Stop Application  ${pid}

XPath Contains Or Example
  [Documentation]  
  ...  This example show xpath or usage by specific properties and languages.
  ...  German or English xpath usage if desktop is localized in germany or english
  ...  For all other langauges AutomationId will be used because names does not work anymore.
  ...  Xpath logic operation example by [or | and]
  [Setup]  Start Application
  Click  ${XPATH_CONTAINS_OR}
  [Teardown]  Element Should Not Exist  /Window[@Name="FlaUI WPF Test App"]
