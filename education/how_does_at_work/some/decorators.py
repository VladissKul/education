"""
Декоратор - это функция, которая принмает другую функцию и возвращает функцию
"""


def decorator(func):
    def inner(*args, **kwargs):
        print('start decorator')
        func(*args, **kwargs)
        print('finish decorator')

    return inner


@decorator  # то же самое что и say = header(say)
def say(name, surname, age):
    print('hello', name, surname, age)


say('Vasya', 'Ivanov', 30)
