import tkinter


def select_all():  # выбирает все флажки
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():  # снимает все флажки
    for check in [over_18, commercial, follow]:
        check.deselect()


def switch_all():  # меняет все флажки на противоположные
    for check in [over_18, commercial, follow]:
        check.toggle()


def show():  # показывает зачение флажков
    print('флажок 18', over_18_value.get())
    print('реклама', commercial_value.get())


window = tkinter.Tk()
window.geometry('500x500+200+200')
window.title('My first graphics application')

over_18_value = tkinter.StringVar()
over_18_value.set('No')  # устанавливает изначальное положение флажка
commercial_value = tkinter.IntVar()

over_18 = tkinter.Checkbutton(window, text='Вам исполнилось 18 лет?',
                              variable=over_18_value,  # привязка переменной
                              offvalue='No',  # если флажок не выбран
                              onvalue='Yes')  # если флажок выбран
commercial = tkinter.Checkbutton(window, text='Хотите получать рекламу?',
                                 variable=commercial_value,  # привязка переменной
                                 offvalue=0,  # если флажок не выбран
                                 onvalue=1)  # если флажок выбран
follow = tkinter.Checkbutton(window, text='Хотите подписаться на канал?', indicatoron=0)
# indicatoron превращает флажок в кнопку, похожую по свойствам на флажок
over_18.pack()
commercial.pack()
follow.pack()

tkinter.Button(window, text='Select all', command=select_all).pack()
tkinter.Button(window, text='Deselect all', command=deselect_all).pack()
tkinter.Button(window, text='Switch all', command=switch_all).pack()
tkinter.Button(window, text='Show', command=show).pack()

window.mainloop()
