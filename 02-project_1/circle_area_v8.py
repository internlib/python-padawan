#!/usr/bin/python3.8

# import math OBS: use math.pi
from math import pi

#pi = 3.14159


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    radius = input('Enter the radius value: ')
    area = circle(radius)
    print(area)

# >>> import circle_area_import_module_func_v8 as v8
# >>> v8.circle(10)
# 314.1592653589793
