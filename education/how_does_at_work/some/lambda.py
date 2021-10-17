r = lambda x: x ** 2
print(r(4))

h = lambda: 'hello'  # можно использовать без аргументов
print(h())

c = lambda x: 'positive' if x > 0 else 'negative'  # пример с if else
print(c(3), c(-3))
