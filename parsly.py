from xml.sax import parse
from xml.sax.handler import ContentHandler
from yattag import Doc, indent


def save_xml(testsuite, testcase_stack, filename):

    doc, tag, text = Doc().tagtext()

    testsuite_name = testsuite[0]
    testsuite_args = testsuite[1]

    with tag(testsuite_name, name=_get_value(testsuite_args, 'name', 'Unknown'),
             tests=_get_value(testsuite_args, 'tests', '0'),
             errors=_get_value(testsuite_args, 'errors', '0'),
             failures=_get_value(testsuite_args, 'failures', '0'),
             skipped=_get_value(testsuite_args, 'skipped', '0'),
             time=_get_value(testsuite_args, 'time', '0')):

        for testcase in testcase_stack:
            testcase_name = testcase['name']
            testcase_args = testcase['attributes']

            with tag(testcase_name, classname=_get_value(testcase_args, 'classname', 'Unknown'),
                     name=_get_value(testcase_args, 'name', 'Unknown'),
                     time=_get_value(testcase_args, 'time', '0')):

                if 'failure' in testcase:
                    failure_args = testcase['failure']
                    with tag('failure', message=_get_value(failure_args, 'message', 'Failed test execution'),
                             name=_get_value(failure_args, 'type', 'Unknown Type')):
                        pass

                pass

    result = '<?xml version="1.0" encoding="utf-8"?>\n' + indent(
        doc.getvalue(),
        newline='\n'
    )

    with open(filename, 'w') as f:
        f.write(result)


def _get_value(attrs, key, default_value):
    try:
        return attrs[key]
    except KeyError:
        return default_value


class Parsly(ContentHandler):

    def __init__(self):
        super().__init__()
        self.testcase_stack = []
        self.testsuite = None

    def startElement(self, name, attrs):

        if name == 'testcase':
            self.testcase_stack.append({
                'name': name,
                'attributes': dict(attrs)
            })
            return

        if name == 'failure':
            data = self.testcase_stack.pop()
            data['failure'] = dict(attrs)
            self.testcase_stack.append(data)
            return

        if not self.testsuite and name == 'testsuite':
            self.testsuite = (name, attrs)
            return


parsly = Parsly()
parse('./result/rebot_xunit.xml', parsly)
save_xml(parsly.testsuite, parsly.testcase_stack, './result/xunit.xml')
