"""
    string_cal - 字符串的计算
 Author : Iven
 Date : 2022/3/2
"""

a = 'hello, world!'

print(a * 5)  # 字符串的重复运算
print('or' in a)  # 字符串的成员运算
print('ko' in a)

# 字符串的比较运算,  **比较字符串的内容**
b = 'hello, World!'
print(a == b)
print(a != b)

c = 'goodbye, world!'
print(b > c)

d = 'hello, everybody!'
print(b >= d)  # Flase 大写字母在小写字母之前

print(ord('W'), ord('e'))

## 索引和切片

print(len(a))

for i in a:
    print(i, end=' ')

for i in range(len(a)):
    print(a[i])


# **字符串类型只能进行读操作,不能进行写入
# a[i] = H 不可行

