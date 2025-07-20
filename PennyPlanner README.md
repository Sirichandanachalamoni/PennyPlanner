# 🪙 PennyPlanner

**PennyPlanner** is a command-line based personal expense tracker built using Python. It helps users track expenses by category, check if they exceed their spending limits, and view a summary of all transactions.

---

## 📌 Features

- ➕ Add expenses with category and description
- 🔍 Search expenses by category
- 📝 Update or delete existing expense categories
- ⚠️ Warns if spending exceeds predefined limits
- 📊 Shows total and category-wise summary on exit

---

## 🛠️ Technologies Used

- **Python**
- **Command Line Interface (CLI)**
- Python **lists**, **dictionaries**, **control flow**, and **exception handling**

---

## 💡 How It Works

1. Choose an operation: `add`, `search`, `update`, `delete`, or `exit`
2. Enter details like amount, category, and description
3. Program tracks the expenses and alerts you if any category goes over the budget
4. On exit, it displays the total and a category-wise summary

---

## 📂 Example Categories & Limits

```python
limits = {
    "food": 5000,
    "travel": 3000,
    "rent": 4000,
    "shopping": 5000
}
