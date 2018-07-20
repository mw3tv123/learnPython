"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
ET 30p
"""


def string_processor(string):
    letter = digit = 0
    for char in string:
        if char.isdigit():
            digit += 1
        elif char.isalpha():
            letter += 1
    return letter, digit


if __name__ == "__main__":
    # string = input(">>> Enter your string: ")
    test_case1 = "hello world! 123"  # 10 ; 3
    test_case2 = "100 miles with 5 cars"  # 13 ; 4
    test_case3 = "five men/ 2 boats"  # 12 ; 1
    tc1_letters, tc1_digits = string_processor(test_case1)
    tc2_letters, tc2_digits = string_processor(test_case2)
    tc3_letters, tc3_digits = string_processor(test_case3)
    print("LETTERS {}\nDIGITS {}".format(tc1_letters, tc1_digits))
    print("LETTERS {}\nDIGITS {}".format(tc2_letters, tc2_digits))
    print("LETTERS {}\nDIGITS {}".format(tc3_letters, tc3_digits))
