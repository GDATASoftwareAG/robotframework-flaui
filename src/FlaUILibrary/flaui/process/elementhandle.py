class ElementHandle:
    """Picklable reference to a native FlaUI element stored in the worker."""

    def __init__(self, handle: int):
        self.handle = handle
