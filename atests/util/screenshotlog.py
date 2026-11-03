from robot.running.context import EXECUTION_CONTEXTS

from loglistener import LogListener


_CONSOLE = LogListener()
ROBOT_LIBRARY_LISTENER = _CONSOLE


def reset_log_listener():
    """Clear messages observed by the log listener."""
    _CONSOLE.reset()


def publish_base64_screenshot(image):
    """Log a Base64 screenshot the same way a captured screenshot is logged."""
    from FlaUILibrary.robotframework import robotlog  # pylint: disable=import-outside-toplevel

    robotlog.log_screenshot_base64(image)


def publish_file_screenshot(filepath):
    """Log a file screenshot the same way a captured screenshot is logged."""
    from FlaUILibrary.robotframework import robotlog  # pylint: disable=import-outside-toplevel

    robotlog.log_screenshot(filepath)


def log_listener_should_have_received(fragment):
    """Fail when no listener message contains ``fragment``."""
    if _CONSOLE.received(fragment):
        return
    raise AssertionError(
        f"Listener did not receive '{fragment}'. Saw {len(_CONSOLE.messages)} message(s)."
    )


def log_listener_should_not_have_received(fragment):
    """Fail when a listener message contains ``fragment``."""
    for message in _CONSOLE.messages:
        if fragment in message:
            preview = message if len(message) < 180 else message[:180] + "..."
            raise AssertionError(f"Screenshot was published to a log listener: {preview}")


def log_should_contain_screenshot(fragment):
    """
    Fail when the current test log has no HTML message containing fragment.

    Args:
        fragment: Text expected inside an HTML log message, such as an image tag.
    """
    test = EXECUTION_CONTEXTS.current.test
    for message in _html_messages(test):
        if fragment in message:
            return
    raise AssertionError(f"Screenshot was not embedded in the log. Missing '{fragment}'.")


def _html_messages(item, seen=None):
    if seen is None:
        seen = set()
    marker = id(item)
    if marker in seen:
        return
    seen.add(marker)

    if getattr(item, "html", False):
        message = getattr(item, "message", None)
        if message:
            yield message

    body = getattr(item, "body", None)
    if body is None:
        return
    try:
        children = list(body)
    except TypeError:
        return
    for child in children:
        yield from _html_messages(child, seen)
