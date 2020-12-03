# Does not guarantee insertion order
# Does not accept repetition
# Not indexed

a = {1, 2, 3}
print(type(a))
a = set('course')
print(a)

print('3' in a)
print(3 in a)
print('c' in a)

print('\n---')
print({1, 2, 3} == {1, 3, 2, 2, 3, 1, 4})

a = {1, 2, 3, 4}
b = {1, 2, 3, 4, 5, 6}
print(a.union(b))
print(a.intersection(b))

print('\n---')
a.update(b)
print(a)  # Changed the value of the set (union)

print(a <= b)
