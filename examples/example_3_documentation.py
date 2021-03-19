# -*- coding: utf-8 -*-

"""Example 3 (style, lint, documentation).

Final version of the example code (slide 15), after adding documentation
(docstrings and an inline comment), type hints, and additional adjustments to
the names of the variables and dict keys.
"""

from typing import Dict


def convert_to_km(distance: float, print_output: bool = True) -> Dict[str, float]:
    """Convert a miles distance into the double of km.

    Args:
        distance: a distance (in miles).
        print_output: if True, prints the progress.

    Returns:
        A dictionary with two keys ('original' and 'converted').

    Raises:
        Exception: if the distance is not a valid value.
    """
    if distance is None:
        raise Exception('distance is not valid')

    if print_output:
        print("calculating ...", "Using ", distance)

    return {
        "original": distance,
        # The constant 2*1.60934 is used as the robot is magic and covers twice
        # the distance if specified in km.
        "converted": distance * 3.21868
    }
