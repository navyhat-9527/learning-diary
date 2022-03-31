"""
homework01 -  一个列表中有多个重复元素,写一段代码去掉列表中的重复元素
list = [1, 2, 2, 3, 4, 4, 6, 8]
Author : wangyiwen03
Date : 2022/2/28
"""

names = ['王', '李四', '二麻子', '大狗', '王', '李四']
unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)

