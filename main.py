class BanckAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.__print_private_data()
    def print_protected_data(self):
        print(self._name, self._balance, self._passport)
    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BanckAccount('Bob', 100000, 123456)
account1.print_public_data()
print(dir(account1))
print(account1._BanckAccount__balance)
# account1.print_protected_data()
print(account1.__name)
print(account1.__balance)
print(account1.__passport)