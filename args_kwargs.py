def func(*args, **kwargs):
    print(args)    # Tuple of positional arguments
    print(kwargs)  # Dictionary of keyword arguments

func(1, 2, 3, a=4, b=5)

'''
outpu:
(1,2,3)
{a:4,b:5}
'''