
myfile = open('people.csv')
data = myfile.read()
myfile.close()

for r in data.splitlines():
    print('Name: {}, Age: {}'.format(*r.split(',')))
