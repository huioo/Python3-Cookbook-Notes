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
