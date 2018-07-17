"""
Write a Python function to create the HTML string with tags around the word(s).
Sample function and result:
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial</b>'

ET: 15 minutes
"""


def add_tag(tag, word):
    return "<{}>{}</{}>".format(tag, word, tag)


print(add_tag("i", "Python"))
print(add_tag("b", "Python Tutorial"))
