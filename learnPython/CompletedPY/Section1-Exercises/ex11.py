"""
Write a Python program to solve the Fibonacci sequence using recursion.

ET: 30 minutes
"""


def gen_fibonaci(fib):
    if fib <= 1:
        return fib
    else:
        return gen_fibonaci(fib - 1) + gen_fibonaci(fib - 2)


data = int(input(">>>Enter your limit: "))
for i in range(data):
    print(gen_fibonaci(i))
