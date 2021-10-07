import tkinter
from tkinter import messagebox


def add_digit(digit):  # добавление цифры
    value = calc.get()  # получить значение из calc
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tkinter.NORMAL  # разблокировка entry, в последующем коде значение то же
    calc.delete(0, tkinter.END)
    calc.insert(0, value + digit)
    calc['state'] = tkinter.DISABLED  # блокировка entry, в последующем коде значение то же


def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/+' in value:
        calculate()
        value = calc.get()
    calc['state'] = tkinter.NORMAL
    calc.delete(0, tkinter.END)
    calc.insert(0, value + operation)
    calc['state'] = tkinter.DISABLED


def calculate():
    """Подсчитывает значение в строке"""
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]  # 7 * 7: value = 7*; value[:-1] = 7
    calc['state'] = tkinter.NORMAL
    calc.delete(0, tkinter.END)
    try:
        calc.insert(0, eval(value))  # eval интрепретирует строку и выводит результат
    except (NameError, SyntaxError):
        messagebox.showinfo('Ошибка', 'Нужно вводить только цифры')  # выводит сообще в окне
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Ошибка', 'Деление на ноль невозможно')
        calc.insert(0, 0)
    calc['state'] = tkinter.DISABLED


def clear():
    calc['state'] = tkinter.NORMAL
    calc.delete(0, tkinter.END)
    calc.insert(0, '0')
    calc['state'] = tkinter.DISABLED


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():  # при нажатии на цифру
        add_digit(event.char)
    elif event.char in '+-*/':  # при нажатии на операцию
        add_operation(event.char)
    elif event.char == '\r':  # при нажатии на enter
        calculate()
    elif event.char == '\x08':  # при нажатии на backspace
        clear()
    elif event.char == '.':  # при нажатии на del на нампаде
        clear()


def make_calc_button(operation):
    return tkinter.Button(text=operation, bd=5, font=('Arial', 15), fg='red',
                          command=calculate)


def make_clear_button(operation):
    return tkinter.Button(text=operation, bd=5, font=('Arial', 15), fg='red',
                          command=clear)


def make_digit_button(digit):
    return tkinter.Button(text=digit, bd=5, font=('Arial', 15),
                          command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tkinter.Button(text=operation, bd=5, font=('Arial', 15), fg='red',
                          command=lambda: add_operation(operation))


win = tkinter.Tk()
win.geometry('240x270+100+200')  # указывается размер окна, плюсами указ. отступ в пикселях от верх. лев. угла
win.title('Калькулятор')  # заголовок
win['bg'] = '#C0C0C0'  # цвет фона
win.resizable(True, True)  # возможность изменять размер окна, стандартно стоит True, True
win.minsize(240, 240)  # минимальный возможный размер окна
win.maxsize(1000, 700)  # максимальный возможный размер окна

win.bind('<Key>', press_key)  # обрабатывает нажатие на клавиатуру и вызывает соответствующую функцию, тут press_key

calc = tkinter.Entry(win, justify=tkinter.RIGHT, font=('Arial', 15), width=15)
# justify исп. чтобы прижимать текст к указанной стороне
calc.insert(0, '0')  # это нужно чтобы отображался 0 при пустой строке
calc['state'] = tkinter.DISABLED  # выделить серым цветом и сделать его невосприимчивым к действию
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)
make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('c').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
