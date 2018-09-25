"""

__repr__()

__str__()

__eq__()
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

    def __eq__(self, other):
        if hasattr(other, 'x') and hasattr(other, 'y'):
            return self.y == getattr(other, 'y') and self.x == getattr(other, 'x')


if __name__ == '__main__':
    pair = Pair(1, 2)
    print(pair)     # (1, 2)
    print(str(pair))     # (1, 2)
    print('p is {0!r}'.format(pair))     # p is Pair(1, 2)
    print('p is {0}'.format(pair))      # p is (1, 2)

    print(eval(repr(pair)))     # (1, 2)
    print(eval(repr(pair)) == pair)     # True
    print(Pair(1, 2) == pair)     # True
    print(Pair(3, 4) == pair)     # False
