class Cat():
    def __init__(self, name, age, color):  # автоматически выполняется при запуске программы
        self.name = name
        self.age = age
        self.color = color


tom = Cat('Tom', 2, 'blue')
print(tom.name, tom.age, tom.color)