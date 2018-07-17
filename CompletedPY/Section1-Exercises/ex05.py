# coding=utf-8
"""
Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng:

    5 == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...

Trả về 1 `list` các `string` có dạng:

    output: ['5 == 1 * 5', '10 == 2 * 5', ...]

Lưu ý: Thứ tự tăng dần theo bảng cửu chương

ET: 30minutes
"""

str_list = []
j = 1
for i in range(1, 101):
    if i % 5 == 0:
        s = "{} == {} * 5".format(i, j)
        print(s)
        j += 1
        str_list.append(s.strip())

print(str_list)
