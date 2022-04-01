"""
    string_cal2 - 字符串的索引和切片
 Author : Iven
 Date : 2022/3/2
"""
import os
import time

# a = 'hello, world!'
# print(a [0], a[-2], a[-len(a)])
#
# print(a[len(a)-1])
#
# print(a[2:5])
# print(a[1:10:3])
# print(a[::-1])


# exercise: 跑马灯文字效果

content = '拼搏到无能为力, 坚持到感动自己         '

while True:
    os.system('cls')
    print(content)
    time.sleep(0.1)
    content = content[1:] + content[0]
