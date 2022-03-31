"""
homework01 - 输入三个数按从大到小的顺序输出
Author : wangyiwen03
Date : 2022/1/12
"""
# [1,10,20,30] 5
nums = [1,2,3]

for _ in range(3):
    temp = int(input('输入数据:'))
    i = 1
    for num in nums:
        if num > temp:
            nums.append(i-1, temp)
            break
        elif num < temp and len(nums) < i:
            i += 1
        else:
            nums.append(-1,temp)
            break
print(nums)
