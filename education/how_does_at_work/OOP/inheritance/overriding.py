class Person:

    special = 'Yes'  # Person, Doctor

    def __init__(self, name):  # Person, Doctor
        self.name = name

    def breathe(self):  # Person
        print('Человек дышит')

    def walk(self):  # Person, Doctor
        print('Человек идет')

    def sleep(self):  # Person
        print('Человек спит')

    def combo(self):  # Person, Doctor
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):  # Person
        return f'Person {self.name}'


class Doctor(Person):
    def breathe(self):  # Doctor
        print('Доктор дышит')

    def sleep(self):  # Doctor
        print('Доктор спит')

    def __str__(self):  # Doctor
        return f'Доктор {self.name}'


d = Doctor('John')
p = Person('Adam')
d.combo()
print(d.special)