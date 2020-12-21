for x in range(1, 11):
    if x % 2 == 0:
        print(x, '= pair')
        continue

for x in range(1, 11):
    if x % 2 == 0:
        print(x, 'pair, by')
        break  # leaves the repeat section
