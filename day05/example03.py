"""
example03 - 排序

简单选择排序 - 每次从剩下的元素中选择最小的
Author : wangyiwen03
Date : 2022/1/28
"""

nums = [35, 12, 99, 58, 42, 49, 31, 73]

for i in range(len(nums)):
    min_value = nums[i]
    min_index = i  # 假设每次剩下的第一个为最小值与位子
    for j in range(i + 1, len(nums)):
        if nums[j] < min_value:
            min_index, min_value = j, nums[j]  # 如果当前元素大于之前记录的最小值,则记录该值和所在列表的索引
    nums[i], nums[min_index] = nums[min_index], nums[i]  # 交换剩下列表中第i位与所得最小值的值与索引j

print(nums)

# sorted_nums=[]
# while len(nums)>0:
#     sorted_nums.append(min(nums))
#     nums.remove(min(nums))
# print(sorted_nums)
