"""
game -
Author : wangyiwen03
Date : 2021/12/29
"""
import  random

answer = random.randrange(1,101)
i = 1
while True:
    num = int(input('请输入猜测得数字: '))
    if num == answer:
        print('恭喜你猜对啦!')
        print(f'共计猜{i}次得到正确答案')
        break
    elif num > answer:
        print('小一点')
    else:
        print('大一点')
    i += 1
    if i > 7 :
        print('智商余额不足')
