"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

user_name = input("What is your user name? ")
print(f"\nHello, {user_name}!\nWhat would you like to do?")
operations = input("1. List items by warehouse\n2. Search an item and place an order\n3. Quit\nType the number of the operation: ")

if operations == "1":
    print("\nItems in warehouse 1:")
    for item in set(warehouse1):
        print(f"- {item}")
    print("\nItems in warehouse 2:")
    for item in set(warehouse2):
        print(f"- {item}")
elif operations == "2":
    chosen_item = input("\nWhat is the name of the item? ")
    if chosen_item not in warehouse1 and chosen_item not in warehouse2:
        print(f"Amount available: 0")
        print(f"Location: Not in stock")
        print(f"\nThank you for your visit, {user_name}!")
    if chosen_item in warehouse1 and chosen_item in warehouse2:
        amount_available1 = warehouse1.count(chosen_item)
        amount_available2 = warehouse2.count(chosen_item)
        amount_available = int(amount_available1) + int(amount_available2)
        print(f"Amount available: {amount_available}")
        print(f"Location: Both warehouses")
        if amount_available2 > amount_available1:
            print(f"Maximum availability: {amount_available2} in Warehouse 2")
        else:
            print(f"Maximum availability: {amount_available1} in Warehouse 1")
        order_option = input("\nWould you like to order this item?(y/n) ")
        if order_option == "y":
            amount_to_order = int(input("How many would you like? "))
            if amount_to_order > amount_available:
                print(50*"*")
                print(f"There are not this many available. The maximum amount that can be ordered is {amount_available}")
                print(50*"*")
                max_amount_to_order =input("Would you like to order the maximum available?(y/n) ")
                if max_amount_to_order == "y":
                    print(f"{amount_available} {chosen_item} have been ordered.")
                else:
                    pass
            else:
                pass
elif operations == "3":
    pass


print(f"\nThank you for your visit, {user_name}!")
# YOUR CODE STARTS HERE

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit
