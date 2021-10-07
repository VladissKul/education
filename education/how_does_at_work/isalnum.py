"""
isalnum() возвращает True если строка состоит только из букв и цифр
"""


def alphanumeric(password):
    return password.isalnum()


print(alphanumeric('aldsjflj'))
print(alphanumeric('ljalsdjfl aljka j '))
