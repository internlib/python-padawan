def sum_numbers(*numbers):
    print(type(numbers))  # packing
    sum = 0
    for n in numbers:
        sum += n
    return sum


def sum_3(n1, n2, n3):
    return n1 + n2 + n3


if __name__ == '__main__':
    print(sum_numbers(1, 1, 1, 100))

    # unpacking
    nums = (1, 2, 3)
    print(sum_3(*nums))
    # unpacking
    list_nums = [5, 5, 5]
    print(sum_3(*list_nums))
