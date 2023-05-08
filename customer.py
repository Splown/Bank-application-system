"""
customer.py

Den här filen innehåller en klass som representerar en bankkund. Klassen Customer har följande attribut:

- name: Kundens namn (str)
- personal_id: Kundens personnummer (str)
- address: Kundens adress (str)

Klassen har även en __str__-metod som returnerar en strängrepresentation av kundobjektet.
"""

class Customer:
    def __init__(self, name, personal_id, address):
        self.name = name
        self.personal_id = personal_id
        self.address = address

    def __str__(self):
        return f"{self.name} ({self.personal_id})"
