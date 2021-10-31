"""
__repr__ - представление объекта, если вы просто введёте его название в консоль. Оно ближе к машине.
Полезно использовать для отладки, чтобы узнать информацию об объекте.
__str__ - выводится при использовании метода print с объектом. Строковое представление объекта, дружелюбное для человека
"""


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'human name is {self.name}'

    def __repr__(self):
        return f'object name is {self.name}'


human1 = User('Jimmy')

print(human1)
