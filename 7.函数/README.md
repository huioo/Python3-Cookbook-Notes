# * 与 ** 的使用
用来动态接收函数接收的参数值。

一个`*`参数只能出现在函数定义中最后一个位置参数后面，而`**`参数只能出现在最后一个参数。  
```python
def a(*args, **kwargs):
    print(args)
    print(kwargs)

a(1,2,3,a=1,b=2)
"""
输出：
(1, 2, 3)
{'a': 1, 'b':2}
"""
```

有一点要注意的是，在`*`参数后面仍然可以定义其他参数，但是使用会出现错误，且需要被作为一个关键字参数来传值。
```python
def a(a1, *args, a2):
    print(a1, args, a2)

a(1,2,3,4,a2=5) # 正确用法，输出：1 (2, 3, 4) 5
a(1,2,3,4,5)    # 抛出异常，TypeError: a() missing 1 required keyword-only argument: 'a2'
```

```python
def a(a1, *args, **kwargs): 
    print(args, a1)
    print(kwargs)

a(1,2,3,a=1,b=2)
""" 输出：
(2, 3) 1
{'a': 1, 'b':2}
"""
```

## 某些参数强制使用关键字参数传递
强制`y`参数通过关键字参数传递。结合上面的某些示例，进行补充：
```python
def b(x, *, y):
    print(x, y)

b(1,2,3,4,y='y')    # 抛出异常：TypeError: b() takes 1 positional argument but 4 positional arguments (and 1 keyword-only argument) were given
                    # 这时，只能传递一个位置参数，和一个关键字参数
b(1,y='y')          # 输出：1 y

def b(x, *args, y, **kwargs):
    print(x, args, y, kwargs)

b(1,2,3,4,y='y',a=1,b=2)    # 输出：1 (2, 3, 4) y {'a': 1, 'b': 2}
b(1,2,3,a=1,b=2)    # 抛出异常，TypeError: a() missing 1 required keyword-only argument: 'a2'

```

# \_\_annotations__
给定义的函数的参数，添加注解，提示参数是什么类型。

```python
>>> def add(x:int, y:int) -> int:
...     return x+y
... 
>>> help(add)
Help on function add:

add(x:int, y:int) -> int

>>> add.__annotations__
{'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

```

# 函数参数有默认值
默认参数的值应该是不可变的对象，比如None、True、False、数字或字符串。 默认参数的值仅仅在函数定义的时候赋值一次，方法实际上也是一个对象，参数就是对象的属性，当默认值是一个可变类型时，每次发生变化时，默认参数的值也会变化。如下所示：
```python
>>> def spam(a, b=[]):
...     b.append(a)
...     print(b)
...     ...
... 
>>> spam(1)
[1]
>>> spam(1)
[1, 1]
>>> spam(1)
[1, 1, 1]

```

# lambda 表达式
匿名函数，主要用于排序和数据reduce等。只接受单个表达式，且表达式的返回值作为函数返回值。
```python
>>> a = lambda x: [i for i in range(x)]
>>> a(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

在lambda表达式生成的函数中，函数中使用的外部变量，不会在生成匿名函数时绑定，只在函数执行时绑定。
```python
>>> funcs = [lambda x: x+n for n in range(5)]
>>> for f in funcs:
... print(f(0))
...
4
4
4
4
4
>>>
```
避免上面错误，需要提供默认值绑定。
```python
>>> funcs = [lambda x, n=n: x+n for n in range(5)]
>>> for f in funcs:
... print(f(0))
...
0
1
2
3
4
>>>
```

# partial()
模块的工具类 `from functools import partial`
```python
>>> from functools import partial
>>> def add(a, b, c):
...     return a+b+c
... 
>>> add(1,2,3)
6
>>> partial(add, 1, 2)(3)
6
>>> partial(add, c=1, b=2)(3)
6

```

# 闭包
简单来讲，闭包就是一个函数。闭包最大的特点就是它会记住自身被定义时的环境。
```python
>>> def a(a):
...     def add(x, y):
...         return x+y+a
...     return add
... 
>>> a(1)
<function a.<locals>.add at 0x000002253B067D90>
>>> a(1)(2,3)
6

>>> add = a(1)
>>> add(2,3)
6

```

