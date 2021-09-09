import tkinter

levels = {
    1: 'Easy',
    2: 'Normal',
    3: 'Hard',
}


def select_level():
    level = level_var.get()  # получаем значение переменной\
    level_text.set(f'Вы выбрали {level} уровень')  # когда будет выбираться кнопка, будет изм. перем. level_text
    print(levels[level])


window = tkinter.Tk()
window.geometry('500x500+200+200')
window.title('My first graphics application')

level_var = tkinter.IntVar()
nation_var = tkinter.IntVar()
level_text = tkinter.StringVar()

tkinter.Label(window, text='Выберите уровень сложности:').pack()
for level in sorted(levels):
    tkinter.Radiobutton(window, text=levels[level], variable=level_var, value=level, command=select_level).pack()
# variable привязывает к определенной переменной
tkinter.Label(window, textvariable=level_text).pack()

window.mainloop()
