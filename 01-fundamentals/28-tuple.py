# It is not possible to change the tuple
t = tuple()  # immutable sequence
print(dir(tuple))
t = ('one')
print(type(t))  # str
t = ('one',)
print(type(t))  # tuple
# t[0] = 'two'
print(t)

x = ('red', 'blue', 'yellow', 'red')
print(x)
print(x.count('red'))
print(x[-1])  # Last element
