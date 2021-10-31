class Section:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)  # автоматически вызывается self.__abs__()

    def __abs__(self):
        return abs(self.x2 - self.x1)


w = Section(10, 9)
print(len(w))

z = Section(8, 10)
print(len(z))