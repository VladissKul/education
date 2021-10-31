class Person:  # parent
    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')


class Doctor(Person):  # subclass
    def can_cure(self):
        print('Я могу лечить')


class Architect(Person):  # subclass
    def can_build(self):
        print('Я могу строить')


class MyList(list):  # можно наследовать втроенные типы, у экземпляров будут доступны все методы наследуемого типа
    pass
