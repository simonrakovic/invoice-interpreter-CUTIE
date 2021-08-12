import unicodedata

import numpy as np

bbox = [
    893,
    988,
    925,
    1001
]

bbox2 = [
1099.52001953125,
                224.22000122070312,
                1152.7976000236742,
                258.04998779296875
]

positions = np.array(bbox).reshape([-1])
x_left = max(0, min(positions[0::2]))

x_right = max(positions[0::2])
y_top = max(0, min(positions[1::2]))
y_bottom = max(positions[1::2])
w = x_right - x_left
h = y_bottom - y_top


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


"""
three cases covered: 
alphabetic string, numeric string, special character
"""



