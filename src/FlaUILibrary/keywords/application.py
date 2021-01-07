from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.module.application import Application


class ApplicationKeywords:
    """
    Interface implementation from robotframework usage for application keywords.
    """

    def __init__(self, module):
        """Constructor for application keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def attach_application_by_name(self, name, msg=None):
        """Attach to an running application by name.

        If application with name not exists an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description            |
        | name       | string | Process name to attach |
        | msg        | string | Custom error message   |

        Examples:
        | Attach Application By Name  <APPLICATION>                     |
        | Attach Application By Name  <APPLICATION>  You shall not pass |


        """
        self._module.action(Application.Action.ATTACH_APPLICATION_BY_NAME, name, msg)

    @keyword
    def attach_application_by_pid(self, pid, msg=None):
        """Attach to an running application by pid.

        If application with pid not exists an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                  |
        | pid        | number | Process identifier to attach |
        | msg        | string | Custom error message         |

        Examples:
        | Attach Application By PID  <PID_NUMBER>                     |
        | Attach Application By PID  <PID_NUMBER>  You shall not pass |

        """
        self._module.action(Application.Action.ATTACH_APPLICATION_BY_PID, pid, msg)

    @keyword
    def close_application(self, msg=None):
        """Closes the attached application.

        If no application is attached an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description          |
        | msg        | string | Custom error message |

        Examples:
        | Launch Application  <APPLICATION> |
        | Close Application                 |

        """
        self._module.action(Application.Action.EXIT_APPLICATION, msg=msg)

    @keyword
    def launch_application(self, application, msg=None):
        """Launches an application.

        If application could not be found an error message will be thrown.

        Arguments:
        | Argument    | Type   | Description                                        |
        | application | string | Relative or absolute path to executable to launch  |
        | msg         | string | Custom error message                               |

        Examples:
        | Launch Application  <APPLICATION> |

        Returns:
        | Process id from started process if successfully |

        """
        return self._module.action(Application.Action.LAUNCH_APPLICATION, application, msg)
