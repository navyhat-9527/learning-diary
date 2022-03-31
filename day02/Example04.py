"""
Example04 -
Author : wangyiwen03
Date : 2021/12/20
"""

a1 = float(input('a1 = '))
b2 = float(input('b2 = '))

print(a1 + b2)
print(a1 - b2)
print(a1 * b2)
print(a1 / b2)
print(a1 // b2)
print(a1 % b2)

# 占位符的使用 %f , 保留小数位数
print('%f + %f = %f' % (a1, b2, a1 + b2))
print('%.1f +%.2f = %.3f ' % (a1, b2, a1 + b2))
# 当占位符参与模的运算时的表达
print('%f %% %f = %0.f' %(a1 ,b2 ,a1 % b2))


