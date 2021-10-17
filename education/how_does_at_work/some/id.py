x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))  # разные id

print('-' * 100)

x = [1, 2, 3]
y = x
print(id(x), id(y))  # одинаковые id потому что x и y ссылаются на один и тот же объект
print(x is y)
print(y is x)

print('-' * 100)

a = [1, 2, 3]
b = a
a.append(4)  # изменяются обе переменные, так как они ссылаются на один и тот же объект
print(a)
print(b)