"""
homework03 - 向列表中随机添加10个数字,找出其中第二大的数字
Author : wangyiwen03
Date : 2022/1/14
"""
import random

nums = []

# for _ in range(10):
#     temp = random.randrange(1, 100)
#     nums.append(temp)

nums = [random.randrange(1,100) for _ in range(10)] #列表的生成式语法(推导式)
print(nums)

m1, m2 = nums[0], nums[1]
if m1 < m2:
    m1, m2 = m2, m1

for i in range(2, 10):
    if m1 < nums[i]:
        m1, m2 = nums[i], m1
    elif m1 == nums[i]:
        pass
    elif m2 < nums[i]:
        m2 = nums[i]

print(m1, m2)
