class FlaUiError(AttributeError):
    """
    Error message handler
    """
    GenericError = "{}"
    ArrayOutOfBoundException = "Given index '{}' could not be found by element"
    ValueShouldBeANumber = "Given value '{}' should be number"
    ApplicationNotFound = "Application '{}' could not be found"
    ApplicationNotAttached = "Application is not attached"
    ApplicationPidNotFound = "Application with pid {} could not be found"
    ApplicationNameNotFound = "Application with name '{}' could not be found"
    NoElementAttached = "No element attached"
    ElementNameNotFound = "Name '{}' could not be found in element"
    ElementNameNotEquals = "Name from element '{}' is not equals to '{}'"
    ElementNameDoesNotContainsFromValue = "Name from element '{}' does not contains to '{}'"
    ElementNotClickable = "Element position could not be found because it is hidden."
    ActionNotSupported = "Action not supported"
    ElementExists = "Element '{}' exists"
    ElementVisible = "Element '{}' is visible"
    ElementNotVisible = "Element '{}' is not visible"
    ElementNotExpandable = "Element '{}' is not expandable"
    NoWindowWithNameFound = "No window with name '{}' found"
    WindowCloseNotSupported = "Close operation only supported for window elements"
    WrongElementType = "'{}' could not be cast as '{}'"
    XPathNotFound = "Element from XPath '{}' could not be found"
    ControlDoesNotContainItem = "Control does not contain item '{}'"
    ItemNotSelected = "Item '{}' is not selected"
    NoItemSelected = "No Item is selected"
    KeyboardInvalidKeysCombination = "Keyboard keys combination {} is not valid"
    KeyboardExtractionFailed = "Can't extract value from input"
    ListviewItemNotFound = "Item name '{}' could not be found in column with index '{}'"
    FalseSyntax = "Incorrect syntax usage '{}'"
    ArgumentShouldBeList = "The given argument should be an array"
    ArgumentShouldNotBeList = "The given argument should not be an array"

    @staticmethod
    def raise_fla_ui_error(message):
        """
        Static method usage to raise an FlaUI exception

        Args:
            message (String): Error message to raise.
        """
        raise FlaUiError(message)
