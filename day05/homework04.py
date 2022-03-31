"""
homework05 - 21根火柴游戏: 有21根火柴,人和计算机轮流拿,人先拿(输入拿几根)计算机后拿,
                每次至少1根至多4根,拿到最后一根火柴的算输,要确保计算机一定可以获胜
Author : wangyiwen03
Date : 2022/1/15
"""
import random

nums = [1 for i in range(21)]
print(list)

i = 1
while True:
    take_man = int(input(f"第{i}次请你取出1-4根火柴:"))
    nums.pop()*take_man
    take_robot = int(input(f'电脑'))