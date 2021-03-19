# -*- coding: utf-8 -*-

"""Example 1 (style, no lint, no documentation).

Second version of the example code (slide 10b), after applying style (`black`
and `pycodestyle`, manually fixing the pycodestyle comparison warning).
"""


def Calculate(A, B={}, print=True):
    if A is None:
        if print:
            print("A is not valid")
        return

    elif A is not None:
        if print:
            print("calculating ...", "Using ", A)
    C = {}
    C["orig"] = A
    # C['comp'] = A*2??????
    C["comp"] = A * 3.21868
    return C
