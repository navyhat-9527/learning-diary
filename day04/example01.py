"""
example01 - 数字矩阵
Author : wangyiwen03
Date : 2021/12/29
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# row = int(input('请输入数字: '))
# for i in range(1, row + 1):
#     for a in range(row):
#         print(i, end=' ')
#     print()

row = int(input('请输入数字: '))
for i in range(1, row + 1):
    for a in range(1,i+1):
        print(f"{a}*{i}={i*a}", end=' ')
    print()

