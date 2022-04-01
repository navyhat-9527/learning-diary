"""
    dict_create - 字典的创建和使用
 Author : Iven
 Date : 2022/3/9
"""

# 字面量语法
student = {'id': 1001,
           'name': '骆昊',
           'gender': True,
           'birth': '1980-11',
           'add': '四川成都',
           'habit': ['code', 'chess', 'ping-pong'],
           'contants': {'qq': '12346789',
                        'tel': '1235456787',
                        'email': '123@baijia.com'
                        }
           }

print(student['name'])
print(student['birth'])

# 构造器函数
student2 = dict(id=1002, name='王大锤', gender='True')
print(student2)
print(student2['name'])
print(('-' * 50))

# 生成式语法(推导式)
list1 = [i for i in range(1, 10)]
print(list1)
set1 = {i for i in range(1, 10)}
print(set1)
dict1 = {i: i ** 2 for i in range(1, 10)}
print(dict1)
print(('-' * 50))

# 生成器
gen = (i for i in range(1, 10))
print(type(gen))

print(('-' * 50))

# 遍历字典中的键
for key in student:
    print(key, student[key])
print(('-' * 50))

# 遍历字典中的值
for value in student.values():
    print((value))
print(('-' * 50))

# 遍历字典中的键值对
for key, value in student.items():
    print(key, value)
