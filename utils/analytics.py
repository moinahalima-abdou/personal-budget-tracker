from collections import defaultdict


class Analytics:
    def __init__(self, transactions):
        self.transactions = transactions

    #  Total revenus
    def total_income(self):
        return sum(t.amount for t in self.transactions if t.type == "income")

    #  Total dépenses
    def total_expense(self):
        return sum(t.amount for t in self.transactions if t.type == "expense")

    #  Solde
    def balance(self):
        return self.total_income() - self.total_expense()

    #  Dépenses par catégorie
    def expenses_by_category(self):
        categories = defaultdict(float)

        for t in self.transactions:
            if t.type == "expense":
                categories[t.category] += t.amount

        return dict(categories)

    #  Dépenses par date (simple)
    def expenses_over_time(self):
        dates = defaultdict(float)

        for t in self.transactions:
            if t.type == "expense":
                date = t.date.split(" ")[0]  # garde juste YYYY-MM-DD
                dates[date] += t.amount

        return dict(dates)