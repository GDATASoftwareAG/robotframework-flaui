from robotlibcore import keyword
from FlaUILibrary.flaui.module.application import Application
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class ApplicationKeywords:
    """
    Interface implementation from robotframework usage for application keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for application keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def attach_application_by_name(self, name, msg=None):
        """
        Attach to a running application by name.

        If application with name not exists an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description            |
        | name       | string | Process name to attach |
        | msg        | string | Custom error message   |

        Example:
        | ${pid}  Attach Application By Name  <APPLICATION>                     |
        | ${pid}  Attach Application By Name  <APPLICATION>  You shall not pass |

        Returns:
        | Process id from attached process if successfully |
        """
        return self._container.create_or_get_module().action(Application.Action.ATTACH_APPLICATION_BY_NAME,
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

        Example:
        | ${pid}  Attach Application By PID  <PID_NUMBER>                     |
        | ${pid}  Attach Application By PID  <PID_NUMBER>  You shall not pass |

        Returns:
        | Process id from attached process if successfully |

        """
        return self._container.create_or_get_module().action(Application.Action.ATTACH_APPLICATION_BY_PID,
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

        Example:
        | ${pid}  Launch Application  <APPLICATION> |
        | Close Application  ${pid}                 |

        """
        self._container.create_or_get_module().action(Application.Action.EXIT_APPLICATION,
                                                      Application.create_value_container(pid=pid, msg=msg),
                                                      msg=msg)

    @keyword
    def close_application_by_name(self, name, msg=None):
        """
        Closes the attached application by name.

        If no application is attached an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description          |
        | name       | string | Process name to close|
        | msg        | string | Custom error message |

        Example:
        | Close Application By Name  $[name}         |

        """
        self._container.create_or_get_module().action(Application.Action.CLOSE_APPLICATION_BY_NAME,
                                                      Application.create_value_container(name=name, msg=msg),
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

        Example:
        | ${pid}  Launch Application  <APPLICATION> |

        Returns:
        | Process id from started process if successfully |

        """
        return self._container.create_or_get_module().action(Application.Action.LAUNCH_APPLICATION,
                                                             Application.create_value_container(name=application,
                                                                                                msg=msg),
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

        Example:
        | ${pid}  Launch Application With Args  <APPLICATION>  <ARGUMENTS> |

        Returns:
        | Process id from started process if successfully |

        """
        module = self._container.create_or_get_module()
        return module.action(Application.Action.LAUNCH_APPLICATION_WITH_ARGS,
                             Application.create_value_container(name=application, args=arguments, msg=msg),
                             msg)

    @keyword
    def wait_for_application_while_busy_by_name(self, name, timeout=None, msg=None):
        """
        Wait for application when in busy state until timeout is reached.

        Arguments:
        | Argument    | Type   | Description                                        |
        | name        | string | Name from application to wait                      |
        | timeout     | number | Timeout to wait in milliseconds. If timeout is not set INFINITY will be used |
        | msg         | string | Custom error message                               |

        Example:
        | Wait For Application While Busy By Name  <NAME>  <TIMEOUT> |

        Raise FlaUiError:
        | If application could not be found by name. |

        Returns:
        | True if the application is idle, false otherwise |

        """
        module = self._container.create_or_get_module()
        return module.action(Application.Action.WAIT_WHILE_APPLICATION_IS_BUSY_BY_NAME,
                             Application.create_value_container(name=name, timeout=timeout, msg=msg),
                             msg)

    @keyword
    def wait_for_application_while_busy_by_pid(self, pid, timeout=None, msg=None):
        """
        Wait for application when in busy state until timeout is reached.

        Arguments:
        | Argument    | Type   | Description                                        |
        | pid         | number | PID from application to wait                       |
        | timeout     | number | Timeout to wait in milliseconds. If timeout is not set INFINITY will be used       |
        | msg         | string | Custom error message                               |

        Example:
        | Wait For Application While Busy By Pid  <PID>  <TIMEOUT> |

        Raise FlaUiError:
        | If application could not be found by name. |

        Returns:
        | True if the application is idle, false otherwise |

        """
        module = self._container.create_or_get_module()
        return module.action(Application.Action.WAIT_WHILE_APPLICATION_IS_BUSY_BY_PID,
                             Application.create_value_container(pid=pid, timeout=timeout, msg=msg),
                             msg)

    @keyword
    def wait_for_application_handle_by_pid(self, pid, timeout=None, msg=None):
        """
        Wait for application handle until timeout is reached.

        Arguments:
        | Argument    | Type   | Description                                        |
        | pid         | number | PID from application to wait                       |
        | timeout     | number | Timeout to wait in milliseconds. If timeout is not set INFINITY will be used      |
        | msg         | string | Custom error message                               |

        Example:
        | Wait For Application Handle By Pid  <PID>  <TIMEOUT> |

        Raise FlaUiError:
        | If application could not be found by pid. |

        Returns:
        | True a main window handle was found, false otherwise |

        """
        module = self._container.create_or_get_module()
        return module.action(Application.Action.WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_PID,
                             Application.create_value_container(pid=pid, timeout=timeout, msg=msg),
                             msg)

    @keyword
    def wait_for_application_handle_by_name(self, name, timeout=None, msg=None):
        """
        Wait for application handle until timeout is reached.

        Arguments:
        | Argument    | Type   | Description                                        |
        | name        | string | Name from application to wait                      |
        | timeout     | number | Timeout to wait in milliseconds. If timeout is not set INFINITY will be used       |
        | msg         | string | Custom error message                               |

        Example:
        | Wait For Application Handle By Name  <NAME>  <TIMEOUT> |

        Raise FlaUiError:
        | If application could not be found by name. |

        Returns:
        | True a main window handle was found, false otherwise |
        """
        module = self._container.create_or_get_module()
        return module.action(Application.Action.WAIT_WHILE_APPLICATION_HANDLE_IS_MISSING_BY_NAME,
                             Application.create_value_container(name=name, timeout=timeout, msg=msg),
                             msg)
