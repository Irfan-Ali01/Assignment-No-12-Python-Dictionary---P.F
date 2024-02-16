menu = {}
with open('menu.txt', 'r') as menu_file:
    for line in menu_file:
        item, price, category = line.strip().split(',')
        menu[item] = {'price': float(price), 'category': category}

while True:
    print("\nRestaurant Menu:")
    print("1. Browse by category")
    print("2. Search for an item")
    print("0. Exit")

    choice = input("Enter your choice (0-2): ")

    if choice == "1":
        category = input("Enter the category: ")
        print(f"\nItems in the '{category}' category:")
        for item, details in menu.items():
            if details['category'] == category:
                print(f"{item} - ${details['price']:.2f}")
    elif choice == "2":
        item_name = input("Enter the item name: ")
        if item_name in menu:
            details = menu[item_name]
            print(f"\nItem: {item_name}")
            print(f"Price: ${details['price']:.2f}")
            print(f"Category: {details['category']}")
        else:
            print(f"{item_name} not found in the menu.")
    elif choice == "0":
        print("Exiting. ")
        break
    else:
        print("Invalid choice. Please select a valid option.")