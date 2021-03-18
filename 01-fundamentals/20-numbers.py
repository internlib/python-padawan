from decimal import Decimal, getcontext

a = 1.1 + 2.2
print(a)

getcontext().prec = 4
b = Decimal(1) / Decimal(7)  # four precision houses
print(b)

getcontext().prec = 10
b = Decimal(1) / Decimal(7)  # four precision houses
print(b)

print(dir(Decimal))  # Allowed options
