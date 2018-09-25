import math


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        # print('Done getter.')
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        print('Done setter.')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        # print('Done setter.')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    person = Person('Guido')    # Done setter.
    print(person.first_name, person._first_name)    # Guido Guido

    person.first_name = 'Tom'   # Done setter.
    print(person.first_name, person._first_name)    # Tom Tom

    try:
        person = Person(1)      # Raise TypeError: Expected a string
    except Exception as e:
        print(e, e.args)                # Expected a string ('Expected a string',)
    
    p = Person2('Jack')
    print(p.name, p._first_name)    # Jack Jack

