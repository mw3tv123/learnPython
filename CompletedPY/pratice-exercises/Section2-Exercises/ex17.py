"""
Write a function that yields the value of every iteration of computing
the square root of a number using Newton's method
(https://en.wikipedia.org/wiki/Newton%27s_method).

NOTE: The number of iterations is provided by user.

Example:
def compute(number, iterations):
    # TODO: Put your code here.
    pass

for v in compute(612, 3):
    print(v)

# 35.6
# 26.395505617978
# 24.790635492455

ET: 1 hour
"""


def newton_method(n):
    approximate_number = n * 0.5
    result = 0.5 * (approximate_number + n/approximate_number)
    while result != approximate_number:
        approximate_number = result
        result = 0.5 * (approximate_number + n/approximate_number)
    return result


print(newton_method(4.84))