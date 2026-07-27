"""
export.py
Save NakshPy patterns as images.
"""

import matplotlib.pyplot as plt


def save(filename="pattern.png"):
    """
    Save the current figure.
    """
    plt.savefig(filename, dpi=300, bbox_inches="tight")
