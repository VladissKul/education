class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_protected_data(self):  # не инкапсулированный метод
        print(self.__name, self.__balance, self.__passport)

    def __print_protected_dat(self):  # инкапсулированный метод
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Rayan', 10000, 98239923)
account1.print_protected_data()  # допустимо, вызывается из класса
account1.__print_proteced_dat()  # недопустимо, метод вызывается не из класса

print(account1.__name)  # исключение, так как __name у нас private
print(account1.__balance)  # исключение, так как __balance у нас private
print(account1.__passport)  # исключение, так как __passport у нас private
