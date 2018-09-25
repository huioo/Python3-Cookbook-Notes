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
参考示例`code/collections_defaultdict.py`。

# 7. 字典排序
有序字典: 模块 `from collections import OrderedDict `

在迭代操作的时候它会保持元素被插入时的顺序，示例如下：

```python
import json
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

# 控制以 JSON 编码后字段的顺序
print(json.dumps(d))    # {"foo": 1, "bar": 2, "spam": 3, "grok": 4}

```
参考示例`code/collections_ordereddict.py`。

# 8. 字典的运算
`zip()`函数反转字典的键和值，返回一个只能访问一次的迭代器。  
`sorted()`函数排序，通过`key`或`func`指定排序方式。

```python
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

```

参考示例`code/zip_sorted_use.py`。

# 9. 查找两字典的相同点

字典是键集合与值集合的映射关系。字典的`keys()`方法返回一个展现键集合的键试图对象。键试图支持集合操作，比如集合并、交、差运算。  
如果你想对集合的键执行一些普通的集合操作，可以直接使用键试图对象而不用先将它们转换成一个set。  
字典的 `items()` 方法返回一个包含 (键，值) 对的元素视图对象。 这个对象同样也支持集合操作，并且可以被用来查找两个字典有哪些相同的键值对。  
尽管字典的 `values()` 方法也是类似，但是它并不支持这里介绍的集合操作。 某种程度上是因为值视图不能保证所有的值互不相同，这样会导致某些集合操作会出现问题。不过，如果你硬要在值上面执行这些集合操作的话，你可以先将值集合转换成 set，然后再执行集合运算就行了。  

## 集合操作

```python
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

```
在Python set是基本数据类型的一种集合类型，它有可变集合(`set()`)和不可变集合(`frozenset()`)两种。创建集合set、集合set添加、集合删除、交集、并集、差集的操作都是非常实用的方法。

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
>>> a - b   # 差集
{1}
>>> b - a   # 差集
{4}
>>> b & a   # 交集
{2, 3}
>>> a & b   # 交集
{2, 3}
>>> a | b   # 并集
{1, 2, 3, 4}

```

参考示例`code/set_operation.py`。

# 10. 删除序列相同元素并保持顺序

不保留序列顺序时，可使用`set()`生成一个集合，但序列的所有元素必须是`hashable`的类型，即元素必须可哈希，哈希散列值是整数类型。
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

模仿`sorted()`、`min()`、`max()`等函数，进行去重且保留顺序

```python
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

```

参考示例`code/sequence_2_ordered_set.py`。

# 11. 命名切片
切片对象：
- class slice(stop)
- class slice(start, stop[, step])

切片对象的使用：

```python
>>> items = [0, 1, 2, 3, 4, 5, 6]
>>> a = slice(2, 4)     # 创建slice对象
>>> items[2:4]          # 切片取值
[2, 3]
>>> items[a]            # 使用切片对象取值
[2, 3]
>>> items[a] = [10,11]  # 重新赋值
>>> items
[0, 1, 10, 11, 4, 5, 6] 
>>> del items[a]        # 删除
>>> items
[0, 1, 4, 5, 6]
```

如果你有一个切片对象a，你可以分别调用它的 a.start , a.stop , a.step 属性来获取更多的信息。
```python
>>> a = slice(5, 50, 2)
>>> a.start, a.stop, a.step
(5, 20, 2)
```

切片对象的` indices(size) `函数，返回` (start, stop, step) `三元组，它符合已知size大小的序列，所有的值都会被缩小，直到适合这个已知序列的边界为止。 这样，使用的时就不会出现 `IndexError` 异常。。
```python
>>> a = slice(5, 50, 2)
>>> s = 'HelloWorld'
>>> a.indices(len(s))
(5, 10, 2)
>>> s[a]
'Wrd'
```

# 12. 序列中出现次数最多的元素

统计计数: 模块工具类 `from collections import Counter`

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

# 13. 通过某个关键字排序一个字典列表

取值工具类（operator.itemgetter）: 模块的工具类 `from operator import itemgetter`

```python
>>> from operator import itemgetter
>>> itemgetter('a')
operator.itemgetter('a')

>>> a = [{'a':1},{'a':1},{'a':1},{'a':1},{'a':1}]
>>> map(itemgetter('a'), a)
<map object at 0x000002253B077EF0>
>>> list(map(itemgetter('a'), a))
[1, 1, 1, 1, 1]

```
