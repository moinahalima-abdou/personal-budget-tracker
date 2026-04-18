from services.budget_manager import BudgetManager
from storage.storage import Storage


def show_menu():
    print("\n=====  BUDGET TRACKER =====")
    print("1. Ajouter un revenu")
    print("2. Ajouter une dépense")
    print("3. Voir les transactions")
    print("4. Voir le solde")
    print("5. Quitter")


def main():
    storage = Storage()
    manager = BudgetManager()

    #  Charger les données
    manager.transactions = storage.load_transactions()

    while True:
        show_menu()
        choice = input("Choisis une option : ")

        #  Ajouter revenu
        if choice == "1":
            try:
                amount = float(input("Montant : "))
            except ValueError:
                print("Montant invalide ❌")
                continue

            category = input("Catégorie : ")
            manager.add_transaction("income", amount, category)

        #  Ajouter dépense
        elif choice == "2":
            try:
                amount = float(input("Montant : "))
            except ValueError:
                print("Montant invalide ❌")
                continue

            category = input("Catégorie : ")
            manager.add_transaction("expense", amount, category)

        #  Voir transactions
        elif choice == "3":
            manager.list_transactions()

        #  Voir solde
        elif choice == "4":
            balance = manager.get_balance()
            print(f"💰 Solde actuel : {balance}€")

        # Quitter
        elif choice == "5":
            storage.save_transactions(manager.transactions)
            print("Au revoir 👋")
            break

        else:
            print("Option invalide ❌")


if __name__ == "__main__":
    main()