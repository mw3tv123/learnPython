
# coding=utf-8
"""
Kiểm tra text có phải là palindrome không.
Kiểm tra text có phải là palindrome không.

Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
String phải dài hơn 1 chữ cái.
Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

:rtype: bool

ET: 30 minutes
"""


def isPalindrome(s):
    return s == s[::-1]


str_data = input(">>>Enter your string: ")
if isPalindrome(str_data.lower()):
    print("Your string is Palindrome!")
else:
    print("Your string is NOT Palindrome!")
