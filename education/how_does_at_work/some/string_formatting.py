name = 'Иван'
mid_name = 'Пупкин'
balance = 1000

text1 = 'Дорогой ' + name + ' ' + mid_name + ', баланс вашего счета составляет ' + str(balance) # хуета, а не метод
print(text1)

text2 = 'Дорогой {0} {1}, баланс вашего счета составляет {2}'.format(name, mid_name, balance)
print(text2)

text3 = 'Дорогой {name} {mid_name}, баланс вашего счета составляет {balance}'.format(name=name, mid_name=mid_name, balance=balance)
print(text3)

text4 = f'Дорогой {name.upper()} {mid_name.upper()}, баланс вашего счета составляет {balance * 2}'
print(text4)
# в f-строках можно использовать различные методы, операции, функции, собственные функции и так далее

text5 = 'Дорогой %s %s, баланс вашего счета составляет %s' % ('Иван', 'Пупкин', '1000')
print(text5)

