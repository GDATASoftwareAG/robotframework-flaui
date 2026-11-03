import os
from datetime import datetime
from typing import Sequence, Tuple
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from robot.result import Message
from robot.running.context import EXECUTION_CONTEXTS
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
    Append testing log by a screenshot.

    The image is written to log.html only. Consoles and log listeners do not receive it.

    ``filepath`` Filepath from stored screenshot.
    """
    source = get_link_path(filepath, get_log_directory())
    _write_to_log_only(source)
    _write_to_log_only(
        '</td></tr><tr><td colspan="3">'
        f'<a href="{source}"><img src="{source}" width="800px"></a>',
        html=True,
    )


def log_screenshot_base64(image: str):
    """
    Append testing log by a screenshot in base64 format.

    The image is written to log.html only. Consoles and log listeners do not receive it.

    ``image`` Image as string in base64 encoding.
    """
    _write_to_log_only(
        '</td></tr><tr><td colspan="3">'
        f'<img src="data:image/png;base64,{image}" width="800px"/>',
        html=True,
    )


def _write_to_log_only(message: str, html: bool = False) -> None:
    """
    Write a screenshot message onto the current keyword.

    ``logger.info`` also notifies log listeners, so a Base64 screenshot would be
    printed as raw HTML in the debug console. The message is stored on the
    keyword result and in the output file instead, which is what log.html renders.
    """
    context = EXECUTION_CONTEXTS.current
    if context is None or not context.steps:
        return

    msg = Message(message, "INFO", html=html, timestamp=datetime.now())
    output_file = context.output.output_file
    if not output_file.is_logged(msg):
        return

    output_file.log_message(msg)
    context.steps[-1][1].body.append(msg)
