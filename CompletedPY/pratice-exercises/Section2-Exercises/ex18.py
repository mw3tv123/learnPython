"""
Write a program that generates a random string.
The program will ask user the length of string.
After 5 seconds, if user doesn't provide the length use the
default value of 10.

ET: 1 hour
"""
import random
import string
from threading import Timer


def gen_string(length):
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(int(length)))
    print("\nThe random string is {}".format(random_string))


def time_out():
    gen_string()


def validate_input():
    while True:
        timer = Timer(5.0)
        timer.start()
        length = input(">>> Enter the lenght of the string: ")
        timer.stop()
        if length.isdigit():
            break
    return length


def main():
    length = validate_input()
    gen_string(length)


if __name__ == "__main__":
    main()