def all_params(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    all_params('a', 'b', 'c')
    all_params(1, 2, 3, x=True, value=12.11)
    all_params('Ana', False, [1, 2, 3], size='M', exist=True)
    
    # all_params(first='John', 'Marie') # ERROR
    all_params('Marie', first='John')
