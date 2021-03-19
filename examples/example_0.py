# -*- coding: utf-8 -*-

"""Example 0 (no style, no lint, no documentation).

First version of the example code (slide 10a), prior to applying any tool.
"""


def Calculate(A, B= {}, print = True):
    if A == None:
        if print:
                print('error: A is not valid')
        return


    elif A != None:
        if print:
                print('calculating ...', \
                      "Using ", A)
    C = {}
    C['orig'] = A
    #C['comp'] = A*2??????
    C['comp'] = A *3.21868
    return C
