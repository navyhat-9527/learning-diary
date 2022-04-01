"""
    homework01 - 找出100-999中的水仙花数(各位数的立方和刚好等于这个数本身)
    ex: 153 = 1^3 + 5^3 + 3^3
 Author : Iven
 Date : 2021/12/24
"""

# a = i % 100
# b = i - a % 10
# c = i - 100 * a - 10 * b

# for i in range(100, 1000):
#     a = i // 100
#     b = (i - a * 100) // 10
#     c = i % 10
#     if i == a * a * a + b * b * b + c * c * c:
#         print(i)

# for i in range(100, 1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if i == a ** 3 + b **3 + c ** 3:
#         print(i)
#     12// 10 = 1 1 % 10 = 1

# x = int(input('x = '))
# i = 10
# total = 0
# while x // 10 > 0 or 0< x < 10:
#     temp2 = x % 10
#     y = x // 10
#     total = total*10 + temp2
#     x = y
# print(total)

x = int(input('x = '))
total = 0
while x > 0 :
    total = total * 10 + x % 10
    x = x // 10

print(total)