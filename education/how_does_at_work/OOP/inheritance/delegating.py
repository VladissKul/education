"""
Делегирование - способ, при котором в дочернем классе мы можем вызвать метод родительского класса
"""


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Person {self.name} {self.surname}'

    def info(self):
        print('Parent class')
        print(self)


class Doctor(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)  # вызывается метод родительского класса
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname}'


p = Person('Ivan', 'Ivanov')
d = Doctor('Petr', 'Petrov', 25)
p.info()
d.info()
