people = {'name': 'Ana', 'courses': ['course1', 'course2']}
print(people)
print(type(people))
print(len(people))  # two key: value
print(people['courses'])
print(people['name'])


print('\n---')
variable = 'testing'
test = {'value': variable}
print(type(test))
print(test)

print(test.keys())
print(test.values())
print(test.items())
print(test.get('value'))
