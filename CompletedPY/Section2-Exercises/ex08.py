"""
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3?
Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
ET 30 minutes
"""
import collections
data = input(">>> Enter your string:")
data = data.split(' ')
word_list = {}
for word in data:
    if word not in word_list:
        word_list[word] = 1
    else:
        word_list[word] += 1
word_list = collections.OrderedDict(sorted(word_list.items()))
for k, v in word_list.items():
    print("{}:{}".format(k, v))