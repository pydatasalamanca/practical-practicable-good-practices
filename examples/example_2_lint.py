# -*- coding: utf-8 -*-

"""Example 2 (style, lint, no documentation).

Third version of the example code (slide 13b), after applying `pylint` and
manually fixing the warnings and applying some changes based on the tool
suggestions.
"""


def calculate(distance, print_output=True):
    if distance is None:
        raise Exception('distance is not valid')

    if print_output:
        print("calculating ...", "Using ", distance)

    return {
        "orig": distance,
        "comp": distance * 3.21868
    }
