class Point:
    list_points = []

    def __init__(self, coord_x, coord_y):
        self.move_to(coord_x, coord_y)  # можно вызывать методы
        Point.list_points.append(self)  # при каждом создании новой точки она будет добавляться в список

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)  # можно вызвать методы

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):  # проверка принадлежности к классу Point
            raise ValueError('Аргумент должен принадлежать классу Точка')
        else:
            return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** 0.5  # Теорема Пифагора


p1 = Point(6, 0)
p2 = Point(0, 8)
print(p1.calc_distance(p2))
print(p2.calc_distance(p1))
print(list(Point.list_points))
