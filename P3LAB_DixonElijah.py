# Elijah Dixon
# 10/27/24
# P3LAB
# Making a program which can accurately calculate a float value for money into coin/bill values.

# Getting the original value from the user.
original_change = float(input("Enter an amount of money as a float: $"))

# Rounding the value into an integer, to prevent issues with float values and math.
change = round(original_change * 100)

# Time to convert that tasty integer into coins/bills!
# The change amount is updated after each calculation by multiplying the amount of coins by its value and then subtracting from "change".
# Well, besides the pennies, since they're only one cent... And since they're last there's no need to subtract.

n_dollars = change // 100
change = change - (n_dollars * 100)

n_quarters = change // 25
change = change - (n_quarters * 25)

n_dimes = change // 10
change = change - (n_dimes * 10)

n_nickels = change // 5
change = change - (n_nickels * 5)

n_pennies = change

# Now we can use an if/else to make sure that all of our values have the proper plurality. (I think thats the word???)

if n_dollars > 0:
    if n_dollars == 1:
        print(f"{n_dollars} Dollar")
    else:
        print(f"{n_dollars} Dollars")

if n_quarters > 0:
    if n_quarters == 1:
        print(f"{n_quarters} Quarter")
    else:
        print(f"{n_quarters} Quarters")
        
if n_dimes > 0:
    if n_dimes == 1:
        print(f"{n_dimes} Dime")
    else:
        print(f"{n_dimes} Dimes")

if n_nickels > 0:
    if n_nickels == 1:
        print(f"{n_nickels} Nickel")
    else:
        print(f"{n_nickels} Nickels")

if n_pennies > 0:
    if n_pennies == 1:
        print(f"{n_pennies} Penny")
    else:
        print(f"{n_pennies} Pennies")

if original_change == 0:
    print("\nSorry I don't speak POOR.")
    input("\nPress ENTER to close, and go get some cash...")
else:
    print("\nNow how much would you like to tip? Just kidding!")
    input("\nPress ENTER to close.")
