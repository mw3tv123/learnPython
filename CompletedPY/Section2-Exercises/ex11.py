"""
Write a function that sorts a list.
The user should be able to pass a compare function that determines
the order of 2 elements in the list.

Example:
def sort(list, comp):
    # TODO: Place your code here, return sorted list.
    pass

def less(a, b):
    return a < b

def greater(a, b):
    return a > b

l = [1, 2, 9, 8, 5, 6]
print(sort(l, less))
print(sort(l, greater))

ET: 2 hours
"""


def sort(list, comp):
    i = 0
    while i < len(list)-1:
        j = i+1
        while j < len(list):
            if comp(list[i], list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
        i += 1
    return list


def less(a, b):
    return a < b


def greater(a, b):
    return a > b


l = [1, 2, 9, 8, 5, 6]
print(sort(l, less))
print(sort(l, greater))