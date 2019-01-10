# coding=utf-8
"""
a, b, c là các số nguyên dương nhỏ hơn 10, biết a + b/c = 10

In ra list chứa các bộ số thỏa mãn điều kiện trên (a, b, c có thể trùng nhau).

Ví dụ:

- output: [[9, 1, 1], ...]
Lưu ý: kết quả từng list con trả về với a giảm dần, b và c tăng dần

ET: 30 minutes
"""

result = []
for a in reversed(range(1, 10)):
    for b in range(1, 10):
        for c in range(1, 10):
            if a + b/c == 10:
                result.append([a, b, c])
print(result)
