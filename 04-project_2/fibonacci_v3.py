
# 0 , 1, 1, 2, 3, 5, 8, 13 ..
import time


def fibonacci(limite):
    before_the_last = 0
    last = 1
    print(f'{before_the_last}, {last}', end=',')
    while last < limite:
        before_the_last, last = last, before_the_last + last
        print(last, end=',')
        # time.sleep(1)


fibonacci(1000)
