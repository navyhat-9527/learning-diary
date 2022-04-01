"""
    homework03 - 字典中保存了股票的信息, 完成下面的操作
    1. 找出股票的价格大于100元的股票并创建一个新的字典
    2. 找出价格最高和最低的股票对应的股票代码
    3. 按照股票价格从高到低给股票代码排序

 Author : Iven
 Date : 2022/3/9
"""

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# new_stocks = {}
# for key, value in stocks.items():
#     if value > 100:
#         new_stocks[key] = value
new_stocks = {key: value for key, value in stocks.items() if value > 100}
print('-' * 50)

print(zip(stocks.values(), stocks.keys()))
print('-' * 50)
print(max(stocks, key=stocks.get))
print('-' * 50)
print(min(stocks, key=stocks.get))
print('-' * 50)
print(sorted(stocks, key=stocks.get, reverse=True))


print('-' * 50)
print(max(zip(stocks.values(), stocks.keys()))[1])
print(min(zip(stocks.values(), stocks.keys()))[1])

# zip可以将两个列表或字符串压缩成二元组
# 再通过dict将二元组转换为字典即可交换键值对

for x in zip(stocks.values(), stocks.keys()):
    print(x)
dict1 = dict(zip('ABCDE', [1, 2, 3, 4]))
dict2 = dict(A=1, B=2, C=3, D=4)
