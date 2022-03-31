"""
game -  九宫格
Author : wangyiwen03
Date : 2022/3/5
"""

import turtle as t
import os
t.speed(0)
t.penup()
t.goto(-250, 150)

for i in range(3):
    t.fd(100)
    t.pendown()
    for _ in range(4):
        t.fd(100)
        t.right(90)

t.penup()
t.goto(-250, 50)
for _ in range(3):
    t.fd(100)
    t.pendown()
    for _ in range(4):
        t.fd(100)
        t.right(90)

t.penup()
t.goto(-250, -50)
for _ in range(3):
    t.fd(100)
    t.pendown()
    for _ in range(4):
        t.fd(100)
        t.right(90)


# while True:
choice = int(input('输入你想填入的位子代码: '))
if choice == 1:
    t.penup()
    t.goto(-100,70)
    t.pendown()
    t.circle(30)


os.system('pause')