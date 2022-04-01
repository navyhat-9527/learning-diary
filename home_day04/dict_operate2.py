"""
    dict_operate2 -
 Author : Iven
 Date : 2022/3/9
"""
student = dict(id=1002, name='王大锤', gender='True')
print(student)
# 字典的索引运算,放在赋值运算符的左边
# 如果索引对应的键是存在的,则更新存储的值
student['gender'] = ' False'
# 如果索引对应的值不存在,则新增键值对
student['address'] = '四川成都'
print(student)

print('name' in student)
print('age' in student)
print('address' in student)

# 使用get函数通过key获取value时, 如果key值不存在, 不会发生KeyError错误
# 而是得到一个None(空值)
print(student.get('age'))
# 如果name不是键值, 则输出填写值
print(student.get('age', 20))
print(student.get('name'))

# 删除键值对
del student['name']
print(student.get('name', 'nobody'))
