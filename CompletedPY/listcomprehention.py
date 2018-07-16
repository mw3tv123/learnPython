import random

a = random.sample(range(0,30), 12)
b = random.sample(range(0,30), 15)

result = [i for i in a if i in b]
print a
print b
print result
