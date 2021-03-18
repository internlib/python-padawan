#!/usr/bin/python3.8

# ARGS
from math import pi
import sys
import errno
#pi = 3.14159

ERROR_COLOR = '\033[91m'
NORMAL = '\033[0m'


def circle(radius):
    return pi * float(radius) ** 2


def help():
    print("{} <value>".format(sys.argv[0]))


if __name__ == '__main__':
    # print(sys.argv[0])
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)  # PARAMNS

    if not sys.argv[1].isnumeric():
        print(ERROR_COLOR, 'parameter is not numeric', NORMAL)
        help()
        sys.exit(errno.EINVAL)  # INVALID

    radius = sys.argv[1]
    area = circle(radius)
    print(area)

# >>> import circle_area_import_module_func_v8 as v8
# >>> v8.circle(10)
# 314.1592653589793
