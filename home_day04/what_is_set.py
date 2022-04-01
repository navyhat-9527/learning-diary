"""
    what_is_set - 集合
 Author : Iven
 Date : 2022/3/8
"""

set1 = {1, 1, 2, 3, 3, 4, 1, 2}
print(type(set1))
print(set1)

# 构造器语法
set2 = set()
set3 = {}
print(type(set2))  # 互异性,没有重复度元素,打印结果是{1,2,3,4}
print(type(set3))  # set3是 字典:dict 不是集合:set

# print(set1[0])
# TypeError: 'set' object is not subscriptable

# 集合的循环遍历
for elem in set1:
    print(elem)

