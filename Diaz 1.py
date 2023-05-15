def create(items, key, value):
    for item in items:
        if item[0] == key:
            return False
    
    items.append((key, value))
    return True

def read(items, key):
    found = False
    for item in items:
        if item[0] == key:
            print(f"Value for item '{key}': {item[1]}\n")
            found = True
            break
    if not found:
        print(f"No item found with name '{key}'.\n")

def update(items, key, new_value):
    found = False
    for i, item in enumerate(items):
        if item[0] == key:
            items[i] = (key, new_value)
            print(f"Value for item '{key}' updated.\n")
            found = True
            break
    if not found:
        print(f"No item found with name '{key}'.\n")

def delete(items, key):
    found = False
    for i, item in enumerate(items):
        if item[0] == key:
            del items[i]
            print(f"Item with name '{key}' deleted.\n")
            found = True
            break
    if not found:
        print(f"No item found with name '{key}'.\n")

items = []

while True:
    print("--STOCKTACKING HELPER 1.0--")
    print(" ")
    print("CHOOSE NUMBER BELOW")
    print("1. Create new item")
    print("2. Read item")
    print("3. Update item")
    print("4. Delete item")
    print("5. Display list")
    print("6. Quit")
    action = input("Enter the number of the action to perform: ")

    if action == "1":
        key = input("Enter the name for the new item: ")
        value = input("Enter the quantity for the new item: ")
        if create(items, key, value):
            print("New item added to list.\n")
        else:
            print(f"Item with name '{key}' already exists. Item not added.\n")

    elif action == "2":
        key = input("Enter the name of the item to display: ")
        read(items, key)

    elif action == "3":
        key = input("Enter the name of the item to modify: ")
        new_value = input(f"Enter the new quantity for item '{key}': ")
        update(items, key, new_value)

    elif action == "4":
        key = input("Enter the name of the item to delete: ")
        delete(items, key)

    elif action == "5":
        print("All items and quantities in list:")
        for item in items:
            print(f"  {item[0]}: {item[1]}")
        print()

    elif action == "6":
        print("Exiting program. Bye!")
        break

    else:
        print("Invalid action. choose 1-6 only!.\n")
