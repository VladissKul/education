"""Метод get() возвращает значение в виде строки, то есть при передаче числа 5 он будет возвращать строку '5' """
import tkinter
from tkinter import ttk  # импортируется combobox только из ttk

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def show_day():
    print(combo.get())


window = tkinter.Tk()
window.geometry('500x500+200+200')
window.title('My first graphics application')

combo = ttk.Combobox(window, values=weekdays)  # values передает виджету компоненты
combo.current(0)  # передает изначальное значение combobox (передается индекс)
combo.pack()

ttk.Button(window, text='Show day', command=show_day).pack()

window.mainloop()
