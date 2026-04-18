from models.transaction import Transaction


class BudgetManager:
    def __init__(self):
        self.transactions = []

    #  Ajouter une transaction
    def add_transaction(self, type, amount, category):
        transaction = Transaction(type, amount, category)
        self.transactions.append(transaction)
        print("Transaction ajoutée !")

    #  Lister les transactions
    def list_transactions(self):
        if not self.transactions:
            print("Aucune transaction.")
            return

        for t in self.transactions:
            print(f"{t.type} | {t.amount}€ | {t.category} | {t.date}")

    #  Calculer le solde
    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expense = sum(t.amount for t in self.transactions if t.type == "expense")
        return income - expense

    #  Total revenus
    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.type == "income")

    #  Total dépenses
    def get_total_expense(self):
        return sum(t.amount for t in self.transactions if t.type == "expense")
    
