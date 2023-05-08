"""
main.py

Det här är huvudfilen för bankapplikationssystemet. Programmet utför följande uppgifter:

1. Skapar två kundobjekt med hjälp av Customer-klassen.
2. Skapar två konton, ett för varje kund, med hjälp av Account-klassen.
3. Skriver ut kontoinformationen före och efter en överföring mellan de två kontona.
4. Hanterar fel och undantag, såsom ogiltiga insättningar, uttag och överföringar samt otillräckligt saldo.
"""

from customer import Customer
from account import Account, InsufficientFundsError

def main():
    customer1 = Customer("Alice Andersson", "901201-1234", "Storgatan 1")
    customer2 = Customer("Bob Bergström", "910612-4321", "Liljegatan 2")

    account1 = Account("123-456-789", customer1, 1000)
    account2 = Account("234-567-891", customer2)

    print("Konton innan överföring:")
    print(account1)
    print(account2)

    try:
        account1.transfer(account2, 500)
    except InsufficientFundsError as e:
        print(f"Överföring misslyckades: {e}")

    print("\nKonton efter överföring:")
    print(account1)
    print(account2)

if __name__ == "__main__":
    main()
