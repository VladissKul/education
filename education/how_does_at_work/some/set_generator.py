"""
Множество исключает дубликаты

Элементами можества могут быть только неименяемые объекты
"""
my_set = {i for i in [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 1] if i > 4}
print(my_set)

my_set2 = {i + j for i in 'aba' for j in 'cde'}  # исключаются дубли
print(my_set2)