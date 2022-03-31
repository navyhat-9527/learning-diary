"""
Joseph circle - 幸运的女人
Author : wangyiwen03
Date : 2022/2/25
"""

persons = [i for i in range(1, 31)]
print(persons)
# index, counter, numbers = 0, 0, 0
#
# while counter < 15:
#     if persons[index]:
#         numbers += 1
#         if numbers == 9:
#             counter += 1
#             numbers = 0
#             persons[index]= False
#     index += 1
#     if index == 30:
#         index = 0
# print(persons)

for _ in range(15):
    persons = persons[9:] + persons[:8]  # 第10个人-最后一个 + 第一个-第8个人 每次把第10个人排到第一个然后将剩下的人按顺序后延
    print(persons)
for i in range(1,31):
    print('女' if i in persons else '男', end='')