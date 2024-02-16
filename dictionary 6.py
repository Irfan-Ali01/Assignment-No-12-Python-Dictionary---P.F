phonebook = {}

while True:
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        phonebook[name] = phone
    elif choice == "2":
        search_name = input("Enter the name to search: ")
        if search_name in phonebook:
            print(f"{search_name}'s phone number: {phonebook[search_name]}")
        else:
            print(f"{search_name} not found in the phonebook.")
    elif choice == "3":
        update_name = input("Enter the name to update: ")
        if update_name in phonebook:
            new_phone = input("Enter the new phone number: ")
            phonebook[update_name] = new_phone
        else:
            print(f"{update_name} not found in the phonebook.")
    elif choice == "0":
        break
    else:
        print("Invalid choice. ")