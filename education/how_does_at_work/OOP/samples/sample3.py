class Stack:  # стек
    def __init__(self):  # создает пустой стек
        self.values = []

    def push(self, item):  # добавляет элемент в стек
        self.values.append(item)

    def pop(self):  # удаляет и возвращает и удаляет последний элемент стека, если он есть, иначе Empty Stack
        if len(self.values) != 0:
            return self.values.pop()
        else:
            print('Empty Stack')

    def peek(self):  # возвращает последний элемент стека, если он есть, иначе Empty Stack
        if len(self.values) != 0:
            return self.values[-1]
        else:
            print('Empty Stack')
            return None

    def is_empty(self):  # возвращает True если стек пуст, иначе False
        return not(bool(self.values))

    def size(self):  # возвращает длину стека
        return len(self.values)


s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2
