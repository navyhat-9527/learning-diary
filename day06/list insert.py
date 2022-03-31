"""
列表嵌套  - 保存5个学生的3们成绩
Author : wangyiwen03
Date : 2022/2/26
"""
import random

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']

scores = [[random.randrange(50, 100) for _ in range(3)] for _ in range(5)]
print(scores)

# for i, name in enumerate(names):
#     for j, course in enumerate(courses):
#         print(f'{name}的{course}成绩是:{scores[i][j]}')

for j, course in enumerate(courses):
    temp = [scores[i][j] for i, name in enumerate(names)]
    print(temp)# 学科分数排名