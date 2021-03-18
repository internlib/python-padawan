d = {'name': 'Albert', 'number': 43,
     'class': 'TXX11', 'courses': ['python', 'go']}
print(d)
d['number'] = 101
print(d)
d['courses'].append('angular')
print(d)
d.pop('number')  # Deletes field
print(d)
del d['courses']
print(d)  # Deletes courses
