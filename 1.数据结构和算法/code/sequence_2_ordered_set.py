# 删除序列相同元素并保持顺序


def dedupe1(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(iterable, key=None):
    """ 自定义重复条件 """
    seen = set()
    for item in iterable:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
        
        
a = [1, 5, 2, 1, 9, 1, 5, 10]

print(list(dedupe1(a)))     # [1, 5, 2, 9, 10]

b = zip(['']*len(a), a)
print(list(dedupe2(b, key=lambda x: x[1])))  # [('', 1), ('', 5), ('', 2), ('', 9), ('', 10)]

b = zip(['']*len(a), a)
print(list(dedupe2(b, key=lambda x: x[0])))  # [('', 1)]
