"""
Для чего используется slots
1) Ограничивает атрибуты экземпляра, с которыми мы можем работать, при попытке работать с атрибутом, которого нет в
__slots__ выдает ошибку
2) Операции над такими экземплярами делаются гораздо быстрее
3) Памяти такие экземпляры потребляют меньше
"""

from timeit import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_point():
    s = Point(3, 4)
    s.x = 100
    s.x
    del s.x


def make_point_slots():
    s = PointSlots(3, 4)
    s.x = 100
    s.x
    del s.x


print(timeit(make_point))
print(timeit(make_point_slots))
