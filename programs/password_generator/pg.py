import random

alphabet = '1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

password = ''

for i in range(int(input('Введите кол-во символов в пароле: '))):
    password += random.choice(alphabet)

print(password)
