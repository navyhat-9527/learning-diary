"""
tuple - 元组的应用
pack / unpack
Author : wangyiwen03
Date : 2022/2/27
"""
import random

scores = [random.randrange(0, 101) for _ in range(10)]
# a,  b =  1, 2, 3  #ValueError: too many values to unpack(解包:把一个元组拆成多个元素) (expected 2)
# a, b, c = 1 ,2 #ValueError: not enough values to unpack (expected 3, got 2)
scores.sort()
a, *b, c = scores

print(a)
print(b)
print(c)  # 列表
