a = '123'
b = '456'
print(a + b)

# Using builtins calling

print(a.__add__(b))
print(str.__add__(a, b))
print(a.__len__())
print(a.__contains__('1'))
