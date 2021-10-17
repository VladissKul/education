import random

a = [random.randint(-100, 100) for i in range(10)]  # список из 10 рандомных чисел
print(a)
a = [elem for elem in a if elem % 2 == 0]  # отбираются только четные элементы списка
print(a)

print([(i, j) for i in [1, 2, 3] for j in 'abc'])  # вложенные циклы в генераторах списков

b = [[random.randint(-1000, 1000) for i in range(3)] for j in range(4)]  # создание двумерного массива
for i in b:
    print(i)

