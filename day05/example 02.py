"""
exmaple 02 - 列表的反转和排序
Author : wangyiwen03
Date : 2022/1/27
"""
items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple']
print(items[::-1])  # 创建了一个新列表进行打印,没有改变原列表
print(items)
items = items[::-1]

# 反转
items.reverse()
print(items)
# 排序 (可以修改reverse参数控制排升序还是排降序如,items.sort(reverse=True))
items.sort(reverse=False)
print(items)

nums = ['1', '10', '234', '2', '35', '100']
nums.sort(key=int)  # sort(self, key(按什么方式排序), reverse)
print(nums)
# nums2= [int(num) for num in nums]
# nums.sort()
