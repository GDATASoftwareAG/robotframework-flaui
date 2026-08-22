class EnumHandle:
    """Picklable reference to a Python Enum whose value is a native .NET object."""

    def __init__(self, module: str, qualname: str, name: str):
        self.module = module
        self.qualname = qualname
        self.name = name
