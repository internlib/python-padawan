def sum(a, b):
    def sum_c(c):
        return a + b + c
    return sum_c


sum5 = sum(2, 3)
print(sum5(5))

print(sum(1, 2)(5))
