"""
homework02 - 向列表中随机添加10个数字, 找出其中第二大的数字
Author : wangyiwen03
Date : 2022/1/13
"""
import random

nums = []

for _ in range(10):
    temp = random.randrange(1, 100)
    nums.append(temp)
print(nums)
max_value = max(nums)
nums.remove(max_value)  # remove 删除指定值的元素
print(max(nums))
