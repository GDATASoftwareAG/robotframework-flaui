from robot.running.context import EXECUTION_CONTEXTS


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
