import random

figures = ['камень', 'ножницы', 'бумага']
player = input('Введите свою фигуру: ').lower()
computer = random.choice(figures)

if player not in figures:
    print('Такой фигуры нет')
else:
    print('Вы выбрали', player)
    print('Компьютер выбрал', computer)
    if player == computer:
        print('Ничья')

    if (player == 'камень' and computer == 'ножницы') or (player == 'ножницы' and computer == 'бумага') \
            or (player == 'бумага' and computer == 'камень'):
        print('Вы победили')

    if (computer == 'камень' and player == 'ножницы') or (computer == 'ножницы' and player == 'бумага') \
            or (computer == 'бумага' and player == 'камень'):
        print('Победил компьютер')
