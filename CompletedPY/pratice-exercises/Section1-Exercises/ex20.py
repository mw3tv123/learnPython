"""
Write a program that swaps the keys and values of a dictionary.

Input:
{
    "a" : 1,
    "b" : 1,
    "c" : 2,
    "d" : 3
}

Output:
{
    1: ["a", "b"],
    2: ["c"],
    3: ["d"]
}

ET: 15 minutes
"""
input_dict = {'a': 1, 'b': 1, 'c': 2, 'd': 3}
output_dict = {key: value for value, key in input_dict.items()}
print(output_dict)
