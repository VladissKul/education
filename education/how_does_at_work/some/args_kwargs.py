def summa(*args):  # передается любое количество аргументов
    s = 0
    for i in args:
        s += i
    return s


print(summa(1, 2, 3, 4, 5))


def f(**kwargs):  # передается любое количество именованных аргументов
    for k, v in kwargs.items():
        print(k, v)


f(a=2, b=3, string='hello')


def func(*args, **kwargs):
    print(args, kwargs)


func(5, 4, 3, 2, 5, a=3, b=4, c='work', d=True)
