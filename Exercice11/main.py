

class BankAccount:

    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            return f"{amount} déposé. Nouveau solde : {self.balance}"
        return "Le montant doit être positif."

    def withdraw(self, amount):

        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"{amount} retiré. Nouveau solde : {self.balance}"
            return "Solde insuffisant."
        return "Le montant doit être positif."

    def display_balance(self):
        return f"Titulaire : {self.account_holder}, Solde : {self.balance}"



"""compte = BankAccount("Jean Dupont", 1000.0)

# Affichage du solde initial
print(compte.display_balance())

# Dépôt de 500
print(compte.deposit(500))

# Retrait de 200
print(compte.withdraw(200))

# Tentative de retrait supérieur au solde
print(compte.withdraw(2000))

# Tentative de dépôt négatif
print(compte.deposit(-100))

# Affichage du solde final
print(compte.display_balance())"""