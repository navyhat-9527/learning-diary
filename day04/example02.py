"""
example02 - 容器型数据类型
            将一筛子投掷60000次,统计每一面出现的次数
Author : wangyiwen03
Date : 2021/12/29
"""
import random
f1, f2, f3, f4, f5, f6 = 0, 0, 0, 0, 0, 0

for i in range(60000):
    toss = random.randrange(1,7)
    if toss == 1:
        f1 += 1
    elif toss == 2:
        f2 += 1
    elif toss == 3:
        f3 += 1
    elif toss == 4:
        f4 += 1
    elif toss == 5:
        f5 += 1
    else:
        f6 += 1

print(f1,f2,f3,f4,f5,f6)