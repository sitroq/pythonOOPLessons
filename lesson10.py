class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value
    balance = property(fget=get_balance, fset=set_balance)
b = BankAccount('Ivan', 30000)
print(b.get_balance())
b.set_balance(75000)
print(b.get_balance())
g = BankAccount('Ivan', 30000)
g.balance = 79000
print(g.balance)