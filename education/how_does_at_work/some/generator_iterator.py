"""
Генератор - коллекция, которую можно проитерировать только один раз

Элементы генератора не хранятся все вместе, а формируются на лету, следовательно сильно экономят память
"""
b = (i ** 2 for i in range(1, 6))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print()


def gen():  # функция генератор
    n = 1
    for i in [12, 13, 14, 15]:
        yield i
        print('*' * n)  # после вывода 12 останавливается и при следующем выводе продолжается с этой строки и так далее
        n += 1


s = gen()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
