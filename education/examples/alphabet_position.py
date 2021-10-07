"""
Данная функция преобразует строку текста в строку чисел, соответствующих позициям букв в латинском алфавите
"""


def alphabet_position(text):
    return ' '.join([str(int(ord(i) - 96)) for i in text.lower() if 96 < ord(i) < 123])


print(alphabet_position("The sunset sets at twelve o' clock."))
