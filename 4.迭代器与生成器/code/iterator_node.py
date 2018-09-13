class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    
    def __repr__(self):
        print('i am function `__repr__()`.')
        return 'Node({!r})'.format(self._value)
    
    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
        print('i am function `__iter__()`.')
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
输出：
i am function `__iter__()`.
----------
i am function `__repr__()`.
Node(1)
----------
i am function `__repr__()`.
Node(2)
"""
