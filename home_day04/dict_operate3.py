"""
    dict_operate3 - 字典的相关操作
 Author : Iven
 Date : 2022/3/9
"""
dict1 = {'A': 100, 'B': 200, 'C': 300}
dict2 = {'D': 400, 'E': 500, 'A': 600}

# print(dict1+ dict2)  TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# 通过update 之前没有的键值对会添加, 存在的键会更新值
# 更新合并
dict1.update(dict2)
print(dict1)



#删除, 需要删除的键必须存在,否则会出现KeyError
# del dict1['B']
dict1.pop('B')
dict1.popitem()
print(dict1)


dict1.setdefault('C', 800)


# 清空
dict1.clear()
print(dict1)