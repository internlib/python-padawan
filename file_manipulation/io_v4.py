
try:
    myfile = open('people.csv')

    for r in myfile:
        print('Name: {}, Age: {}'.format(*r.strip().split(',')))
except IndexError:
    pass
finally:
    print('finally')
    myfile.close()

if myfile.closed:
    print('closed file')
