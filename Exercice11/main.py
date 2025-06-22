

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


if __name__ == '__main__':

    compte = BankAccount("Fabien", 1000.0)

    print("affichage des infos du compte: ", compte.display_balance())
    print("Depot de 500: ", compte.deposit(500))
    print("Retrait de 200: ", compte.withdraw(200))
    print("tentative de retrait superieur au solde: ", compte.withdraw(2000))
    print("tentative de depot d'un montant negatif: ", compte.deposit(-100))
    print("affichage des infos du compte: ", compte.display_balance())
