"""
    Joseph环 - 幸运的女人
    有15个男人和15个女人坐船出海,船坏了,需要把其中15个人扔到海里,其他人才能活下来;
    所有人围成一个圈,由某人从1开始报数,报到9的人就被扔到海里,下一个人重新从1开始报数,直到将15个人扔到海里。
    最后，15个女人都活了下来，15个男人被扔到了海里
    问原先哪些位置是男人的位子，哪些是女人的位子
 Author : Iven
 Date : 2022/2/25

 [1, 2, 3, 4, 5, x, x, 8 , x ,10 , 11, 12, 13, 14, 15, x, 17, x, x, 20, 21, 22, 23 ,24, 25, x ,x, 28, 29 ,30]
"""

persons = ['o'] * 30
index, counter, number = 0, 0, 0

while counter < 15:
    for i in range(30 - counter):
        number += 1
        index = i
        if number != 9:
            pass
        elif number == 9:
            counter += 1
            persons[index] = 'x'
            number = 0


print(persons)