"""
    example02 - 列表的遍历(依次从列表中取出)
 Author : Iven
 Date : 2022/1/5
"""

nums = [1, 2, 3, 4, 5]

# print(nums[0], [-5])
# print(nums[1], [-4])
# nums.append(6)
# nums[2] = 10
#
# print(nums)
#
# # for i in range(5):
# #     print(num[i])  # 如果期间增加或减少列表中的元素,则会出现无法遍历列表的情况
#
# for i in range(len(nums)):  # len(list_name)计算列表元素
#     print(nums[i])
#     nums[i] = 100
#
# print(nums)

for i,num in enumerate(nums):   #enumerate 列举,枚举
    print(i,num)  #对列表只做读操作