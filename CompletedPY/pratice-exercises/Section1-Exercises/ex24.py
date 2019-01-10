"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
ET 30m
"""


def string_processor(string):
    upper = lower = 0
    for char in string:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
    return upper, lower


if __name__ == "__main__":
    # string = input(">>> Enter your string: ")
    test_case1 = "Hello world!"  # 1 ; 9
    test_case2 = "Lavender flower SO BEAUTIFUL!"  # 12 ; 13
    test_case3 = "CAR truck"  # 3 ; 5
    tc1_uppers, tc1_lowers = string_processor(test_case1)
    tc2_uppers, tc2_lowers = string_processor(test_case2)
    tc3_uppers, tc3_lowers = string_processor(test_case3)
    print("UPPER CASE {}\nLOWER CASE {}".format(tc1_uppers, tc1_lowers))
    print("UPPER CASE {}\nLOWER CASE {}".format(tc2_uppers, tc2_lowers))
    print("UPPER CASE {}\nLOWER CASE {}".format(tc3_uppers, tc3_lowers))
