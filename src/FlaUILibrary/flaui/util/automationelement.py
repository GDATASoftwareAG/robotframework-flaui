import re


class AutomationElement:
    """ AutomationElement wrapper class which contains data about automation elements. """

    def __init__(self, automation_id: str, name: str, class_name: str, xpath: str):
        """
            Creates Automation Element entity.
            ``automation_id`` Automation ID if set by element.
            ``name`` Name if set by element.
            ``class_name`` Class Name from element.
            ``xpath`` Xpath from element.
        """
        self.Xpath = xpath
        self.AutomationId = ""
        self.Name = ""
        self.ClassName = ""

        if automation_id:
            self.AutomationId = self._get_argument_in_xpath(self.Xpath, "[@AutomationId=\"" + automation_id + "\"]")

        if name:
            self.Name = self._get_argument_in_xpath(self.Xpath, "[@Name=\"" + name + "\"]")

        if class_name:
            self.ClassName = self._get_argument_in_xpath(self.Xpath, "[@ClassName=\"" + class_name + "\"]")

    @staticmethod
    def _get_argument_in_xpath(xpath, argument) -> str:
        xpaths = xpath.split("/")
        xpaths[-1] = re.sub(r"\[\d+]", argument, xpaths[-1])
        return "/".join(xpaths)
