"""
account.py

Den här filen innehåller en klass som representerar ett bankkonto och ett anpassat undantag för otillräckligt saldo. 

Klassen Account har följande attribut:
- account_number: Kontonumret (str)
- owner: Kontots ägare, en instans av Customer-klassen
- balance: Kontots saldo (float, standardvärde 0)

Klassen Account har följande metoder:
- deposit(amount): Lägger till en insättning på kontot, ger ValueError om beloppet är negativt eller 0.
- withdraw(amount): Gör ett uttag från kontot, ger ValueError om beloppet är negativt eller 0 och InsufficientFundsError om saldot är otillräckligt.
- transfer(other_account, amount): Överför pengar från det aktuella kontot till ett annat konto, ger ValueError om beloppet är negativt eller 0 och InsufficientFundsError om saldot är otillräckligt.

InsufficientFundsError är ett anpassat undantag som används för att indikera att ett konto har otillräckligt saldo för att genomföra en transaktion.
"""

class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Insättningar måste vara större än 0.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Uttag måste vara större än 0.")
        if amount > self.balance:
            raise InsufficientFundsError("Otillräckligt saldo för uttag.")
        self.balance -= amount

    def transfer(self, other_account, amount):
        if amount <= 0:
            raise ValueError("Överföringar måste vara större än 0.")
        self.withdraw(amount)
        other_account.deposit(amount)

    def __str__(self):
        return f"{self.account_number}: {self.owner}, Saldo: {self.balance} kr"
