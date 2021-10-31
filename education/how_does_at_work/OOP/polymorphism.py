"""
Метод get_area и перегрузка __str__ будет работать по-разному, в зависимости от того, к экземпляру
какого класса он применяется
"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle {self.a} x {self.b} = {self.a * self.b}'

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square {self.a} ** 2 = {self.a ** 2}'

    def get_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle s = {3.14 * self.r ** 2}'

    def get_area(self):
        return 3.14 * self.r ** 2


a = Rectangle(4, 9)
b = Square(4)
c = Circle(5)
print(a.get_area(), b.get_area(), c.get_area())

figures = [a, b, c]
for figure in figures:
    print(figure)
    print(figure.get_area())
