"""
Write a decorator which wraps functions to log function arguments and
the return value on each call.
Provide support for both positional and named arguments
(your wrapper function should take both
*args
and
**kwargs
and print them both):
>>> @logged
... def func(*args):
...     return 3 + len(args)
>>> func(4, 4, 4)
you called func(4, 4, 4)
it returned 6
6
ET 2 hours
"""


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        string = "You called {}\nIt return {}"\
            .format(original_function.__name__, original_function(*args))
        return string
    return wrapper_function


@decorator_function
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))