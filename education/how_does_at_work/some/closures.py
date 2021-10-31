def main_func(name):
    def inner_func():
        print('hello my friend', name)

    return inner_func  # нет скобочек, то есть нет самого вызова


y = main_func('Jim')
y()


def counter():
    count = 0  # называется свободная переменная

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


r = counter()  # 0
print(r())  # 1
print(r())  # 2
print(r())  # 3
print(r())  # 4