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
    pass
elif operations == "2":
    pass
elif operations == "3":
    pass

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
