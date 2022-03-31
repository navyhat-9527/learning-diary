"""
example05 - 输入10个数,计算平均值/方差/标准差,找出最大值和最小值

描述性统计 -----> 通常可以获得整体的情况
推断性统计 -----> 只能获得样本呢,通过样本去推测总体

Author : wangyiwen03
Date : 2022/1/12
"""

nums = []

for _ in range(10):
    temp = int(input('请输入数据: '))
    nums.append(temp)

mean_value = sum(nums)/len(nums)
max_value = max(nums)
min_value = min(nums)

total = 0
for num in nums:
    total += (num-mean_value)**2

var_value = total/(len(nums)-1)
std_value = var_value**0.5

print(f'输入数据为:{nums}')
print(f'均值:{mean_value}')
print(f'最大值:{max_value}')
print(f'最小值:{min_value}')
print(f'方差:{var_value}')
print(f'标准差:{std_value}')
print(f'极差:{max_value-min_value}')
