# Example which will help on finishing P4 HW 1
# Elijah Dixon

# List of available items (unneeded for hw)
availableitems = ["soil", "perlite", "terracotta pot", "fertilizer", "insecticidal soap",\
                  "neem oil", "bark"]
# Empty list to hold user inputs.
cart = []

# This part is like the hw. Get the number of items to purchase.
numitems = int(input("How many items would you like to purchase? "))

# Loop to get all of the items
for item in range(numitems):
    thisitem = input(f"Enter item #{item + 1}: ")
    # Loop to ensure this item is in availaible items list.
    while thisitem.lower() not in availableitems:
        print(f"Sorry, {thisitem} is not in stock...")
        thisitem  = input(f"Enter item #{item + 1} again, please: ")
    # Add the valid item to the list
    cart.append(thisitem)

# Print every item in the cart.
print()
print("Items you purhcased are: ")