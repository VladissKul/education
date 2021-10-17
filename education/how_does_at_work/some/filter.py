a = [14, 14, 0, '', 'hello', ' ', 133, [], [1, 2, 3]]
print(list(filter(bool, a)))  # возвращает только ненулевые элементы

b = ['world', 'apple', 'cat', 'map', 'popit']
print(list(filter(lambda x: len(x) > 3, b)))  # возвращает только те элементы, длина которых больше 3

c = 'lajdslfjlaj38834ujljdalsf98329jklfjasf'
print(list(filter(str.isdigit, c)))  # возвращает только цифры
