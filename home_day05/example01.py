"""
    example01 -  获取A班和B班的考试成绩的描述性统计信息

如果要使用
 Author : Iven
 Date : 2022/3/17
"""
from utils.stats import *


class_a_scores = [random.randrange(40, 100) for _ in range(50)]

class_b_scores = [random.randrange(40, 100) for _ in range(50)]

print('A班考试成绩描述性统计信息: ')
print(f'A班的平均分是:{avg(class_a_scores)} ')
print(f'A班的中位数是:{median(class_a_scores)}')
print(f'A班的方差是:{variance(class_a_scores)}')
print(f'A班的标准差是:{std_deviation(class_a_scores)}')
print('B班考试成绩描述性统计信息:')
print(f'A班的平均分是:{avg(class_b_scores)}')
print(f'A班的中位数是:{median(class_b_scores)}')
print(f'A班的方差是:{variance(class_b_scores)}')
print(f'A班的标准差是:{std_deviation(class_b_scores)}')