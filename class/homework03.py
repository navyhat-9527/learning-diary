"""
    homework03 - 用函数实现求两个数的最大公约数和最小公倍数
 Author : Iven
 Date : 2022/3/16
"""


def gcd(m, n):
    """求最大公约数"""
    while m % n != 0:
        m, n = n, m % n
    return n


def lcm(m, n):
    """最小公倍数"""
    return m * n // gcd(m, n)

print(gcd(15, 27))
print(lcm(15, 27))
