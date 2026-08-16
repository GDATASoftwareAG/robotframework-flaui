class KeywordUtil:
    """
    Helper class for optional XPath identifier handling in keyword implementations.
    """

    @staticmethod
    def has_identifier(identifier):
        """
        Returns True if identifier is set and not empty.
        """
        return identifier is not None and identifier != ""

    @staticmethod
    def get_optional_element(module, identifier, msg=None):
        """
        Returns the element for identifier or None if identifier is not set.
        """
        if not KeywordUtil.has_identifier(identifier):
            return None
        return module.get_element(identifier=identifier, msg=msg)
