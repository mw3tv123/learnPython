"""
Ta có 1 list gồm 100 số  trong khoảng 1-99 trong đó có 1 số lặp lại 2 lần.
Tìm số đó.

ET: 30 minutes
"""

import random

data = []
for i in range(100):
    data.append(random.randint(1, 100))
data.sort()
for i in data:
    if data.count(i) >= 2:
        print(i, end=" ")
