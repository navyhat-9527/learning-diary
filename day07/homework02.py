"""
homework02 -  双色球随机选号(实现机选N注)

红色球01-33, 选择不重复的6个球, 按从小到大排列.
蓝色球01-16, 选择一个球,跟在红色球后面

Author : wangyiwen03
Date : 2022/3/14
"""
import random


def ball_chosen(ball_numbers, num):
    """

    :param ball_numbers: 总球数
    :param num: 选球数
    :return: 中球结果
    """
    ball_numbers = [i for i in range(1, ball_numbers)]
    balls = random.sample(ball_numbers, k=num)
    return balls


n = int(input('机选几注: '))


def double_balls():
    """双色球"""
    for _ in range(n):
        red_balls = ball_chosen(34, 6)
        blue_balls = ball_chosen(14, 1)
        red_balls.sort()
        selected_balls = red_balls + blue_balls
        for i in selected_balls:
            print(f'{i:0>2d}', end=' ')
        print()


def lotter():
    """大乐透"""
    for _ in range(n):
        red_balls = ball_chosen(36, 5)
        blue_balls = ball_chosen(12, 2)
        red_balls.sort()
        blue_balls.sort()
        selected_balls = red_balls + blue_balls
        for i in selected_balls:
            print(f'{i:0>2d}', end=' ')
        print()


double_balls()
lotter()
