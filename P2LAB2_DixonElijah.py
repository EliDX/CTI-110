# Elijah Dixon
# P2LAB2
# 10/10/24
# Use a dictionary.

# Create the dictionary!
cars = {"Camaro":18.21, "Prius":52.36, "Model S": 110, "Silverado": 26}

# Variable that holds the keys.
keys = cars.keys()

# Print out the dictionary's keys. 
print(keys)
print("\n")

# Get the user to input a key.
carschoice = input("Enter one of the vehicles above to see its mpg/mpge: ")
print()

# Print the miles per gallon of the car that was selected.
print(f"The {carschoice} gets {cars[carschoice]} mpg.")
print("\n")

# Ask for how many miles the car will be driven, and save it as a variable.
milesdrive = float(input(f"How many miles will you drive the {carschoice}? "))
print()

# Calculate how much gas it will take to drive the car that far.
milesneeded = milesdrive / cars[carschoice]

# Print the final amount of gas needed to drive the car the previously inputted amount of miles to be driven.
print(f"{milesneeded:.2f} gallon(s) of gas are needed to drive the {carschoice} {milesdrive} miles.")
print("\n\n")

input("Press ENTER to close.")



