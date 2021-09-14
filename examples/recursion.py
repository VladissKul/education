"""
В данном примере функция вызывается рекурсивно в строке 9
"""
def digital_root(n):
    summa = 0
    for i in str(n):
        summa += int(i)
    if summa > 9:
        return digital_root(summa)  # рекурсия
    else:
        return summa


print(digital_root(493193))
