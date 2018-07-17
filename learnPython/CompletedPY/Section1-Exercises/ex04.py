# coding=utf-8
"""
Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:
- input_data: 2
- output: February 28

ET: 30 minutes
"""

import calendar

usr_num = 0
while True:
    usr_num = int(input(">>>Enter your number: "))
    if usr_num < 1 or usr_num > 12:
        continue
    date_string = calendar.month_name[usr_num] + " " + str(calendar.monthrange(2018, usr_num)[1])
    break

print(date_string)
