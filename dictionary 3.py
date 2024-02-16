
shopping_list = {}
def add_item():
        item = input("Enter the item to add: ")
        shopping_list[item] = False
        print(f"{item} added to the shopping list.")

def remove_item():
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            del shopping_list[item]
            print(f"{item} removed from the shopping list.")
        else:
            print(f"{item} not found in the shopping list.")

def mark_checked_off():
        item = input("Enter the item to mark as checked off: ")
        if item in shopping_list:
            shopping_list[item] = True
            print(f"{item} marked as checked off.")
        else:
            print(f"{item} not found in the shopping list.")
def view_shopping_list ():
    print (shopping_list)
while True:
    choice=input('''
            1. Add item
            2. Remove item
            3. Mark item as checked off
            4. View shopping list
            0. Exit


''')

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        mark_checked_off()
    elif choice == "4":
        view_shopping_list()
    elif choice == "0":
        print("Exiting. Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        print("\nShopping List:")
        for item, checked in shopping_list.items():
            status = "✓" if checked else " "
            print(f"{status} {item}")