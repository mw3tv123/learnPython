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
    return lines[0].count(lines[1])


input_data = input(">>>Enter your string (use space to split substring adn origin string): ")
print(count_string(input_data))
