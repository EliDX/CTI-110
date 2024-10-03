 # Elijah Dixon
 # 9/26/24
 # P1HW2
 # I have been tasked to create a program that can do basic math on any number that is entered, relating to travel expenses.

#Before I concider any code, I need to tell what this application will do.
print("This program calculates and displays travel expenses!")

#I need to get the program to gather information from the user and store them as variables.
#The error checking uses a string of regular expression code, I was able to figure it out with my professor.

#It dictates what characters the program needs to watch in a string of text, allowing the program to detect specific characters that are being inputted.
#It basically says "A decimal symbol "." may or may not be present in this response."

import re
pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'

budget = input("What is your budget? ")

while not re.match(pattern, budget):
    print("No symbols or letters, please!")
    budget = input("What is your budget? ")

# The loop will break if budget matches the pattern. Then it is converted into a float! We will repeat this for every number-related input.
budget = float(budget)

#Now I will ask the user where they want to go. This does not need a regular expression.

destination = input("Where do you want to go? ")

#Next are the gas, accomodation, and food prices. They will reuse the regular expression from before.

gas = input("How much will you spend on gas? ")

while not re.match(pattern, gas):
    print("No symbols or letters, please!")
    gas = input("How much will you spend on gas? ")

gas = float(gas)

accomodations = input("How much will you spend on a hotel or other accomodations? ")

while not re.match(pattern, accomodations):
    print("No symbols or letters, please!")
    accomodations = input("How much will you spend on a hotel or other accomodations? ")

accomodations = float(accomodations)

food = input("How much will you spend on food? ")

while not re.match(pattern, food):
    print("No symbols or letters, please!")
    food = input("How much will you spend on food?: ")

food = float(food)

#Now that we have evrything we can start the calculations. I have the program print each of the results and calculate the total and amout of money left over. 

total = gas + accomodations + food
fbudget = budget - total

print("")
print("_-_-_-_-_-_- Results -_-_-_-_-_-_")
print("")

print(f"Location: {destination}")
print(f"Original Budget: {budget}")
print(f"Gas Expenses: {gas}")
print(f"Accomodation: {accomodations}")
print(f"Food: {food}")
print("")
print("")
print(f"Money to be spent: {total}")
print(f"Remaining Balance: {fbudget}")
print("")

#I left a little message at the end so the program doesnt instantly close. If your total exeeds your budget, a different message will display.
if total>budget :
    input("You might need to revise your budget... Press ENTER to close.")
    print("")
    print("")

else:
   input("Have a great trip! Press ENTER to close.") 



