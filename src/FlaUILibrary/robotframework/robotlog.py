import os
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.api import logger
from robot.utils import get_link_path


def get_log_directory():
    """Get output directory from robot framework built in variables if not exists fallback to os path execution"""
    try:
        return BuiltIn().get_variable_value("${OUTPUT DIR}")
    except RobotNotRunningError:
        return os.getcwd()


def log(message):
    """Log given message to robot result.

    ``message`` Message to log to robot.
    """
    logger.info(message)


def log_screenshot(filepath):
    """Append testing log by a screenshot

    ``filepath`` Filepath from stored screenshot.
    """
    logger.info(get_link_path(filepath, get_log_directory()))
    logger.info(
        '</td></tr><tr><td colspan="3">'
        '<a href="{src}"><img src="{src}" width="800px"></a>'.format(
            src=get_link_path(filepath, get_log_directory())
        ),
        html=True,
    )
