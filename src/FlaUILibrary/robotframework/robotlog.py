import os
from typing import Sequence, Tuple
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.api import logger
from robot.utils import get_link_path


def get_log_directory():
    """
    Get output directory from robot framework built in variables if not exists fallback to os path execution
    """
    try:
        return BuiltIn().get_variable_value("${OUTPUT DIR}")
    except RobotNotRunningError:
        return os.getcwd()


def log(message: str):
    """
    Log given message to robot result.

    ``message`` Message to log to robot.
    """
    logger.info(message)


def publish_screenshot_logs(entries: Sequence[Tuple[str, str]]) -> None:
    """
    Write screenshot log entries collected in the UIA helper process.

    ``entries`` Sequence of ``("file", path)`` or ``("base64", image)`` tuples.
    """
    for kind, value in entries:
        if kind == "file":
            log_screenshot(value)
        elif kind == "base64":
            log_screenshot_base64(value)


def log_screenshot(filepath: str):
    """
    Append testing log by a screenshot

    ``filepath`` Filepath from stored screenshot.
    """
    source = get_link_path(filepath, get_log_directory())
    logger.info(source)
    logger.info(
        '</td></tr><tr><td colspan="3">'
        f'<a href="{source}"><img src="{source}" width="800px"></a>',
        html=True,
    )


def log_screenshot_base64(image: str):
    """
    Append testing log by a screenshot in base64 format.

    ``image`` Image as string in base64 encoding.
    """
    logger.info(
        '</td></tr><tr><td colspan="3">'
        f'<img src="data:image/png;base64,{image}" width="800px"/>',
        html=True
    )
