"""
Если после except не указывать никакого конкретоного исключения, то будут обрабатываться все исключения
try можно использовать со множеством конструкций except
Также допускается конструкция в которой есть только try и finally
"""

try:  # блок кода, который нужно исполнить
    1 / 0
except (ZeroDivisionError, ValueError):  # можно указать несколько в кортеже, а можно сделать много разных exception
    print('error')
except KeyError as err:  # можно дать псевдоним исключению, появляется переменная, которую можно использовать
    print('keyerror')
else:  # отрабатывает только тогда, когда в try не было исключения
    print('ошибки не было')
finally:  # отрабатывает в любом случае
    print('конец')