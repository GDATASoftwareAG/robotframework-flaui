from typing import List, Tuple


class ScreenshotLogBuffer:
    """
    Holds screenshot log entries captured in the UIA helper process.

    That process has no Robot log, so the worker returns these entries and the
    Robot process writes them on the keyword that captured the screenshot.
    """

    def __init__(self):
        self._entries: List[Tuple[str, str]] = []

    def add_file(self, filepath: str) -> None:
        """Remember a screenshot file until it can be written to the Robot log."""
        self._entries.append(("file", filepath))

    def add_base64(self, image: str) -> None:
        """Remember a Base64 screenshot until it can be written to the Robot log."""
        self._entries.append(("base64", image))

    def take(self) -> List[Tuple[str, str]]:
        """Return the remembered entries and clear this buffer."""
        entries = self._entries
        self._entries = []
        return entries
