#!/usr/bin/python3.8

# ARGS
from math import pi
import sys
#pi = 3.14159


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    # print(sys.argv[0])
    print("{} <value>".format(sys.argv[0]))
    if len(sys.argv) < 2:
        print("Missing values")
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print(area)

# >>> import circle_area_import_module_func_v8 as v8
# >>> v8.circle(10)
# 314.1592653589793
