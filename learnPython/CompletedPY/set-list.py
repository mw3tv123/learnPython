import random
a = random.sample(range(100), 30)
b = random.sample(range(90), 40)

new_list = [x for x in a if x in b]

print list(set(new_list))
print(a)
print(b)
