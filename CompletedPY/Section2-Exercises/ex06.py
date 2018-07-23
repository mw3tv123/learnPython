"""
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
ET 1h
"""


class Generator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index = self.index + 1
        if self.data[self.index] % 7 == 0:
            return self.data[self.index]


num_list = [x for x in range(10)]
gen = Generator(num_list)
for char in gen:
    print(char)
