def concept_note(value):
    note = float(value)

    if note > 10:
        return 'invalid'
    elif note >= 9.1:
        return 'A'
    elif note >= 8.1:
        return 'B'
    elif note >= 7.1:
        return 'C'
    elif note >= 6.1:
        return 'D'
    elif note >= 5.1:
        return 'E'
    elif note >= 4.1:
        return 'F'
    elif note >= 3.1:
        return 'G'
    else:
        return '0'


print(concept_note(4))
