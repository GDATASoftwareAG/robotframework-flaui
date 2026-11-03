class LogListener:
    """Records log messages delivered to listeners, as a debug console would."""

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        self.messages = []

    def log_message(self, message):
        """Remember one message delivered to log listeners."""
        if isinstance(message, dict):
            text = message.get("message") or ""
        else:
            text = getattr(message, "message", "") or ""
        self.messages.append(text)

    def reset(self):
        """Clear the messages recorded so far."""
        self.messages.clear()

    def received(self, fragment):
        """Return whether any recorded message contains ``fragment``."""
        return any(fragment in message for message in self.messages)
