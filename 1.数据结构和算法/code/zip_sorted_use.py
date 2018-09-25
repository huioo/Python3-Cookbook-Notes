from operator import itemgetter
# 股票名和价格映射字典
prices = {
    'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55,
    'HPQ': 37.20, 'FB': 10.75
}
kvs = prices.items()
minimum = min(kvs, key=itemgetter(1))
maximum = max(kvs, key=itemgetter(1))
print(minimum, maximum)     # ('FB', 10.75) ('AAPL', 612.78)

print(prices.keys())   # dict_keys(['ACME', 'AAPL', 'IBM', 'HPQ', 'FB'])
print(prices.values())   # dict_values([45.23, 612.78, 205.55, 37.2, 10.75])

# zip() 函数创建的是一个只能访问一次的迭代器
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price, max_price)     # (10.75, 'FB') (612.78, 'AAPL')

# sorted() 函数排序默认 element-wise 排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]

min(prices, key=lambda k: prices[k])   # Returns 'FB'
max(prices, key=lambda k: prices[k])   # Returns 'AAPL'

