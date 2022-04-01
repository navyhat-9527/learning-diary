"""
    homework04 - 输入10个1-99的证整数,计算平均值,找出最大值和最小值
 Author : Iven
 Date : 2021/12/28
"""
total = 0
max = 0
min = 100
for i in range(1,11):
    num = int(input(f'请输入第{i}个数字(范围在1-100之间):'))
    if num >100 or num < 0:
        print('输入数字有误,请输入范围在1-100之间')
        i -= 1
    else:
        total += num
        if num > max :
            max = num
        elif num < min :
            min = num
        else:
            pass
avg = total / 10
print(f"平均值={avg},最大值={max},最小值={min}")
