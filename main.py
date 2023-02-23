class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            print("Недостаточно средств на кошельке.")
            return False
        else:
            self.balance -= amount
            print("Оплата прошла успешно.")
            return True

class Person:
    wallet = Wallet(1000) # Задаем начальный баланс кошелька

class Pay:
    @staticmethod
    def pay(person, amount):
        if person.wallet.withdraw(amount):
            print("Сумма", amount, "грн. списана с кошелька.")
        else:
            print("Сумма не списана с кошелька.")

# Пример использования классов
person = Person()
Pay.pay(person, 500) # Попытка оплаты на 500 грн
Pay.pay(person, 1000) # Попытка оплаты на 1000 грн
