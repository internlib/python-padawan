
myfile = open('people.csv')

for r in myfile:
    print('Name: {}, Age: {}'.format(*r.strip().split(',')))
    

myfile.close()