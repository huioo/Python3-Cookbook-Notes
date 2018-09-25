class A:
    """
    任何以单下划线 “_” 开头的名字都应该是内部实现
    """
    def __init__(self):
        self.public = 1     # 公共属性
        self._internal = 2     # 内部属性
        self.__private = 3     # 私有属性
    
    def public_method(self):
        """ 公共方法 """
        print('public method of {!r}'.format(self))
        print('function name of {!r} is {!r}'.format(self.__class__.__name__, self.public_method.__name__))
    
    def _internal_method(self):
        print('internal method of {}'.format(self))
        print('function name of {} is {}'.format(self.__class__.__name__, self._internal_method.__name__))

    def __private_method(self):
        print('private method of {!r}'.format(self))
        print('function name of {!r} is {}'.format(self.__class__.__name__, self.__private_method.__name__))


class B(A):
    def __init__(self):
        self.public = 11     # 公共属性
        self._internal = 12     # 内部属性
        self.__private = 13     # 私有属性

    # Does not override B.__private_method()
    def __private_method(self):
        print('private method of {!r}'.format(self))
        print('function name of {!r} is {}'.format(self.__class__.__name__, self.__private_method.__name__))


if __name__ == '__main__':
    a = A()
    print('public attribute:', a.public)
    print('internal attribute:', a._internal)
    print('private attribute:', a._A__private)
    print(20*'*')
    a.public_method()
    print(20*'*')
    a._internal_method()
    print(20*'*')
    a._A__private_method()
    print(20*'*')
    b = B()
    print('public attribute:', b.public)
    print('internal attribute:', b._internal)
    print('private attribute:', b._B__private)
    print(20*'*')
    b.public_method()
    print(20*'*')
    b._internal_method()
    print(20*'*')
    b._A__private_method()
    print(20*'*')
    b._B__private_method()

