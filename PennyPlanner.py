list1 = []
limits = {"food": 5000, "travel": 3000, "rent": 4000, "shopping": 5000}

def add():
    while True:
        try:
            amount = int(input("Enter the amount: "))
            break
        except ValueError:
            print("Please enter a number.")

    category = input("Enter the category you spent the amount on: ").lower()
    description = input("Enter the description: ")

    for i in list1:
        if i["category"] == category:
            i["amount"] += amount
            if description not in i["description"]:
                i["description"].append(description)
            break
    else:
        list1.append({
            "amount": amount,
            "category": category,
            "description": [description]
        })

    print("\nExpense added successfully!\n")

def search():
    search_category = input("Enter the category you want to search: ").lower()
    for i in list1:
        if i["category"] == search_category:
            print(f"\n Found in '{search_category.title()}':")
            print(f"  Amount spent: ₹{i['amount']}")
            print(f"  Descriptions: {', '.join(i['description'])}")
            if search_category in limits:
                if i["amount"] > limits[search_category]:
                    print(f" Warning: You have exceeded your limit for {search_category}!")
            else:
                print(f"No predefined limit for {search_category}.")
            return
    print("Category not found.")

def update():
    category = input("Enter the category to update: ").lower()
    for i in list1:
        if i["category"] == category:
            try:
                new_amount = int(input("Enter the new amount to set: "))
                i["amount"] = new_amount
                print("Amount updated successfully!")
                return
            except ValueError:
                print("Invalid amount.")
                return
    print("Category not found.")

def delete():
    category = input("Enter the category you want to delete: ").lower()
    for i in list1:
        if i["category"] == category:
            list1.remove(i)
            print(f"'{category}' deleted successfully.")
            return
    print("Category not found.")

def show_summary():
    print("\nSummary of All Expenses:")
    total = 0
    for i in list1:
        print(f"- {i['category'].title()}: ₹{i['amount']} (Descriptions: {', '.join(i['description'])})")
        total += i["amount"]
    print(f"\nTotal Expenses: ₹{total}")
    print("Thank you!\n")

while True:
    print("\n--- Expense Tracker ---")
    operation = input("Choose operation (add/search/update/delete/exit): ").lower()

    if operation == "add":
        add()
    elif operation == "search":
        search()
    elif operation == "update":
        update()
    elif operation == "delete":
        delete()
    elif operation == "exit":
        show_summary()
        break
    else:
        print("Invalid input. Please try again.")
