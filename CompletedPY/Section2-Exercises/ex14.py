"""
Write a program to open a text file and count the number of occurrences
for every word.
Print out the 5 second most used words and 5 second least used words.

NOTE: The file name is passed by user.
BONUS: Can you write this program without sorting the whole list?

ET: 2 hours
"""
import os
from operator import itemgetter
from collections import OrderedDict


def get_file_path():
    while True:
        path = input(">>> Enter file path: ")
        if os.path.exists(path):
            return path
        else:
            print("!!! WRONG FILE PATH ! TYPE AGAIN !!!")


def process_word_list(path):
    words_list = {}
    with open(path, 'r') as file:
        for line in file.readlines():
            line = line.lower().strip().split(' ')
            for word in line:
                if word not in words_list:
                    words_list[word] = 1
                else:
                    words_list[word] += 1
    return words_list


def print_top_5(words_list):
    words_list = OrderedDict(sorted(words_list.items(), key=itemgetter(1)))
    print("\t===== Top 5 most used =====")
    i = 0
    for index, value in words_list.items():
        if i == 5:
            break
        else:
            print("\t\t\t{:<4}:{}".format(index, value))
            i += 1
    words_list = OrderedDict(sorted(words_list.items(), key=itemgetter(1), reverse=True))
    print("\n\t===== Top 5 most used =====")
    i = 0
    for index, value in words_list.items():
        if i == 5:
            break
        else:
            print("\t\t\t{:<5}:{}".format(index, value))
            i += 1


def main():
    path = get_file_path()
    result_list = process_word_list(path)
    print_top_5(result_list)


if __name__ == "__main__":
    main()