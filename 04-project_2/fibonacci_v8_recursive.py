def fibonacci(amount, sequence=(0, 1)):
    # stop condition
    if len(sequence) == amount:
        return sequence
    return fibonacci(amount, sequence + (sum(sequence[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
