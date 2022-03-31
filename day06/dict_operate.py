"""
dict_operate - 字典中保存了股票的信息,完成下面操作
1. 找出股票价格大于100的股票并创建一个新字典
2. 找出价格最高和最低的股票代码
3. 按照股票价格从高到低给股票排序
Author : wangyiwen03
Date : 2022/3/10
"""

stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.25,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.96,
    'SYMC': 21.29
}

new_stocks = {}
for stock, price in stocks.items():
    if price > 100:
        new_stocks[stock] = price
print('-' * 50)
print(new_stocks)
print('-' * 50)
print(max(zip(stocks.values(), stocks.keys())))
print(min(zip(stocks.values(), stocks.keys())))
print('-' * 50)
print(max(stocks, key=stocks.get))
print('-' * 50)
print(stocks.values())
print(stocks.get)
print('-' * 50)
print((sorted(stocks, key=stocks.get, reverse=True)))
