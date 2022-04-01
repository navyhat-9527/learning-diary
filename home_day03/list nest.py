"""
    list nest - 循环嵌套
 Author : Iven
 Date : 2022/2/26
"""
import random

names = ['张三', '李四', '王五', '二麻子', '李总']

courses = ['语文', '数学', '英语']

scores = [[random.randrange(50, 101) for _ in range(len(courses))]
          for _ in range(len(names))]

print(scores)

for i, name in enumerate(names):
    for j, course in enumerate(courses):
        print(f'{name}的{course}成绩:{scores[i][j]}')

for i, name in enumerate(names):
    print(f'{name}的平均成绩为{sum(scores[i])/3:.1f}')

for j, course in enumerate(courses):
    temp = [scores[i][j] for i in range(len(names))]
    print(f'{courses[j]}的最高分为{max(temp)}')
    print(f'{courses[j]}的最低分为{min(temp)}')

