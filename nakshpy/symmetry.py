"""
symmetry.py
Geometric transformations for NakshPy.
"""

import math
from .geometry import Point


def rotate(points, angle):
    """
    Rotate a list of points around the origin.
    """
    radians = math.radians(angle)
    cos_a = math.cos(radians)
    sin_a = math.sin(radians)

    rotated = []

    for p in points:
        x = p.x * cos_a - p.y * sin_a
        y = p.x * sin_a + p.y * cos_a
        rotated.append(Point(x, y))

    return rotated


def translate(points, dx, dy):
    """
    Move all points by (dx, dy).
    """
    return [Point(p.x + dx, p.y + dy) for p in points]


def scale(points, factor):
    """
    Scale all points from the origin.
    """
    return [Point(p.x * factor, p.y * factor) for p in points]


def reflect_x(points):
    """
    Reflect points across the x-axis.
    """
    return [Point(p.x, -p.y) for p in points]


def reflect_y(points):
    """
    Reflect points across the y-axis.
    """
    return [Point(-p.x, p.y) for p in points]
