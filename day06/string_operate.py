"""
string_operate - 字符串操作
Author : wangyiwen03
Date : 2022/3/4
"""

email = '   213114123@qq.com  '
tel = '    12313   141241  '
name = '  123是傻逼   '

print(email.strip())
print(tel.strip())
print(email.lstrip())
print(email.rsplit())
print(name.replace('傻逼', '**').strip())


