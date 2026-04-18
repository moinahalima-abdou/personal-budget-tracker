from datetime import datetime
import uuid


class Transaction:
    def __init__(self, type, amount, category):
        self.id = str(uuid.uuid4())
        self.type = type  # "income" ou "expense"
        self.amount = amount
        self.category = category
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }