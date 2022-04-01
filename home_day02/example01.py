"""
    example01 - while循环
 Author : Iven
 Date : 2021/12/24
"""

# while 条件:
#     print('....')
# # 在不知道循环次数的时候适用于while


# i = 0
# while True:
#     print('hello,world')
#     i += 1
#     if i >= 10:
#      break
#      print('game over!')

# x = int(input('x = '))
# y = int(input('y = '))
#
# while y % x != 0 :
#     temp = x
#     x = y % x
#     y = temp
# print(x)
#
# a = 92913 / 2915
# print(a)

x = int(input('x = '))
y = int(input('y = '))

while y % x != 0:
    x , y = y % x , x #欧几里得公式/辗转相除法
print(x)