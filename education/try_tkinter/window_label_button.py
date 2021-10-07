import tkinter

window = tkinter.Tk()  # можно считать, что window как полноценное окно приложения

window.title('My first graphics application')  # заголовок
window['bg'] = '#CADABA'  # цвет фона
window.geometry('500x500+200+200')  # указывается размер окна, плюсами указ. отступ в пикселях от верх. лев. угла
window.resizable(True, True)  # возможность изменять размер окна, стандартно стоит True, True
window.minsize(300, 300)  # минимальный возможный размер окна
window.maxsize(1000, 700)  # максимальный возможный размер окна

photo = tkinter.PhotoImage(file='icon.png')  # загрузка нужной фотографии
window.iconphoto(False, photo)  # непосредственно изменяем иконку

label_1 = tkinter.Label(window, text='Hello!',  # создание текстового поля (первый параметр - нужное окно)
                        bg='white',
                        fg='red',
                        font=('Arial', 20, 'bold'),  # шрифт
                        # padx=15,    # отступ внутри label по х в пикселях
                        # pady=15,    # отступ внутри label по у в пикселях
                        width=7,  # ширина (указывается в количестве символов, которые можно уместить)
                        height=3,  # высота (указывется в количестве символов, которые можно уместить)
                        anchor='sw',  # расположение текста внутри label в кавычках указывается сторона(-ы) света
                        relief=tkinter.RAISED,  # границы label
                        bd=4,  # ширина границ
                        justify=tkinter.LEFT  # выравниваение текста, в данном случае по левой стороне
                        )
label_1.pack()


def say_hello():
    print('hello')


def new_label():  # данная функция создает новый label
    label = tkinter.Label(window, text='new')
    label.pack()


count = 0


def counter():
    global count
    count += 1
    button_4['text'] = f'Счетчик: {count}'


button_1 = tkinter.Button(window, text='Hello',
                          command=say_hello,  # функция, которая выполнится при нажатии кнопки
                          state=tkinter.DISABLED  # блокирует кнопку
                          )

button_2 = tkinter.Button(window, text='create new label',
                          command=new_label  # функция, которая выполняется при нажатии кнопки
                          )

button_3 = tkinter.Button(window, text='new label with lambda',
                          command=lambda: tkinter.Label(window, text='new label').pack()
                          )  # lambda функция также выполняется при нажатии кнопки

button_4 = tkinter.Button(window, text=f'Счетчик: {count}',
                          command=counter,
                          activebackground='blue'  # какого цвета становится кнопка при нажатии
                          )
button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()

window.mainloop()
