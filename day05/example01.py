"""
example01 -   列表的相关操作
Author : wangyiwen03
Date : 2022/1/26
"""

list1 = ['apple', 'banana', 'orange']  # 字面量定义
list2 = list(list1)
list3 = list(range(1, 100))  # 构造器函数
list4 = list(i ** 2 for i in range(1, 10))  # 生成式(推导式)语法

print(len(list1))  # 获取列表元素个数

# 列表遍历

for i in range(len(list1)):
    print(list1[i])

for i in list1:
    print(i)

for i, x in enumerate(list1):
    print(i, x)

# 和列表相关的运算
list4 = [1, 100, 1000] * 5  # 重复运算

# 成员运算---> True/False

print(10 in list4)  # 10 是否在list4中 bool值
print(5 not in list4)

# 索引和切片

# 整形索引:  正向索引 0 ~ N-1 / 负向索引: -N ~ -1


# 合并运算

list5 = [1, 2, 3]
list6 = [4, 5, 6]
temp = list5 + list6
print(temp)
list5 = list5 + list6
print(list5)
# list5 = list5 + list6   ==  list5 += list6
# 比较

list7 = list(range(1, 8, 2))
list8 = [1, 3, 5, 7, 9]
print(list7 == list8)

# 比较两个列表对应元素的大小
list8 =[1, 3, 5, 8]
print(list7 < list8)# 按顺序比较
