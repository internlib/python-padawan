#!/usr/bin/python3.8

# import math OBS: use math.pi
from math import pi

#pi = 3.14159


def circle(radius):
    print("circle area = ", pi * float(radius) ** 2)


if __name__ == '__main__':
    radius = input('Enter the radius value: ')
    circle(radius)

# >>> import circle_area_import_module_func_v7
# >>> circle_area_import_module_func_v7.circle(11.222)


# >>> from circle_area_import_module_func_v7 import circle
# >>> circle(12.2)
