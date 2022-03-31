"""
homework01 - 输入10个1-100之间的数字,计算他们的平均值,并指出最大值和最小值.
Author : wangyiwen03
Date : 2021/12/29
"""

i = 1
max = 0
min = 100
total = 0
while True:
    num = int(input(f'请输入第{i}个数(输入范围在1-100之间): '))
    if 1 <= num <= 100:
        total += num
        if num > max:
            max = num
        elif num < min:
            min = num
        else:
            pass
    else:
        i -= 1
        print("输入有误,请输入1-100之间的数字")
    i += 1
    if i > 10:
        avg = total / 10
        print(f'平均值={avg},最大值={max},最小值={min}')
        break
