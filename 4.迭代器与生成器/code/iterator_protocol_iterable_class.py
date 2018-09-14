"""
Python的迭代协议要求一个 __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
但是，实现这些通常会比较繁琐。 下面我们演示下这种方式，如何使用一个关联迭代器类重新实现 depth_first() 方法：
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        """
        遍历开始时，_children_iter 与 _child_iter 为None，_node 为根节点；
        
        _children_iter 表示根节点的子节点迭代器；
            该值为None时，返回根节点，并获取根节点的子节点迭代器赋值给它。
            该值不为None时，检查_child_iter是否为None。当_child_iter为None时，迭代（next(s)）该值取值，
                否则，以_child_iter作为根节点进行新的迭代；
        _child_iter 表示作为根节点进行迭代的子节点的迭代器；
        """
        # Return myself if just started; create an iterator for children
        # print('__next__()', self._node, self._children_iter, self._child_iter)
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            # print('创建子节点的迭代器', self._children_iter, '\n\t 返回节点', self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                # print('\t 返回节点', nextchild)
                return nextchild
            except StopIteration:
                self._child_iter = None
                # print(self._child_iter, '子节点迭代结束')
                return next(self)
        # Advance to the next child and start its iteration
        else:
            child = next(self._children_iter)
            self._child_iter = child.depth_first()
            # print(child, '调用其depth_first()方法')
            return next(self)


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    # for ch in root.depth_first():
    #     # print(ch)
    #     print()
    #     # pass

    for ch in DepthFirstIterator(root):
        print(ch)
        # print()
        # pass

    # while True:
    #     try:
    #         next(DepthFirstIterator(root))
    #     except StopIteration:
    #         break

"""
输出
Node(0)
Node(1)
Node(3)
Node(4)
Node(2)
Node(5)
"""
