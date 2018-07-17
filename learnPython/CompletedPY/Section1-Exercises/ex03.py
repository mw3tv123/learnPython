# coding=utf-8
"""
Find common elements of two given lists.

Returns a list contains those elements.
Require: use only lists, if/else and for loops.

ET: 15 minutes
"""

data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)
result = [x for x in data[0] if x in data[1]]

print(result)
