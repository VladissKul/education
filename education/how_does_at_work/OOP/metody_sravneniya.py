"""
__eq__ отвечает за ==
__ne__ отвечает за !=
__lt__ отвечает за <
__le__ отвечает за <=
__gt__ отвечает за >
__ge__ отвечает за >=
Реализованных в классе методов достаточно, чтобы выполнять все возможные операции сравнения, так как при вызове
несуществуеющего метода соответствующей операции сравнения, вызывается обратная ей, которая у нас реализована
"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__ call')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('__lt__ call')
        if isinstance(other, Rectangle):
            return self.area < other.area
        if isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other


a = Rectangle(2, 4)
b = Rectangle(2, 4)
c = Rectangle(5, 10)
print(a == b)
print(a != b)
print(a < c)
print(a > c)
print(a >= c)
print(a <= c)
