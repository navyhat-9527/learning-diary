"""
poke game - 用一个列表保存54张扑克牌,先洗牌,
再按斗地主的方式把牌发给三个玩家,多的3张牌给第一个玩家(地主)
最后把每个玩家手上的牌显示出来
Author : wangyiwen03
Date : 2022/2/25
"""
import random

suites = ['♠', '♥', '♣', '♦']
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = [f'{suite}{face}' for suite in suites for face in faces]
cards.append('大王')
cards.append('小王')
print(cards)

# 嵌套列表
players = [[] for _ in range(3)]

random.shuffle(cards)

for _ in range(17):
    for i in range(3):
        players[i].append(cards.pop())

cards.extend(cards)

for i in range(3):
    players[i].sort(key=lambda x: x[1:])
    for card in players[i]:
        print(card, end=' ')
    print()

