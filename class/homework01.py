"""
    homework01 - 写一个实现生成指定长度的随机验证码(有英文字母和数字组成)的函数
 Author : Iven
 Date : 2022/3/16
"""
import random
import string


def verify_code(length=4):
    '''生成随机验证码

    :param length: 验证码的长度
    :return: 随机验证码的字符串
    '''
    code_combine = random.choices(string.digits + string.ascii_uppercase, k=length)
    return ''.join(code_combine)


for _ in range(10):
    print(verify_code(4))
