"""
geometry.py
Basic geometric objects used throughout NakshPy.
"""

from dataclasses import dataclass
import math


@dataclass
class Point:
    """
    Represents a point in 2D space.
    """
    x: float
    y: float

    def distance_to(self, other):
        """
        Calculate the distance to another point.
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


@dataclass
class Line:
    """
    Represents a line segment between two points.
    """
    start: Point
    end: Point

    def length(self):
        return self.start.distance_to(self.end)


@dataclass
class Polygon:
    """
    Represents a polygon defined by its vertices.
    """
    vertices: list

    def perimeter(self):
        total = 0

        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]

            total += p1.distance_to(p2)

        return total

    def translate(self, dx, dy):
        """
        Move the polygon.
        """
        for point in self.vertices:
            point.x += dx
            point.y += dy
