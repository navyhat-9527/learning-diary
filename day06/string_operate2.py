"""
string_operate2 -  字符串的拆分和合并
Author : wangyiwen03
Date : 2022/3/4
"""

content = 'You go your way, i will go mine.'
content2 = content.replace(',', '').replace('.', '')
words = content2.split()
print(type(words))
for word in words:
    print(word)

items = content.split(',')
for item in items:
    print(item)

contents = ['风抓不住我',
            '云找不到我',
            '只有你知道',
            '何处是我'
            ]

print('-'.join(contents))
