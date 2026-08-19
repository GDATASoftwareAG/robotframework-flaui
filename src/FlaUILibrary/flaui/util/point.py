from __future__ import annotations
from typing import Any


class Point:
    """
    Python point helper for mouse coordinates.
    """

    def __init__(self, x: int = 0, y: int = 0):
        """
        Create a point from x and y coordinates.

        Args:
            x (int): X coordinate
            y (int): Y coordinate
        """
        self.x = int(x)
        self.y = int(y)

    def offset(self, x: int = 0, y: int = 0) -> Point:
        """
        Return a new point moved by the given offset.

        Args:
            x (int): X offset
            y (int): Y offset
        """
        return Point(self.x + int(x), self.y + int(y))

    @staticmethod
    def from_clickable_point(clickable_point: Any) -> Point:
        """
        Create a point from a FlaUI clickable point object.

        Args:
            clickable_point (Any): Object exposing X and Y attributes.
        """
        return Point(clickable_point.X, clickable_point.Y)
