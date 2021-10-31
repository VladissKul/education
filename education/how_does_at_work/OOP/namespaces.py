class DepartmentIt:
    PYTHON_DEV = 1
    GO_DEV = 2
    REACT_DEV = 3

    def info(self):  # доступ через экземпляр класса
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info2(self):  # доступ через класс
        print(DepartmentIt.PYTHON_DEV, DepartmentIt.GO_DEV, DepartmentIt.REACT_DEV)

    @property
    def info3(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @classmethod
    def info4(cls):  # доступ через classmethod
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info5():  # доступ через staticmethod
        print(DepartmentIt.PYTHON_DEV, DepartmentIt.GO_DEV, DepartmentIt.REACT_DEV)

    def new_python_ex(self):  # в данном случае увеличивается количество разработчиков в экземпляре класса
        self.PYTHON_DEV += 1

    def new_python_cl(self):  # в данном случае увеличивается количество разработчиков в самом классе
        DepartmentIt.PYTHON_DEV += 1


it = DepartmentIt()
it.info()
it.info2()
it.info3
it.info4()
it.info5()
