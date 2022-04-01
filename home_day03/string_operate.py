"""
    string_operate - 字符串的操作
 Author : Iven
 Date : 2022/3/2
"""

a = 'hello world'

print(a.upper())  # 全大写
print(a.lower())  # 全小写
print(a.capitalize())  # 首字母大写
print(a.title())  # 单词首字母大写

b = 'abc123'
print(b.isdigit())
print(b.isalpha())
print(b.isascii())
print(b.startswith('a'))
print(b.endswith('5'))
