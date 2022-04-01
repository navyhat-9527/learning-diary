"""
    set_operate - 集合的操作(方法)
 Author : Iven
 Date : 2022/3/8
"""


set1 = {'apple', 'banana', 'pitaya', 'apple'}
set2 = {True, False, True}
set1.add('grape')
set1.add('durian')
set1.discard('apple')
print(set1)
print(set2)
# set3 = {[1, 2, 3], [4, 5, 6,]}  TypeError: unhashable type: 'list'
# 集合底层使用了一种高效率的储存方式,我们称之为散列(哈希)存储

print(set1.pop())
