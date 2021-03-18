import csv

with open('people.csv') as inputfile:
    for people in csv.reader(inputfile):
        print('Name: {}, Age: {}'.format(*people))
