"""
work -
Author : wangyiwen03
Date : 2022/2/27
"""

import turtle

bob = turtle.Turtle()
# x = [-110, 0, 110, -55, 55]
# y = [-25, -25, -25, -75, -75]
# c = ["red","blue","green","yellow","black"]
bob.penup()
bob.goto(-110, -25)
bob.color('red')
bob.pendown()
bob.circle(50)

bob.penup()
bob.goto(0, -25)
bob.color('blue')
bob.pendown()
bob.circle(50)
bob.hideturtle()

bob.penup()
bob.goto(110, -25)
bob.color('green')
bob.pendown()
bob.circle(50)

bob.penup()
bob.goto(-55, -75)
bob.color('yellow')
bob.pendown()
bob.circle(50)

bob.penup()
bob.goto(55, -75)
bob.color('black')
bob.pendown()
bob.circle(50)
bob.hideturtle()
