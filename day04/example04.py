"""
example04 - 容器型数据类型
            将一筛子投掷60000次,统计每一面出现的次数
Author : wangyiwen03
Date : 2022/1/5
"""
import random

count = [0, 0, 0, 0, 0, 0]

for _ in range (60000):
    face = random.randrange(1,7)
    count[face-1] += 1
