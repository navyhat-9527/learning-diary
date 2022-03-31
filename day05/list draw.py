"""
list draw - 列表抽样
Author : wangyiwen03
Date : 2022/2/24
"""
import random

names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = random.sample(names,5)
# sample无放回随机抽样,没有重复值
print(a)

b = random.choices(names, k=5)
# choices有放回随机抽样,k=n n为抽样次数
print(b)

c = random.choice(names)
# choice随机抽取一个列表中的元素
print(c)

random.shuffle(names)
# 打乱列表顺序
print(names)
