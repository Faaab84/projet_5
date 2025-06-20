

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
