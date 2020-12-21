
# 0 , 1, 1, 2, 3, 5, 8, 13 ..
import time


def fibonacci(amount):
    result = [0, 1]
    while True:
        result.append(sum(result[-2:]))
        if len(result) == amount:
            break
    return result


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
