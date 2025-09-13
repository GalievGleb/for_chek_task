class BankAccount:
    def __init__(self, owner, balance=0 ):
        self.owner = owner
        self. __balance = balance

    def deposit(self, amount):
        """ метод для пополнения баланса """
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Значение должно быть положительным")

    def withdraw(self, amount):
        """ метод для снятия средст """
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Некорректная операция")

    def get_balance(self):
        """ метод для получения текущего баланса """
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self._BankAccount__balance -= amount


my_client = SavingsAccount("Kate", 0)
my_client.deposit(500)
my_client.withdraw(100)
my_client.apply_interest()
print(f"Баланс после всех операций: {my_client.get_balance()}")


