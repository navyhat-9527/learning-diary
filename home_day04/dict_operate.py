"""
    dict_operate -  字典  --->元素由键和值两个部分构成,冒号前面的称为键,冒号后称为值,合在一起叫键值对.
 Author : Iven
 Date : 2022/3/9
"""


# 键必须是不可变的数据类型, 运用哈希存储
student = {'id': 1001,
           'name': '骆昊',
           'gender': True,
           'birth': '1980-11',
           'add': '四川成都',
           'habit': ['code', 'chess', 'ping-pong'],
           'contants': {'qq':'12346789',
                        'tel':'1235456787',
                        'email':'123@baijia.com'
                        }
}

print(student['name'])
print(student['birth'])