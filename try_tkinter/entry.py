import tkinter

window = tkinter.Tk()
window.title('My first graphics application')  # заголовок
window['bg'] = '#CADABA'  # цвет фона
window.geometry('500x500+200+200')  # указывается размер окна, плюсами указ. отступ в пикселях от верх. лев. угла
window.resizable(True, True)  # возможность изменять размер окна, стандартно стоит True, True
window.minsize(300, 300)  # минимальный возможный размер окна
window.maxsize(1000, 700)  # максимальный возможный размер окна

name = tkinter.Entry(window)
name.grid(row=0, column=1)

password = tkinter.Entry(window, show='*')
password.grid(row=1, column=1)

tkinter.Label(window, text='Имя').grid(row=0, column=0, stick='w')
tkinter.Label(window, text='Пароль').grid(row=1, column=0, stick='w')


def get_entry():
    value = name.get()  # получить значение из name
    if value:
        print(value)
    else:
        print('Nope')


def delete_entry():
    name.delete(0, tkinter.END)  # удаляет элементы name (с нулевого индекса и до конца)


def submit():
    print(name.get())
    print(password.get())
    delete_entry()      # удаляет поле
    password.delete(0, tkinter.END)     # удаляет поле


tkinter.Button(window, text='get', command=get_entry).grid(row=3, column=0,stick='we')
tkinter.Button(window, text='delete', command=delete_entry).grid(row=3, column=1,stick='we')
tkinter.Button(window, text='insert', command=lambda: name.insert(0, 'hello')).grid(row=3, column=2,stick='we')
# вставляет строку в место с указанным индексом
tkinter.Button(window, text='submit', command=submit).grid(row=3, column=3)

window.grid_columnconfigure(0, minsize=100)
window.grid_columnconfigure(1, minsize=100)

window.mainloop()
