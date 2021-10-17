a = [-1, 2, 3, -4, -100]
print(list(map(abs, a)))


def f(x):
    return x ** 2


print(list(map(f, a)))  # также можно передавать собственные функции

b = ['you', 'me', 'he', 'they']
print(list(map(str.upper, b)))  # также можно передавать методы

s = list(map(int, input().split()))  # используется для ввода
print(s)
