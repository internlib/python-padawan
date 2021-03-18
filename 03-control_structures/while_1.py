from random import randint
import sys

number = 8

while True:
    secret_number = randint(0, 9)
    if number == secret_number:
        print('found, number =', secret_number)
        sys.exit(1)
    else:
        print('not found')
