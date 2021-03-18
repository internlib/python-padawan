# With: closes the file automatically
with open('people.csv') as myfile:

    for r in myfile:
        print('Name: {}, Age: {}'.format(*r.strip().split(',')))


if myfile.closed:
    print('closed file')
