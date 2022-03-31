"""
homework -  CRAPS赌博游戏
玩家摇两个色子,如果第一次摇出了7点或11点则玩家获胜; 如果玩家摇出了2点、3点、12点则庄家获胜；
如果摇出其他点数则游戏继续，玩家重新摇色子；如果玩家摇出了第一次摇的点数，则玩家获胜；
如果玩家摇出了7点，庄家获胜；如果玩家摇出其他点数则游戏继续，玩家重新摇色子直到游戏结束。

游戏开始时, 玩家有1000元的初始资金,玩家可以下注,赢了获得下注的金额,输了就扣除下注的金额
直到输光为止
Author : wangyiwen03
Date : 2022/3/10
"""
import random

play_money = 1000


def roll_dice(times=2):  # 默认值=2
    """
    摇色子
    :param times: 色子的数量
    :return: 色子的总点数
    """
    total = 0
    for _ in range(times):
        total += random.randint(1, 7)
    return total


def paly_win():
    """闲家胜"""
    print('play win!')
    global play_money
    play_money += debt
    return play_money


def bank_win():
    """庄家胜"""
    print('bank win!')
    global play_money
    play_money -= debt


while play_money > 0:
    debt = 0
    print(f'目前玩家的资产为{play_money}')
    while debt > play_money or debt <= 0:
        try:
            debt = int(input('请下注:'))
        except ValueError:
            pass
    temp = roll_dice()
    print(temp)
    if temp in (7, 11):
        paly_win()
    elif temp in (2, 3, 12):
        bank_win()
    else:
        while True:
            current_dice = roll_dice()
            print(current_dice)
            if current_dice == temp:
                paly_win()
                break
            elif current_dice == 7:
                bank_win()
                break

print('玩家已破产,游戏结束')