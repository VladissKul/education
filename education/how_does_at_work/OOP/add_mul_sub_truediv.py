"""
add(+), mul(*), sub(-), truediv(/)
"""


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):  # автоматически вызывается при сложении экемпляра с чем-либо, если экземпляр слева
        if isinstance(other, BankAccount):  # в случае если складываются два экземпляра класса
            return self.balance + other.balance
        if isinstance(other, (int, float)):  # в случае если складывается с числом
            return self.balance + other
        raise NotImplemented

    def __radd__(self, other):  # автоматически вызывается при сложении экземпляра с чем-либо, если экземпляр слева
        return self + other

    def __mul__(self, other):
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        raise NotImplemented

    def __rmul__(self, other):
        return self * other


acc1 = BankAccount('ivan', 1000)
acc2 = BankAccount('klim', 200)
print(acc1 + 100)  # add
print(100 + acc1)  # radd
print(acc1 + acc2)  # add
print(acc1 * 2)
print(2 * acc1)
print(acc1 * acc2)
