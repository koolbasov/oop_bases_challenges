"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income

    def decrease_balance(self, outcome: float):
        if outcome < 0:
            raise ValueError("Расход не может быть отрицательным")
        elif outcome > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= outcome


if __name__ == "__main__":
    bank_account_1 = BankAccount("Ivanov Ivan Ivanovich", 100_000)
    print(bank_account_1.balance)
    bank_account_1.decrease_balance(1000)
    print(bank_account_1.balance)
    # bank_account_1.decrease_balance(100_000)
    # print(bank_account_1.balance)
    bank_account_1.decrease_balance(-10000)
    print(bank_account_1.balance)
