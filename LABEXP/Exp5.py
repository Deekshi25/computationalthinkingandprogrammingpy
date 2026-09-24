from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, number: str, balance: float):
        self.number = number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class SavingsAccount(Account):
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount


class CurrentAccount(Account):
    def withdraw(self, amount: float) -> None:
        self.balance -= amount


a = SavingsAccount("S101", 5000.0)
a.deposit(1000)
a.withdraw(2000)

print("Account:", a.number)
print("Balance:", a.balance)
