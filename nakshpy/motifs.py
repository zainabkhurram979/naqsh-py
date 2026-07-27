"""
motifs.py
Pattern generators for NakshPy.
"""

import math
from .geometry import Point


def regular_polygon(sides=6, radius=1):
    """
    Generate a regular polygon.
    """
    points = []

    for i in range(sides):
        angle = 2 * math.pi * i / sides

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        points.append(Point(x, y))

    return points


def star_pattern(points=8, outer_radius=1, inner_radius=0.5):
    """
    Generate a star pattern.
    """
    vertices = []

    total = points * 2

    for i in range(total):

        if i % 2 == 0:
            radius = outer_radius
        else:
            radius = inner_radius

        angle = math.pi * i / points

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        vertices.append(Point(x, y))

    return vertices


def ajrak_tile(size=1):
    """
    Simple Ajrak-inspired geometric motif.
    """

    return [
        Point(-size, 0),
        Point(0, size),
        Point(size, 0),
        Point(0, -size)
    ]
