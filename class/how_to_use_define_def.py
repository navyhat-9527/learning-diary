"""
    how_to_use_define_def -  函数的定义和使用

计算组合数: C(M,N) = M! / N! / (M-N)!
将来使用函数要么是python标准库或者三方库的函数,
要么是自定义的函数

 Author : Iven
 Date : 2022/3/16
"""


def factorial(m):
    total = 1
    for i in range(2, m + 1):
        total *= i
    return total


m = int(input('m = '))
n = int(input('n= '))
print(factorial(m)/factorial(n)/factorial(m-n))