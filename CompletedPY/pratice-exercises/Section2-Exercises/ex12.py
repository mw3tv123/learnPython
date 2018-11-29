"""
Write a function that can measure the execution time of a function
(with any number of arguments).

ET: 2 hours
"""
import time


def speed_check(func):
    def timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        string = "----- Function {}'s execution time is {:4f}s -----"\
            .format(func.__name__, end - start)
        return string
    return timer


@speed_check
def test():
    for i in range(2000000):
        pass


print(test())