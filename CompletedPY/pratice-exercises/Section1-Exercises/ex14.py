"""
Write a python program to count repeated characters in a string. Go to the editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2

ET: 30 minutes
"""


data = "thequickbrownfoxjumpsoverthelazydog"
char_list = {}
for c in data:
    if c not in char_list:
        char_list[c] = 1
    else:
        char_list[c] = char_list.get(c) + 1
for pairs in char_list:
    if char_list.get(pairs) >= 2:
        print(pairs, char_list[pairs])
