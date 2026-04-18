# personal-budget-tracker
A personal budget tracking application built with Python.  It allows users to manage income and expenses, categorize transactions, and visualize financial data.


 # 💰 Personal Budget Tracker

A simple Python application to manage your personal budget.

It allows you to track income and expenses, categorize transactions, and visualize your financial data with charts.

---

## 🚀 Features

- ➕ Add income and expenses
- 🏷️ Categorize transactions (food, transport, salary, etc.)
- 💰 Calculate balance automatically
- 📊 View statistics and charts
- 💾 Save data locally (JSON)
- 📈 Visualize data with graphs (matplotlib)
- 🌐 Web interface with Streamlit

---

## 🧱 Project Structure

 personal-budget-tracker/
│
├── app.py # Streamlit interface
├── main.py # CLI version (optional)
│
├── models/
│ └── transaction.py
│
├── services/
│ └── budget_manager.py
│
├── storage/
│ └── storage.py
│
├── utils/
│ └── analytics.py
│
├── data/
│ └── transactions.json
│
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1. Clone the project
```bash
git clone https://github.com/your-username/personal-budget-tracker.git
cd personal-budget-tracker

pip install -r requirements.txt
