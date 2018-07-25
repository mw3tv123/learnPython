"""
Write a program to open a text file and count the number of occurrences
for every word.
Print out the 5 second most used words and 5 second least used words.

NOTE: The file name is passed by user.
BONUS: Can you write this program without sorting the whole list?

ET: 2 hours
"""
file = open(input(">>> Enter file path: "))
words = {}
with line in file:
    line = line.split(' ')
    for index, value in line:
        if value not in words:
            words[index] = value
        else:
            words[index] = value + 1
