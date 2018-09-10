# 元素赋值
使用多个变量名，“,”分隔接收同等长度的序列中的元素。

# 元素解压
使用“*+变量名”动态接受多个元素，变量类型是list

# deque（双向队列 FIFO）
模块的工具类 `from collections import deque`

`q = deque(maxlen=3)`创建一个长度为3的堆，用法类似list。

# heap （堆）
模块 `import heapq`

模块方法：
- 'heappush'：添加
- 'heappop'： 取出
- 'heapify'： 堆化序列
- 'heapreplace'：取出并替换
- 'merge'： 合并
- 'nlargest'： 找出最大的几个元素
- 'nsmallest'： 找出最小的几个元素
- 'heappushpop'： 

# multidict
一个键映射多个值，即值为序列类型的容器，如list、set等

模块的工具类 `from collections import defaultdict`

dict类型的方法 `{}.setdefault('a', []).append(1)`

# 有序字典
记录插入顺序的字典类型

模块的工具类 `from collections import OrderedDict`

# zip()（压缩函数）
```python
>>> prices = {
...     'ACME': 45.23,
...     'AAPL': 612.78,
...     'IBM': 205.55,
...     'HPQ': 37.20,
...     'FB': 10.75
... }
>>> prices.items()
dict_items([('ACME', 45.23), ('AAPL', 612.78), ('IBM', 205.55), ('HPQ', 37.2), ('FB', 10.75)])
>>> zip(*prices.items())    # 返回一个迭代器，zip对象
<zip object at 0x000001B4C7340488>
>>> list(zip(*prices.items()))
[('ACME', 'AAPL', 'IBM', 'HPQ', 'FB'), (45.23, 612.78, 205.55, 37.2, 10.75)]
```

# 集合操作
在Python set是基本数据类型的一种集合类型，它有可变集合(`set()`)和不可变集合(`frozenset()`)两种。创建集合set、集合set添加、集合删除、交集、并集、差集的操作都是非常实用的方法。
```python
>>> set('boy')      # 创建set
{'o', 'y', 'b'}

>>> a = set('boy')  # 集合添加删除
>>> a.add('python')     # add()
>>> a
{'b', 'o', 'python', 'y'}
>>> a.remove('python') # remove()
>>> a
{'b', 'o', 'y'}
```
Python set()集合操作符号、数学符号：

 数学符号 | Python符号 | 含义
 :-----  |  :-----  |  :-----
 -或\    |  -        | 差集，相对补集
 ∩      |  &        | 交集
 ∪     |  &#124;    | 并集、合集
 ≠      |  !=       | 不等于
 =      |  ==       | 等于
 ∈     |  in       | 是成员关系
 ∉     |  not in    | 不是成员关系

```python
>>> a = set([1,2,3])
>>> b = set([2,3,4])
>>> a,b
({1, 2, 3}, {2, 3, 4})
>>> a - b
{1}
>>> b - a
{4}
>>> b & a
{2, 3}
>>> a & b
{2, 3}
>>> a | b
{1, 2, 3, 4}

```

# 去重且保留顺序
不保留序列顺序时，可使用`set()`生成一个集合，但序列的所有元素必须是`hashable`的类型，即元素必须可哈希。
```python
>>> a = {'a':1}
>>> b = {'b':2}
>>> set([a,b])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'dict'
>>> set([1,a])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'dict'

>>> hash(1)
1
>>> hash(a)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'dict'
```
模仿`sorted()`、`min()`、`max()`等函数

```python
def dedupe(iter):
    seen = set()
    for item in iter:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe(iter, key=None):
    """ 自定义重复条件 """
    seen = set()
    for item in iter:
        val = item if key is None else key(item)
        if val not in seen:
        ``    yield item
            seen.add(val)

```

# slice 切片 
切片对象的` indices(size) `函数，返回一个符合size大小的切片的` (start, stop, step) `元组值，所有的值都会被缩小，直到适合这个已知序列的边界为止。 这样，使用的时就不会出现 IndexError 异常。。
```python
>>> a1 = slice(2, 5, 1)
>>> b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> b[a1]
[2, 3, 4]
>>> a1.start, a.stop, a.step
(2, 3, 1)
>>> a1.indices('01')    # 参数值为integer类型
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> a1.indices(len('01'))
(2, 2, 1)
>>> a2 = a1.indices(len('01'))
>>> a2
(2, 2, 1)
>>> b[slice(*a2)]
[]
>>> '01'[slice(*a2)]
''
>>> '01'[a1]
''

```

# 统计计数
模块工具类 `from collections import Counter`

```python
>>> from collections import Counter
>>> Counter()                   # a new, empty counter
Counter()
>>> Counter('gallahad')         # a new counter from an iterable
Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
>>> Counter({'a': 4, 'b': 2})   # a new counter from a mapping
Counter({'a': 4, 'b': 2})
>>> Counter(a=4, b=2)           # a new counter from keyword args
Counter({'a': 4, 'b': 2})

>>> c = Counter('aaabbc')
>>> c['b'] -= 2                 # 计数为0时，依旧存在，除非删除entry或清除counter
>>> c
Counter({'a': 3, 'c': 1, 'b': 0})
>>> c['b'] -= 2
>>> c
Counter({'a': 3, 'c': 1, 'b': -2})

>>> c['d']      # 不存在时，返回0
0
```

# operator.itemgetter

模块的工具类 `from operator import itemgetter`


```python
>>> from operator import itemgetter
>>> itemgetter('a')
operator.itemgetter('a')
>>> 
"""
上述结果的itemgetter类相应`__repr__()`方法：
    def __repr__(self):
        return '%s.%s(%s)' % (self.__class__.__module__,
                              self.__class__.__name__,
                              ', '.join(map(repr, self._items)))
"""
```

```python
>>> a = [{'a':1},{'a':1},{'a':1},{'a':1},{'a':1}]
>>> map(itemgetter('a'), a)
<map object at 0x000002253B077EF0>
>>> list(map(itemgetter('a'), a))
[1, 1, 1, 1, 1]

"""
itemgetter类，实例化返回的 `callable` 对象，当作函数调用相关`__call__()`方法：
    def __init__(self, item, *items):
        if not items:
            self._items = (item,)
            def func(obj):
                return obj[item]
            self._call = func
        else:
            self._items = items = (item,) + items
            def func(obj):
                return tuple(obj[i] for i in items)
            self._call = func

    def __call__(self, obj):
        return self._call(obj)
"""
```
