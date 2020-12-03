from string import Template

name, age, weight = 'Ana', 30, 55.2231
print('Name: %s Age: %d Weight: %.2f' % (name, age, weight))
print('Name: {0} Age: {1}'
      .format(name, age))

# print(f'Name: {name} Age: {weight}')
s = Template('Name: $name Age: $age')
print(s.substitute(name=name, age=age))

# f-string
bags = 3
apples_in_bag = 12
print(f'There are total of {bags * apples_in_bag} apples')
