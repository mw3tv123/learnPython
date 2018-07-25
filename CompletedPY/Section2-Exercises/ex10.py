# -*- coding: <utf-8> -*-
"""
Viết chương trình nhận thông tin của các học sinh
(tên, điểm trung bình, id)
In danh sách các học sinh có điểm trung bình từ cao tới thấp
Nếu bằng điểm thì sắp xếp theo tên

ET 2hours
"""
from operator import itemgetter
data = input(">>> Enter the list: ")
data = data.split(' ')
i = 0
for element in data:
    data[i] = tuple(element.split(','))
    i += 1
data.sort(key=itemgetter(1), reverse=True)
print(data)