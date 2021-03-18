def day_type(day):
    days = {
        1: 'weekend',
        2: 'weekday',
        3: 'weekday',
        4: 'weekday',
        5: 'weekday',
        6: 'weekday',
        7: 'weekend'
    }
    return days.get(day, 'INVALID')


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {day_type(day)}')
