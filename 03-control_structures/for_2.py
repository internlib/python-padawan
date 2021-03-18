word = 'python3'
for letter in word:
    print(letter)

print('\n')

word = 'python3'
for letter in word:
    print(letter, end='*')

print('\n')

word = 'python3'
for letter in word:
    print(letter, end='')

print('\n')

approved = ['John', 'Maria', 'Tereza', 'Ana']
for name in approved:
    print(name)

print('\n')

for position, name in enumerate(approved):
    print(position + 1, name)

print('\n')

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday')

for position, day in enumerate(days_of_the_week):
    print(position + 1, day)

print('\n')

for letter in set('Brazil'):
    print(letter)
