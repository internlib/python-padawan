def run(func):
    func()


def good_morning():
    print('Good Morning !')


def good_afternoon():
    print('Good Afternoon !')


if __name__ == '__main__':
    run(good_morning)
    run(good_afternoon)
    # run(1)
