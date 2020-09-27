import math
from array import array

"""
Started out basic 
Then we added a constructor from bytes with a classmethod
Then we added formatting as polar coords, using a property for the angle, and the __format__ method
Then we wanted to make the vector hashable. For this we need the attributes to be immutable, and implement __hash__.
"""


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r}'.format(class_name, *self)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __format__(self, fmt=''):
        if fmt.endswith('p'):
            fmt = fmt[:-1]
            coords = abs(self), self.angle
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @classmethod
    def frombytes(cls, source):
        typecode = chr(source[0])
        memv = memoryview(source[1:]).cast(typecode)
        return cls(*memv)

    @property
    def angle(self):
        return math.atan2(self.y, self.x)


v1 = Vector2d(3, 4)
print(format(v1, '.4fp'))
