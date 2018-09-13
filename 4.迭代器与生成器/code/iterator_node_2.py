from collections import UserList


class CustomList(UserList):
    def __iter__(self):
        print('i am function `__iter__()` of class CustomList.')
        return super().__iter__()
    
    def __next__(self):
        print('i am function `__next__()`.')
        return super().__next__()


class Node:
    def __init__(self, value):
        self._value = value
        self._children = CustomList()
    
    def __repr__(self):
        print('i am function `__repr__()`.')
        return 'Node({!r})'.format(self._value)
    
    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
        print('i am function `__iter__()` of class Node.')
        return iter(self._children)


# Example use
if __name__ == '__main__':
    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    # Output Node(1), Node(2)
    for ch in root:
        print(10*'-')
        print(ch)

"""
迭代时，调用 __iter__() 方法返回一个迭代对象，该迭代对象实现 __next__() 方法。
iter(s) 函数调用 s.__iter__() 方法来返回对应的迭代器对象。
输出：
i am function `__iter__()` of class Node.
i am function `__iter__()` of class CustomList.
----------
i am function `__repr__()`.
Node(1)
----------
i am function `__repr__()`.
Node(2)

"""
