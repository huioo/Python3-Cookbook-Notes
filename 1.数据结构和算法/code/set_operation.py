# 集合操作

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 相同的键
print(a.keys() & b.keys())         # { 'x', 'y' }
# 在a中且不在b中的键
print(a.keys() - b.keys())         # { 'z' }
# 相同的键值对
print(a.items() & b.items())       # { ('y', 2) }
# 制造一个新的字典，去掉某些键（去掉'z'和'w'）
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)                           # {'x': 1, 'y': 2}
