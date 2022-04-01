"""
    list draw - 列表抽样
 Author : Iven
 Date : 2022/2/25
"""
import random

names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(len(names))

print(random.sample(names, 5))  # sample无放回抽样
print(random.choices(names, k=5))  # choice有放回抽样
print(random.choice(names))  # choice从列表中随意抽取一个元素

random.shuffle(names) # random.shuffle使列表随机乱序
print(names)
