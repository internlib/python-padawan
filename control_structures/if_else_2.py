def age_range(age):
    if 0 <= age < 18:
        return 1
    elif age in range(18, 50):
        return 2
    elif age in range(51, 100):
        return 3
    else:
        return 4


# print(age_range(98))

for age in (17, 12, 21, 1, 101, 98, 12):
    print(age_range(age))
