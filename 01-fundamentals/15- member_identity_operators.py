# Member Operator

listx = [1, 2, 3, 5, 'Ana', '*']
print(2 in listx)
print(999 in listx)
print('*' in listx)
print(2 not in listx)

print('\n---')
# Identity Operator

x = 3
y = 2
z = 1

print(x is y)
print(x is 3)
print(10 is not z)

print('\n---')
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]
print(list_a is list_b)
print(list_a is list_c)
