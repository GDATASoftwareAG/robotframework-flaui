import re


class AutomationElement:
    """Automation element data returned by Find One Element and Find All Elements.

    ``Name``, ``ClassName`` and ``AutomationId`` are the raw property values.
    ``Xpath`` is the positional locator. When a property exists, ``XpathName``,
    ``XpathClassName`` and ``XpathAutomationId`` use that property on the last segment
    instead of its positional index.
    A missing property is an empty string on the raw field and on its xpath field.
    """

    def __init__(self, automation_id: str, name: str, class_name: str, xpath: str):
        """
            Creates Automation Element entity.
            ``automation_id`` Automation ID if set by element.
            ``name`` Name if set by element.
            ``class_name`` Class Name from element.
            ``xpath`` Positional xpath from element.
        """
        # pylint: disable=C0103
        self.Xpath = xpath or ""
        self.AutomationId = str(automation_id) if automation_id else ""
        self.Name = str(name) if name else ""
        self.ClassName = str(class_name) if class_name else ""
        self.XpathAutomationId = self._property_xpath(self.Xpath, "AutomationId", self.AutomationId)
        self.XpathClassName = self._property_xpath(self.Xpath, "ClassName", self.ClassName)
        self.XpathName = self._property_xpath(self.Xpath, "Name", self.Name)
        # pylint: enable=C0103

    @staticmethod
    def _property_xpath(xpath: str, attribute: str, value: str) -> str:
        """Put one property on the last segment when that property exists.

        ``/Window[1]/Tab/TabItem[1]`` with Name ``Simple Controls`` becomes
        ``/Window[1]/Tab/TabItem[@Name="Simple Controls"]``.
        A positional index on the last segment is replaced. Earlier segments stay unchanged.
        """
        if not value:
            return ""
        segments = xpath.split("/")
        last = re.sub(r"\[\d+]", "", segments[-1])
        segments[-1] = f'{last}[@{attribute}="{value}"]'
        return "/".join(segments)
