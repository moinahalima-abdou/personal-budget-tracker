import json
from models.transaction import Transaction


class Storage:
    def __init__(self, filename="data/transactions.json"):
        self.filename = filename

    #  Sauvegarder
    def save_transactions(self, transactions):
        data = [t.to_dict() for t in transactions]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    #  Charger
    def load_transactions(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read().strip()

                if not content:
                    return []

                data = json.loads(content)

                return [self.dict_to_transaction(item) for item in data]

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    #  convertir JSON → objet
    def dict_to_transaction(self, data):
        transaction = Transaction(
            data["type"],
            data["amount"],
            data["category"]
        )
        transaction.id = data["id"]
        transaction.date = data["date"]
        return transaction