"""
Write a Python program to swap comma and dot in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"

ET: 30 minutes
"""


string = "32.054,23"
maketrans = string.maketrans
string = string.translate(maketrans(",.", ".,"))
print(string)
