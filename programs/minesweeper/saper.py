import tkinter as tk
from random import shuffle  # рандомно перемешивает коллекцию
from tkinter.messagebox import showinfo, showerror

colors = {
    1: 'blue',
    2: 'green',
    3: '#FF4500',
    4: '#8B0000',
    5: '#9ACD32',
    6: '#DC143C',
    7: '#D2691E',
    8: '#2F4F4F',
}


class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False  # является ли кнопка миной или нет
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self):
        return f'My Button {self.x} {self.y} {self.number} {self.is_mine}'


class MineSweeper:
    win = tk.Tk()
    ROW = 10
    COLUMNS = 10
    MINES = 15
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True

    def __init__(self):  # автоматически запускается при вызове класса
        self.buttons = []
        for i in range(MineSweeper.ROW + 2):  # создание кнопок и размещение их в двумерных списках
            temp = []
            for j in range(MineSweeper.COLUMNS + 2):
                btn = MyButton(MineSweeper.win, x=i, y=j, width=3)
                btn.config(command=lambda button=btn: self.click(button))
                btn.bind("<Button-3>", self.right_click)  # button 3 отвечает за нажати правой кнопки мыши
                temp.append(btn)
            self.buttons.append(temp)

    def right_click(self, event):  # event - обязательный параметр
        if MineSweeper.IS_GAME_OVER:
            return
        cur_btn = event.widget
        if cur_btn['state'] == 'normal':
            cur_btn['state'] = 'disabled'
            cur_btn['text'] = '🚩'
            cur_btn['disabledforeground'] = 'red'
        elif cur_btn['text'] == '🚩':
            cur_btn['text'] = ''
            cur_btn['stage'] = 'normal'

    def click(self, clicked_button: MyButton):  # аннотация, то есть мы подасказываем, с каким типом объекта будем раб.

        if MineSweeper.IS_GAME_OVER:  # предотвращает показ содержимого кнопок после поражения
            return

        if MineSweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_button.number)
            self.count_mines_in_buttons()
            self.print_buttons()
            MineSweeper.IS_FIRST_CLICK = False

        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
            clicked_button.is_open = True
            MineSweeper.IS_GAME_OVER = True
            showinfo('Game over', 'Вы проиграли!')
            for i in range(1, MineSweeper.ROW + 1):
                for j in range(1, MineSweeper.COLUMNS + 1):
                    btn = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.breadth_first_search(clicked_button)
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)  # оставляет кнопку нажатой после первого нажатия

    def breadth_first_search(self, btn: MyButton):
        queue = [btn]
        while queue:
            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disabled')
            cur_btn.config(relief=tk.SUNKEN)  # оставляет кнопку нажатой после первого нажатия
            if cur_btn.count_bomb == 0:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:  # цикл ищет соседей по вертикали и горизонтали
                    for dy in [-1, 0, 1]:
                        # if not abs(dx - dy) == 1:
                        #     continue
                        next_btn = self.buttons[x + dx][y + dy]
                        if not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.ROW and \
                                1 <= next_btn.y <= MineSweeper.COLUMNS and next_btn not in queue:
                            queue.append(next_btn)

    def reload(self):
        [child.destroy() for child in self.win.winfo_children()]  # как бы "разрушает" все кнопки
        self.__init__()  # заново создает кнопки
        self.create_widgets()  # отрисовывает кнопки
        MineSweeper.IS_FIRST_CLICK = True
        MineSweeper.IS_GAME_OVER = False

    def create_settings_win(self):
        win_settings = tk.Toplevel(self.win)
        win_settings.wm_title('Настройки')

        tk.Label(win_settings, text='Количество строк:').grid(row=0, column=0)
        row_entry = tk.Entry(win_settings)
        row_entry.insert(0, MineSweeper.ROW)
        row_entry.grid(row=0, column=1, padx=20, pady=20)

        tk.Label(win_settings, text='Количество столбцов:').grid(row=1, column=0)
        column_entry = tk.Entry(win_settings)
        column_entry.insert(0, MineSweeper.COLUMNS)
        column_entry.grid(row=1, column=1, padx=20, pady=20)

        tk.Label(win_settings, text='Количество мин:').grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.insert(0, MineSweeper.MINES)
        mines_entry.grid(row=2, column=1, padx=20, pady=20)

        save_btn = tk.Button(win_settings, text='Применить',
                             command=lambda: self.change_settings(row_entry, column_entry, mines_entry))
        save_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

    def change_settings(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry):
        try:
            int(row.get()), int(column.get()), int(mines.get())
        except ValueError:
            showerror('Ошибка', 'Вы ввели неправильное значение!')
            return
        MineSweeper.ROW = int(row.get())  # int ставится для того чтобы передавалось число, а не строка
        MineSweeper.COLUMNS = int(column.get())
        MineSweeper.MINES = int(mines.get())
        self.reload()  # используется чтобы перезапустить игру после применения настроек

    def create_widgets(self):

        menubar = tk.Menu(self.win)
        self.win.config(menu=menubar)

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label='Играть', command=self.reload)
        settings_menu.add_command(label='Настройки', command=self.create_settings_win)
        settings_menu.add_command(label='Выход', command=self.win.destroy)  # закрывает окно
        menubar.add_cascade(label='Файл', menu=settings_menu)

        count = 1
        for i in range(1, MineSweeper.ROW + 1):  # размещение кнопок в окне
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j, stick='NSEW')
                count += 1

        for i in range(1, MineSweeper.ROW + 1):
            tk.Grid.rowconfigure(self.win, i, weight=1)  # задает пропорциональный размер ряда

        for i in range(1, MineSweeper.COLUMNS + 1):
            tk.Grid.columnconfigure(self.win, i, weight=1)  # задает пропорциональный размер столбца

    def open_all_buttons(self):
        for i in range(MineSweeper.ROW + 2):  # размещение кнопок в окне
            for j in range(MineSweeper.COLUMNS + 2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', background='red', disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg=color)

    def start(self):
        self.create_widgets()
        # self.open_all_buttons()
        MineSweeper.win.mainloop()

    def print_buttons(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    def insert_mines(self, number: int):
        index_mines = self.get_mines_places(number)
        print(index_mines)
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                if btn.number in index_mines:
                    btn.is_mine = True

    def count_mines_in_buttons(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMNS + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:  # с помощью этих циклов мы получаем все соседние клетки
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i + row_dx][j + col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    @staticmethod
    def get_mines_places(exclude_number: int):
        indexes = list(range(MineSweeper.ROW * MineSweeper.COLUMNS + 1))  # индексы, в клетках которых будут мины
        print(f'Искючаем кнопку номер {exclude_number}')
        indexes.remove(exclude_number)
        shuffle(indexes)  # перемешивает эти индексы
        return indexes[:MineSweeper.MINES]  # возвращает индексы от начала до указанного количества мин


game = MineSweeper()
game.start()
