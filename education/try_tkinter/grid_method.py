import tkinter

window = tkinter.Tk()
window.title('My first graphics application')  # заголовок
window['bg'] = '#CADABA'  # цвет фона
window.geometry('500x500+200+200')  # указывается размер окна, плюсами указ. отступ в пикселях от верх. лев. угла
window.resizable(True, True)  # возможность изменять размер окна, стандартно стоит True, True
window.minsize(300, 300)  # минимальный возможный размер окна
window.maxsize(1000, 700)  # максимальный возможный размер окна

# button_1 = tkinter.Button(window, text1='hello1')
# button_2 = tkinter.Button(window, text1='hello2')
# button_3 = tkinter.Button(window, text1='hello3')
# button_4 = tkinter.Button(window, text1='hello4')
# button_5 = tkinter.Button(window, text1='hello5')
# button_6 = tkinter.Button(window, text1='hello6')
# button_7 = tkinter.Button(window, text1='hello7')
# button_8 = tkinter.Button(window, text1='hello8')
# button_9 = tkinter.Button(window, text1='hello9')
#
# button_1.grid(row=0, column=0)  # номер столбца и строки
# button_2.grid(row=0, column=1)
# button_3.grid(row=1, column=0)
# button_4.grid(row=1, column=1)
# button_5.grid(row=2, column=0)
# button_6.grid(row=2, column=1)
# button_7.grid(row=3, column=0, columnspan=2)  # сколько колонок будет занимать кнопка по гор.
# button_8.grid(row=4, column=0, columnspan=2, stick='we')    # растягивает кнопку (указывается стороны(-ы) света
# button_9.grid(row=0, column=2, rowspan=5, stick='ns')    # сколько колонок будет занимать кнопка по верт.

window.columnconfigure(0, minsize=100)  # минимальный размер колонки

for i in range(5):      # автоматическое создание кнопок
    for j in range(2):
        tkinter.Button(window, text=f'hello {i} {j}').grid(row=i, column=j)

window.mainloop()
