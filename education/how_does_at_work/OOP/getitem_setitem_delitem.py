class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __str__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Индекс за границами коллекции')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError('Индекс за границами коллекции')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами коллекции')


v1 = Vector(1, 2, 3, 4, 9, 100)
print(v1[2])
v1[3] = 1000
print(v1)
del v1[4]
print(v1)