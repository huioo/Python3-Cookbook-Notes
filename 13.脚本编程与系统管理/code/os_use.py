"""

In[18]: a = list(os.walk('.\\1.数据结构和算法'))
In[19]: len(a)
Out[19]: 3
In[20]: a[1]
Out[20]:
('.\\1.数据结构和算法\\code',
 [],
 ['collections_defaultdict.py', 'heapq_use.py', 'sequence_tail_n.py'])
In[21]: a[0]
Out[21]:
('.\\1.数据结构和算法',
 ['code', 'data'],
 ['1.解压序列赋值给多个变量.md',
  '10.删除序列相同元素并保持顺序.md',
  '11.命名切片.md',
  '12.序列中出现次数最多的元素.md',
  '13.通过某个关键字排序一个字典列表.md',
  '2.解压可迭代对象赋值给多个变量.md',
  '3.保留最后 N 个元素.md',
  '4.查找最大或最小的 N 个元素.md',
  '5.实现一个优先级队列.md',
  '6.字典中的键映射多个值.md',
  '7.字典排序.md',
  '8.字典的运算.md',
  '9.查找两字典的相同点.md',
  'README.md'])
In[22]: a[1]
Out[22]:
('.\\1.数据结构和算法\\code',
 [],
 ['collections_defaultdict.py', 'heapq_use.py', 'sequence_tail_n.py'])
In[23]: a[2]
Out[23]: ('.\\1.数据结构和算法\\data', [], ['somefile.txt'])
"""
