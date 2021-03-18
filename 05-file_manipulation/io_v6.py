# With: closes the file automatically
with open('people.csv') as myfile:
    with open('people.txt', 'w') as out:
            
        for r in myfile:
            people = r.strip().split(',')
            print('Name: {}, Age: {}'.format(*people), file=out)


if myfile.closed:
    print('closed file')
