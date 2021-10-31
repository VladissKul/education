"""
slots дочернего класса расширяет имена находящиеся в slots родительского класса
"""


class Rectangle:
    __slots__ = ('__width', 'height')

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value


class Square(Rectangle):
    __slots__ = 'color'

    def __init__(self, width, height, color):
        super().__init__(width, height)
        self.color = color


s = Square(4, 4, 'red')
print(s.width)
print(s.height)
print(s.color)
