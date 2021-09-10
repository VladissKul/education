'''
как работает эта залупа
короче блять len(alphabet) = 34
берем букву 'ю', самую уебищную
ее индекс бля равен 32
32 плюс шаг 2 = 34
34 % len(alphabet) = 34 % 34 = 0
следовательно, бля, 'ю' заменяется на знак пробела
гнилая ебатория, гнилое крем брюле
'''
alphabet = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
message = input('Введите текст: ')
step = int(input('Введите шаг:'))


def encryption(result=''):  # шифровка
    for i in message:
        result += alphabet[(alphabet.index(i) + step) % len(alphabet)]
    return result


def decryption(result=''):  # расшифровка
    for i in message:
        result += alphabet[(alphabet.index(i) - step) % len(alphabet)]
    return result


q = int(input('1 - шифровка, 2 - расшифровка\n'))
if q == 1:
    print(encryption())
else:
    print(decryption())
