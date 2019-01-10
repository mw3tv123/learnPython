"""
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
ET 30m
"""


def sum_number(number):
    data = []
    for i in range(0, 4):
        element = str(number)*(i+1)
        data.append(int(element))
    return sum(data)


if __name__ == "__main__":
    number = int(input(">>>Enter your number: "))
    print(sum_number(number))
