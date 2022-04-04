"""
    homework02 - 写一个函数判断一个正整数是不是质数
 Author : Iven
 Date : 2022/3/16
"""


def is_prime(num):
    """
    判断一个数是不是质数

    :param num: 给出一个正整数
    :return: 判断是质数返回True,不是质数返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num != 1


counter = 0
for n in range(1, 1000):
    if is_prime(n):
        counter += 1
        print(n, end=' ')
print()
print(counter)