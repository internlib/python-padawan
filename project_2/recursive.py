def printx(max, current):
    if current > max:
        return
    print(current)
    printx(max, current + 1)


printx(10, 1)
