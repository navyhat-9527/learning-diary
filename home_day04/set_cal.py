"""
    set_cal - 集合的运算
 Author : Iven
 Date : 2022/3/8
"""

set1 = {1, 1, 2, 3, 3, 4, 1, 2}
set2 = {2, 5, 2, 1, 7, 9}
print(1 in set1)
print(1 not in set1)

# 交集
print(set1 & set2)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)
print(set2.difference(set1))

# 对称差
print(set1 ^ set2)
print((set1 | set2) - (set1 & set2))
print(set1.symmetric_difference(set2))

set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 判断真子集
print(set1 < set3)
# 判断自己
print(set1 <= set3)
# 判断超集
print(set3 > set2)


