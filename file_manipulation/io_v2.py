
myfile = open('people.csv')

for r in myfile:
    print('Name: {}, Age: {}'.format(*r.split(',')),end='')

myfile.close()