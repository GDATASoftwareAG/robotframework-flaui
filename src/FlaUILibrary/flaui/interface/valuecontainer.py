try:
    from typing import TypedDict  # Python >=3.8
except ImportError:
    from typing_extensions import TypedDict  # Python <=3.7


class ValueContainer(TypedDict):
    """
    Default value container class for an flaui wrapper module.
    """
