class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        print('__bool__ call')
        return self.x != 0 or self.y != 0


p1 = Point(1, 2)
p2 = Point(0, 0)
print(bool(p1), bool(p2))
