import streamlit as st
import matplotlib.pyplot as plt

from services.budget_manager import BudgetManager
from storage.storage import Storage
from utils.analytics import Analytics


# INIT

storage = Storage()
manager = BudgetManager()

manager.transactions = storage.load_transactions()
analytics = Analytics(manager.transactions)

st.title(" Personal Budget Tracker")


# AJOUT TRANSACTION

st.header(" Ajouter une transaction")

type_choice = st.selectbox("Type", ["income", "expense"])
amount = st.text_input("Montant")
category = st.text_input("Catégorie")

if st.button("Ajouter"):
    try:
        amount = float(amount)

        manager.add_transaction(type_choice, amount, category)
        storage.save_transactions(manager.transactions)

        st.success("Transaction ajoutée ")
    except ValueError:
        st.error("Montant invalide ")


# SOLDE

st.header("💰 Solde")

st.metric("Balance", f"{analytics.balance()} €")


# TRANSACTIONS

st.header(" Transactions")

for t in manager.transactions:
    st.write(f"{t.type} | {t.amount}€ | {t.category} | {t.date}")

# GRAPH - CATEGORIES

st.header(" Dépenses par catégorie")

data = analytics.expenses_by_category()

if data:
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())
    st.pyplot(fig)
else:
    st.info("Aucune dépense")


# GRAPH - EVOLUTION

st.header(" Dépenses dans le temps")

data_time = analytics.expenses_over_time()

if data_time:
    fig2, ax2 = plt.subplots()
    ax2.plot(list(data_time.keys()), list(data_time.values()), marker="o")
    plt.xticks(rotation=45)
    st.pyplot(fig2)
else:
    st.info("Aucune donnée")