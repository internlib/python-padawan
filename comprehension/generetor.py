# Consumes less memory
generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))

for number  in generator:
    print(number)