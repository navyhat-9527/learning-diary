"""
    excesice -数字矩阵
    输入N 按照如下所示的规律打印
 Author : Iven
 Date : 2021/12/28
"""

user_input = int(input('请输入打印次数'))

for i in range (1,user_input+1):
    print(f'{i} ' * i)