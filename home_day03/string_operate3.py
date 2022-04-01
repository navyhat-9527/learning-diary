"""
    string_operate3 - 字符串的操作

编码: 把字符串编写成字节  str---> encode()---->byte
解码: 将字节还原成字符串  byte---> decode()---->str

了解:
    1. 什么是'百分号编码'
    2. 什么是'BASE64编码'

重点:
    1. 选择字符集时(编码)的时候,最佳的选择是UTF-8编码
    2. 编码和解码选择的字符集要保持一致,否则会出现乱码或报错现象\
    3. 不能使用ISO-8859-1 保存中文字符,否则会出现编码黑洞, 中文变成?
    4. UTF-8是Unicode的一种实现方案,也是一种变长编码
       最少1个字节,最多4个字节(emoji),中文是3个字节,英文是1个字节
 Author : Iven
 Date : 2022/3/7
"""
#
# a = '我爱你中国'
# # GBK <---- GB2312 <---- ASCII
# b = a.encode('gbk')
# print(type(b))
# print(b, len(b))
# c = b'\xce\xd2\xb0\xae\xc4\xe3\xd6\xd0\xb9\xfa'
# print(c.decode('gbk'))

a = '我爱你中国'
# UTF-8编码是Unicode(万国码)的一种实现方案
b = a.encode('utf-8')
print(type(b))
print(b, len(b))
# 如果编码和解码的方式不一致, python中通常会产生UnicodeDecodeError
# 也有可能会出现乱码现象
print(b.decode('utf-8'))


# 编码黑洞----中文编程问号 无法还原解码
# a = '我爱你中国'
# b = a.encode('iso-8859-1')
# print(b, len(b))

