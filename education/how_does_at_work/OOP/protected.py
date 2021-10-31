class BankAccount:
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)


account1 = BankAccount('Rayan', 10000, 98239923)
account1.print_protected_data()  # допустимо на уровне соглашения, вызов из класса
print(account1._name)  # выводит, но недопустимо по соглашению, вызывается не из класса
print(account1._balance)  # выводит, но недопустимо по соглашению, вызывается не из класса
print(account1._passport)  # выводит, но недопустимо по соглашению, вызывается не из класса
