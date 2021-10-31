class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура, я отучился на доктора')

    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень')


class Builder:
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Ура, я отучился на строителя')

    def can_build(self):
        print('Я строитель, я умею строить')


class Person(Builder, Doctor):
    def __init__(self, rank, degree):
        super().graduate()  # вызовется метод класса Builder, так как он стоит на первом месте
        super().__init__(rank)  # вызовется метод класса Builder, так как он стоит на первом месте
        Doctor.__init__(self, degree)  # метод класса Doctor придется вызвыать вручную, так как super() тут не работает

    def __str__(self):
        return f'Person {self.rank} {self.degree}'


p = Person(5, 'spec')
print(p)
