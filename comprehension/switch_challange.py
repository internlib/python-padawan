def which_day(day):
    days = {
        (1, 7): 'weekend',
        tuple(range(2, 7)): 'weekday'
    }
    chosen_day = (t for numbers, t in days.items() if day in numbers)
    return next(chosen_day, '**invalid**')


if __name__ == '__main__':
    for day in range(0,9):
        print(f'{day}: {which_day(day)}')