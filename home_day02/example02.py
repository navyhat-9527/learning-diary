"""
    example02 - 百钱买百鸡
    鸡翁一值钱5,鸡母一值钱3,鸡雏三值钱1,用百钱买百鸡,问鸡翁鸡母鸡雏各几何
 Author : Iven
 Date : 2021/12/27
 5x +3y + 1/3z = 100
"""
cock = 5
hen = 3
chiken = 1 / 3
money = 100
# for num_cock in range(0, 21):
#     num_hen = 0
#     num_chiken = 0
#     money = 100 - 5 * num_cock
#     for num_hen in range(0, int(money - 5 * num_cock) // 3 + 1):
#         num_chiken = 3 * (100 - 5 * num_cock - 3 * num_hen)
#         money = 100 - 5 * num_cock - 3 * num_hen - 1 / 3 * num_chiken
#         if money == 0:
#                 print(num_cock, num_hen, num_chiken)
#     money = 100

for num_cock in range (0,21):
    for num_hen in range (0 , 34):
        num_chiken = 100 - num_hen -num_cock
        if num_chiken*1/3 + num_cock*5 +num_hen*3 == 100 :
            print(num_cock,num_hen,num_chiken)