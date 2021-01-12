# object can behave as a function

class Potency:
    # cacl potency
    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, base):
        return base ** self.exponent


if __name__ == '__main__':
    squared = Potency(2)
    cube = Potency(3)
    if callable(squared) and callable(cube):
        print(f'3^2 => {squared(2)}')
        print(f'3^5 => {cube(5)}')

    print(Potency(2)(4))
