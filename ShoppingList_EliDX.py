#This program will simulate and display a shopping recipt.


#Getting info for item 1. I am using an f string for the first time in this project! Wohoo! Also we are going to stop them for puttting letters.
item1 = input("Enter your first item: ")
quantity1 = int(input(f"Enter the quantity of {item1}: "))
price1 = float(input(f"Enter the price of {item1}: "))

#I could add this code to stop any items from going though that are not numbers, but I didn't for this project.
'''
while quantity1.isalpha():
    print("Please only type in plain numbers.")
    quantity1 = input(f"Enter the quantity of {item1}: "))
    
price1 = float(input(f"Enter the price of {item1}: "))
'''


#Getting info for item 2.
item2 = input("Enter your second item: ")
quantity2 = int(input(f"Enter the quantity of {item2}: "))
price2 = float(input(f"Enter the price of {item2}: "))

#Getting info for item 3.
item3 = input("Enter your third item: ")
quantity3 = int(input(f"Enter the quantity of {item3}: "))
price3 = float(input(f"Enter the price of {item3}: "))

#Display top of recipt.
print("Thanks for shopping at [REDACTED]!")
print("*"*50)
print("")
item="ITEM"
quantity="QUANTITY"
print(f"{item:<20}{quantity:<15}")
print(f"{item1:<20} {quantity1:<15}${price1*quantity1:.2f}")
print(f"{item2:<20} {quantity2:<15}${price2*quantity2:.2f}")
print(f"{item3:<20} {quantity3:<15}${price3*quantity3:.2f}")

#Display the subtotal.
subtotal = (price1*quantity1)+(price2*quantity2)+(price3*quantity3)
print("")
print("")
print(f"Subtotal: {subtotal}")

#Calculating tax and displaying the total price.
tax= subtotal*0.07
total= subtotal + tax
print(f"Tax owed: ${tax:.2f}")
print("")
print(f"Total Price: ${total:.2f}")
