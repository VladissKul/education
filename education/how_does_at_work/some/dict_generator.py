a = {i: i ** 2 for i in range(1, 11)}
print(a)

b = {len(word): word for word in ['hi', 'hello', 'www']}
print(b)

# также можно применять генераторы словарей на основе другого словаря
dict1 = {
    'илоН МаСК': '126',
    'Джефф Безос': '177',
    'Райан госЛинг': '1132',
    'Уоррен баффЕт': '1111',
}
dict2 = {key.title(): int(value) for key, value in dict1.items()}
print(dict2)
