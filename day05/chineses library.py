"""
chineses library -  所有汉字编码
Author : wangyiwen03
Date : 2022/1/27
"""


###汉字编码范围: 0x4e00 ~ 09fa5

#ord()函数 ---> 查看字符对应的编码
#chr()函数 ---> 将编码处理成对应的字符

'''for i in range (0x4e00,0x9fa6):
    print(chr(i),end='')'''

print(hex(ord('王')),hex(ord('艺')),hex(ord('文')))