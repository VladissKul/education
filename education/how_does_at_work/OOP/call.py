class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):  # вызывается при вызове экемпляра
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Наш экземпляр вызывался {self.counter} раз')

    def average(self):
        return self.summa / self.length


r = Counter()
r()
r()
r(3, 4, 5, 6)
print(r.average())
r()
r()
