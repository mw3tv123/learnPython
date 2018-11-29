"""
Write a Python program of recursion list sum.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21

ET: 1 hour
"""


def recursion_list_sum(data):
    list_sum = 0
    for ele in data:
        if isinstance(ele, type([])):
            list_sum += recursion_list_sum(ele)
        else:
            list_sum += ele
    return list_sum


data_list = [1, 2, [3, 4], [5, 6]]
print(recursion_list_sum(data_list))
