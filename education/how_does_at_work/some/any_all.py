a = b = c = d = True
if all((a, b, c, d)):  # если все элементы итерируемой последовательности можно привести к буллевскому типу True
    print('all true')
if any((a, b, c, d)):
    print('all true')  # если хотя бы один элемент может быть приведен к булевскому типу True
