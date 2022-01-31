from robotlibcore import keyword
from FlaUILibrary.flaui.module.application import Application


class ApplicationKeywords:
    """
    Interface implementation from robotframework usage for application keywords.
    """

    def __init__(self, module):
        """
        Constructor for application keywords.

        ``module`` UIA3 module to handle element interaction.
        """
        self._module = module

    @keyword
    def attach_application_by_name(self, name, msg=None):
        """
        Attach to a running application by name.

        If application with name not exists an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description            |
        | name       | string | Process name to attach |
        | msg        | string | Custom error message   |

        Examples:
        | ${pid}  Attach Application By Name  <APPLICATION>                     |
        | ${pid}  Attach Application By Name  <APPLICATION>  You shall not pass |

        Returns:
        | Process id from attached process if successfully |
        """
        return self._module.action(Application.Action.ATTACH_APPLICATION_BY_NAME,
                                   Application.create_value_container(name=name, msg=msg),
                                   msg)

    @keyword
    def attach_application_by_pid(self, pid, msg=None):
        """
        Attach to a running application by pid.

        If application with pid not exists an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                  |
        | pid        | number | Process identifier to attach |
        | msg        | string | Custom error message         |

        Examples:
        | ${pid}  Attach Application By PID  <PID_NUMBER>                     |
        | ${pid}  Attach Application By PID  <PID_NUMBER>  You shall not pass |

        Returns:
        | Process id from attached process if successfully |

        """
        return self._module.action(Application.Action.ATTACH_APPLICATION_BY_PID,
                                   Application.create_value_container(pid=pid, msg=msg),
                                   msg)

    @keyword
    def close_application(self, pid, msg=None):
        """
        Closes the attached application.

        If no application is attached an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description          |
        | pid        | int    | Process id to close  |
        | msg        | string | Custom error message |

        Examples:
        | $[pid}  Launch Application  <APPLICATION> |
        | Close Application  $[pid}                 |

        """
        self._module.action(Application.Action.EXIT_APPLICATION,
                            Application.create_value_container(pid=pid, msg=msg),
                            msg=msg)

    @keyword
    def launch_application(self, application, msg=None):
        """
        Launches an application.

        If application could not be found an error message will be thrown.

        Arguments:
        | Argument    | Type   | Description                                        |
        | application | string | Relative or absolute path to executable to launch  |
        | msg         | string | Custom error message                               |

        Examples:
        | ${pid}  Launch Application  <APPLICATION> |

        Returns:
        | Process id from started process if successfully |

        """
        return self._module.action(Application.Action.LAUNCH_APPLICATION,
                                   Application.create_value_container(name=application, msg=msg),
                                   msg)

    @keyword
    def launch_application_with_args(self, application, arguments, msg=None):
        """
        Launches an application with given arguments.

        If application could not be found an error message will be thrown.

        Arguments:
        | Argument    | Type   | Description                                        |
        | application | string | Relative or absolute path to executable to launch  |
        | arguments   | string | Arguments for application to start                 |
        | msg         | string | Custom error message                               |

        Examples:
        | ${pid}  Launch Application  <APPLICATION>  <ARGUMENTS> |

        Returns:
        | Process id from started process if successfully |

        """
        return self._module.action(Application.Action.LAUNCH_APPLICATION_WITH_ARGS,
                                   Application.create_value_container(name=application, args=arguments, msg=msg),
                                   msg)
