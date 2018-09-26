from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

merge = ChainMap(a, b)
print(merge)    # ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})

merge1 = merge.new_child({'a': 1})
print(merge1)   # ChainMap({'a': 1}, {'x': 1, 'z': 3}, {'y': 2, 'z': 4})

merge2 = merge1.new_child({'b': 2})
print(merge2)   # ChainMap({'b': 2}, {'a': 1}, {'x': 1, 'z': 3}, {'y': 2, 'z': 4})

# 返回一个新的ChainMap对象
print(merge2.parents)   # ChainMap({'a': 1}, {'x': 1, 'z': 3}, {'y': 2, 'z': 4})
print(merge2.parents.parents)   # ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})

# new_child()之后，原ChainMap对象没有变
print(merge1)   # ChainMap({'a': 1}, {'x': 1, 'z': 3}, {'y': 2, 'z': 4})
print(merge2)   # ChainMap({'b': 2}, {'a': 1}, {'x': 1, 'z': 3}, {'y': 2, 'z': 4})

#
merge['x'] = 100
print(merge)    # ChainMap({'x': 100, 'z': 3}, {'y': 2, 'z': 4})
merge['a'] = 'a'
print(merge)    # ChainMap({'x': 100, 'z': 3, 'a': 'a'}, {'y': 2, 'z': 4})

try:
    del merge['y']
except KeyError as e:
    print(e)    # "Key not found in the first mapping: 'y'"
