"""
Example03 -
Author : wangyiwen03
Date : 2021/12/20
"""
# 十进制计数法
a = 110

# 八进制计数法
b = 0o110

# 十六进制计数法
c = 0x110

# 二进制计数法

d = 0b110

#浮点数的科学计数法
e = 123e-3
print(e)
e = 1.23e-3
print(e)

print( a, b, c, d)
# bin ---> binary  十进制转二进制
print(bin(47))

# oct ---> octal 十进制转八进制
print(oct(47))

# hex ---> hexadecimal 十进制转十六进制
print(hex(47))

print(bin(a))
print(hex(a))
print(oct(a))
