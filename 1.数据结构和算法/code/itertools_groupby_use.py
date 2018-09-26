from itertools import groupby

rows = [{'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 2, 'b': 2}, {'a': 1, 'b': 3}]

# groupby 使用前需要对iterable进行排序
by_b = groupby(rows, key=lambda x: x['b'])
print(by_b)     # <itertools.groupby object at 0x00000206D4497958>
'''
若只在此时迭代 by_b，打印情况如下：
print('***')
for b, items in by_b:
    print(b, [i for i in items])
print('***')

***
2 [{'a': 1, 'b': 2}]
1 [{'a': 2, 'b': 1}]
2 [{'a': 2, 'b': 2}]
3 [{'a': 1, 'b': 3}]
***
'''

rows_by_b = list(by_b)
'''
若只在此时迭代 by_b，打印情况如下：
print('***')
for b, items in by_b:
    print(b, [i for i in items])
print('***')
# 紧接着迭代 by_b 的 list 对象
print([list(row) for b, row in rows_by_b])

迭代时没有值了。
***
***
[[], [], [], [{'a': 1, 'b': 3}]]

若只在此时迭代 rows_by_b，打印情况如下：
print('***')
for b, items in rows_by_b:
    print(b, [i for i in items])
print('***')
# 紧接着迭代 by_b 的 list 对象
print([list(row) for b, row in rows_by_b])

迭代时的值如下
***
2 []
1 []
2 []
3 [{'a': 1, 'b': 3}]
***
[[], [], [], []]

'''
print(rows_by_b)
# [(2, <itertools._grouper object at 0x00000206D614A5C0>),
#  (1, <itertools._grouper object at 0x00000206D6152C50>),
#  (2, <itertools._grouper object at 0x00000206D6152C88>),
#  (3, <itertools._grouper object at 0x00000206D6152CC0>)]

row = rows_by_b[0]
print(row)     # (2, <itertools._grouper object at 0x00000206D614A5C0>)

items = rows_by_b[0][1]
print(items)    # <itertools._grouper object at 0x00000206D614A5C0>

print([i for i in items])    # []，进行操作，迭代器进行了迭代操作,迭代器中已经到最后，没有值了
print(list(items))    # []


rows = [{'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 2, 'b': 1}, {'a': 1, 'b': 3}]
groups = groupby(rows)  # key 为None时，按相同的值进行分组
print(list(groups))
# [({'a': 1, 'b': 2}, <itertools._grouper object at 0x00000271337B2CF8>),
#  ({'a': 2, 'b': 1}, <itertools._grouper object at 0x00000271337B2C50>),
#  ({'a': 1, 'b': 3}, <itertools._grouper object at 0x00000271337B2C88>)]


