import math

print(type(1))
print(type('1'))

print(__builtins__.type('testing'))
# __builtins__.print(1)
a = 10 / 2
print(a)
print(dir())  # present in the global scope of the application
print(dir(__builtins__))

name = 'John Wick'
print(__builtins__.len(name))
