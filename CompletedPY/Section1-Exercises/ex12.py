"""
Ta có 1 list gồm 100 số  trong khoảng 1-99 trong đó có 1 số lặp lại 2 lần.
Tìm số đó.

ET: 30 minutes
"""

import random

data = []
for i in range(100):
    data.append(random.randint(1, 100))

temp = 0
for i in data:
    j = i + 1
    while j < len(data):
        if data[i] == data[j]:
            temp += 1
        if temp == 2:
            print(data[i])
            break
        j += 1
    i += 1
