shopping_list = []
max_items = 10

while True:
    print("\nShopping List Menu:")
    print("\nOptions: add / remove / view / exit")
    choice = input("What will you like to do?: ").lower()

    if choice == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to your shopping list.")

    elif choice == "remove":
        item = input("Enter item to be removed: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from your shopping list")
        else:
            print("Item not found!")

    elif choice == "view":
        print("\n Your shopping list")
        for item in shopping_list:
            print(f"- {item}")

    elif choice == "exit":
        print("Goodbye")
        break


    

    else:
        print("Invalid choice. Please type add, remove, view, or exit. ")