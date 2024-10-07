"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относятся непосредственно к кредитам в отдельный класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == "__main__":
    user_1 = BankAccount("Винни Пух", 1234.5)
    print(user_1.owner_full_name)
    print(user_1.balance)
    user_1.increase_balance(100)
    print(user_1.balance)
    user_1.decrease_balance(100)
    print(user_1.balance)
    print()
    user_2 = CreditAccount("Свин Пятачок", 2345.6)
    print(user_2.owner_full_name)
    print(user_2.balance)
    user_2.increase_balance(100)
    print(user_2.balance)
    user_2.decrease_balance(100)
    print(user_2.balance)
    print(user_2.is_eligible_for_credit())
