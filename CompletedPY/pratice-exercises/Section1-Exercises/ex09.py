"""
Input Format
The first line of input contains the original string. The next line contains the substring.
Each character in the string is an ascii character.

Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
ABCDCDC
CDC

Sample Output
2

ET: 30 minutes
"""


def count_string(data=""):
    lines = data.split(" ")
    l1 = len(lines[0])
    l2 = len(lines[1])
    count = temp = 0
    for i in range(l1):
        if l1 - i < l2:
            break
        for j in range(l2):
            if lines[0][i+j] == lines[1][j]:
                temp += 1
        if temp == l2:
            count += 1
        temp = 0
    return count


input_data = input(">>>Enter your string (use space to split substring adn origin string): ")
print(count_string(input_data))
