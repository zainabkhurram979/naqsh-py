"""
visualization.py
Functions for displaying NakshPy patterns.
"""

import matplotlib.pyplot as plt


def draw(points, color="navy", show_points=True):
    """
    Draw a list of Point objects.
    """

    x = [p.x for p in points]
    y = [p.y for p in points]

    # Close the shape
    x.append(points[0].x)
    y.append(points[0].y)

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, color=color)

    if show_points:
        plt.scatter(x[:-1], y[:-1])

    plt.gca().set_aspect("equal")
    plt.grid(True)
    plt.title("NakshPy Pattern")

    plt.show()
