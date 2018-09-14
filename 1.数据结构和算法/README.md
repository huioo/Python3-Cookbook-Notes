# 第一章：数据结构和算法

Python 提供了大量的内置数据结构，包括列表，集合以及字典。大多数情况下使用这些数据结构是很简单的。 但是，我们也会经常碰到到诸如查询，排序和过滤等等这些普遍存在的问题。 因此，这一章的目的就是讨论这些比较常见的问题和算法。 另外，我们也会给出在集合模块 collections 当中操作这些数据结构的方法。

# 1. 解压序列赋值给多个变量
元素赋值：使用多个变量名，“,”分隔接收同等长度的序列中的元素。  
赋值语句 -> 解压（变量的数量必须跟序列元素的数量一样） -> 赋值
```python
p = (4, 5)
x, y = p  # x=4, y=5
p = (1, 2, 3, 4, 5)
x, _, _, _, y = p # x=1, y=5; 使用任意变量名占位，只使用一部分

p = (1, (2, 3, 4), 5)
x, (a1, a2, a3), y = p # x=1, a1=2, a2=3, a3=4, y

```  
变量个数与序列元素不匹配：
```python
In[2]: p = (1, (2, 3, 4), 5)
In[9]: x, (a1, a2, a3) = p
Traceback (most recent call last):
  File "F:\Python3\lib\site-packages\IPython\core\interactiveshell.py", line 2961, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-9-207532b8fdb0>", line 1, in <module>
    x, (a1, a2, a3) = p
ValueError: too many values to unpack (expected 2)
```

# 2. 解压可迭代对象赋值给多个变量
元素解压：使用“* + 变量名”的形式动态接受多个元素，变量类型是list  
```python
p = (1, 2, 3, 4, 5)
x, *y, z = p   # x=1, y=[2,3,4], z=5
a, b, c, d, e, *f = p   # a=1, b=2, c=3, d=4, e=5, f=[]

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record  # name='ACME', year=2012

```

# 3. 保留最后 N 个元素
deque（双向队列 FIFO）: `collections`模块的工具类 `from collections import deque`  
使用` deque(maxlen=N) `构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。  

`q = deque(maxlen=3)`创建一个长度为3的堆，用法类似list。

参考示例`code/sequence_tail_n.py`。  
`yield`表达式参考4.3节。

# 4. 查找最大或最小的 N 个元素
heap （堆）: 模块 `import heapq`

模块方法：
- 'heappush'：
- 'heappop'： 
- 'heapify'： 堆排序
- 'heapreplace'：
- 'merge'： 
- 'nlargest'： 找出最大的几个元素
- 'nsmallest'： 找出最小的几个元素
- 'heappushpop'： 

参考示例`code/heapq_use.py`。  


# 5. 实现一个优先级队列
heap （堆）: 模块 `import heapq`

`heappush`方法的特性：插入元素之后，heap[0]总是最小；  
`heappop`方法的特性：取出的元素总是最小的；
`heappop()` 函数总是返回”最小的”的元素，这就是保证队列pop操作返回正确元素的关键。 另外，由于 push 和 pop 操作时间复杂度为 O(log N)，其中 N 是堆的大小，因此就算是 N 很大的时候它们运行速度也依旧很快。
```python
# 每个元素，对应一个优先级priority值(priority, index, item)
nums = [
    (1, 0, 1), (5, 1, 5), (2, 2, 2), (4, 3, 4), (3, 4, 3), 
]
import heapq
heapq.heapify(nums)
print(heapq.heappop(nums))  # (1, 0, 1)
print(heapq.heappop(nums))  # (2, 2, 2)
print(heapq.heappop(nums))  # (3, 4, 3)

```
上面根据priority的值排序，总是取出最小的。反之，取priority的相反数。


# 6. 字典中的键映射多个值
multidict： 一个键对应多个值的字典，即键对应的值是list、set、tuple等序列形式。  
个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面。比如，你可以像下面这样构造这样的字典：
```python
d = {'a': [1, 2, 3], 'b': [4, 5]}
e = {'a': {1, 2, 3}, 'b': {4, 5}}
```
模块的工具类 `from collections import defaultdict`：`defaultdict`的第一个特性是它会自动初始化每个`key`刚开始对应的值，所以只需要管理这个默认的值对象。
```python
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
```
dict类型的方法 `{}.setdefault('a', []).append(1)`：获取字典某个key的对应value，如果不存在，就将默认值赋给value。
```python
d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
```
参考示例`collections_defaultdict.py`。

# 8. 字典的运算
有序字典
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
