for i in range(1, 11):
    print('i = {}'.format(i))

for j in range(10):
    print('j = {}'.format(j))


for j in range(10):
    for i in range(1, 11):
        print(f'{j} * {i} = {j * i}')
