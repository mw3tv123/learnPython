# coding=utf-8
"""
Trả về tiêu đề bài thơ ghép từ các chữ cái đầu tiên của mỗi dòng.
Chỉ viết hoa chữ cái đầu tiên.
OUTPUT: Crossmyheart

ET: 30 minutes
"""

data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''

# https://www.poetrysoup.com/poem/cross_my_heart_609765

result = ""
temp = data.strip().splitlines()
for line in temp:
    result += line[0]
print(result.title())
