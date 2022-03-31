"""
bubble sort -Bubble Sort
冒泡排序:元素两两比较,如果前面的元素大于后面的元素则交换俩个元素位置

1.nums = [35, 12, 99, 58, 42, 49, 31, 73]
2.nums = [12, 35, 99, 58, 42, 49, 31, 73]
3.nums = [12, 35, 58, 99, 42, 49, 31, 73]
4.nums = [12, 35, 58, 42, 99, 49, 31, 73]
5.nums = [12, 35, 58, 42, 49, 99, 31, 73]
6.nums = [12, 35, 58, 42, 49, 31, 99, 73]
7.nums = [12, 35, 58, 42, 49, 31, 73, 99]

Author : wangyiwen03
Date : 2022/2/20
"""
import time

nums = [92, 26, 12, 73, 99, 21, 29, 72, 83, 64]

for i in range(1, len(nums)):
    swapped = False
    for j in range(0, len(nums) - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print(nums, i)
            swapped = True
        if nums[-j - i] < nums[-j - i - 1]:
            nums[-j - i], nums[-j- i - 1] = nums[-j - i - 1], nums[-j - i]
            swapped = True
            print(nums, i/2)
    if not swapped:
        print(i)
        break
