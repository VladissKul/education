from typing import Dict, List


def add_numbers(a: int, b: int) -> int:
    return a + b


first: int = 100
second: int = 200
print(add_numbers(first, second))
print(add_numbers.__annotations__)  # просмотр аннотаций функции

a: int | float = 10  # если нужно, чтобы переменная могла быть аннотирована разными типами

primes: list[int] = [1, 2, 3]  # все элементы коллекции типа int

d: dict[str, int] = {'a': 100, 'b': 200}  # ключи типа str, значения типа int


def list_upper(lst: list[str]):
    for elem in lst:
        return elem.upper()  # благодаря аннотированию присутствуют методы строк
