from itertools import compress

a = [1, 2, 3, 4, 5, 6]
selectors = [1, 0, 1, 0, 1, 0]

result = compress(a, selectors)     # 根据selectors的对应位置的 boolean 值，选择为 True 的元素值
print(list(result))     # [1, 3, 5]

result = filter(lambda x: x % 2, a)
print(list(result))     # [1, 3, 5]

