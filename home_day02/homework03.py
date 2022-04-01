"""
    homework03 - 计算机生成一个1-100的随机数,人输入一个自己猜的数字
    计算机会给出对应提示:"大一点","小一点","恭喜你猜对了",知道猜中为止.
    如果所猜次数超出7次,计算机温馨提示"智商余额明显不足"
 Author : Iven
 Date : 2021/12/28
"""
import random

answer = random.randrange(1,101)
Start = True
i = 1
while True :
    user_input= int(input("请输入猜测值: "))
    if user_input == answer:
        print("恭喜你猜对了")
        break
    elif user_input > answer:
        print("小一点")
    else:
        print("大一点")
    i += 1
    if i >7:
        print("智商余额明显不足")
print(f'一共猜了{i}次得出正确答案')