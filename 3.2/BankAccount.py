class BankAccount:
    def __init__(self, owner, balance=100):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        try:
            if amount > 0:
                self._balance += amount
                print(f"Пополнение на {amount}, прошло успешно!")
            else:
                raise ValueError(f"Некорректная сумма пополнения {amount}")
        except ValueError as error:
            print(f"Ошибка: {error}")

    def withdraw(self, amount):
        try:
            if amount > 0 and amount <= self._balance:
                self._balance -= amount
                print(f"Снятие {amount}, прошло успешно!")
            else:
                raise ValueError(f"Невозможно снять {amount} - Недостаточно средств на счету.")
        except ValueError as error:
            print(f"Ошибка: {error}")

    def get_balance(self):
        return self._balance

class SavingAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Начисленные проценты - {interest}. {self._balance} - Остаток на счету")

class CheckingAccount(BankAccount):

    def withdraw(self, amount):
        self._balance -= amount
        print(f"Снятие {amount}, прошло успешно!")

"""account = SavingAccount("Иван Иванов")
account.deposit(500)
account.withdraw(100)
account.apply_interest()"""

#Тест
def test_check_balance(dep=100):

    account = SavingAccount("Anton", 0)
    account.deposit(dep)
    account.apply_interest()
    account.withdraw(200)
    balance = account.get_balance()
    assert balance > 0
test_check_balance()