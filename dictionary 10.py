expense_tracker = {}

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add an expense")
    print("2. View expenses by category")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter the expense category (e.g., transportation, accommodation, food): ")
        expense = float(input("Enter the expense amount: "))

        if category in expense_tracker:
            expense_tracker[category] += expense
        else:
            expense_tracker[category] = expense

        print(f"{expense:.2f} added to {category} expenses.")
    elif choice == "2":
        print("\nExpenses by Category:")
        for category, total_expense in expense_tracker.items():
            print(f"{category}: ${total_expense:.2f}")
    elif choice == "0":
        print("Exiting. Safe travels!")
        break
    else:
        print("Invalid choice.")