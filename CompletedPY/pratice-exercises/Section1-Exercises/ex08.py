"""
What is the sum of the digits of the number `2**1000`?
https://projecteuler.net/problem=16

Must: use list comprehension
Tips: list comprehension always create new list

ET: 30 minutes
"""

result = [int(x) for x in str(2**1000)]
print(sum(result))
