"""
list operation - 列表的相关操作
Author : wangyiwen03
Date : 2022/1/27
"""
items=['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple']

#寻找元素
if 'apple' in items:
    print(items.index('apple'))

#list.count() 统计元素在列表中出现的次数
print(items.count('apple'))


#添加元素
items.append('buleberry')
items.insert(1,'watermelon')
print(items)

#删除元素
items.pop()
items.pop(4)
del items[0]  #面向对象删除
items.remove('apple')

#清空列表
print(items)
items.clear()
