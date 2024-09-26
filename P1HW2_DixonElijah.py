 # Elijah Dixon
 # 9/26/24
 # P1HW2
 # I have been taskes to create a program that can do basic math on any number that is entered.

#Before I concider any code, I need to tell what this application will do.
print("This program calculates and displays travel expenses.")

#First, I need to get the program to gather information from the user and store them as variables.
#The text input type must match what will be typed. I put a try-exept block to prevent crashing just in case!
try:
    budget = float(input("Please enter the budget for your trip: "))
except ValueError:
     print("Please type in only numbers.")

destination = input("Where would you like to go? ")
 
try:
    gas = float(input("How much do you think you'll use on gas? "))
except ValueError:
     print("Please type in only numbers.")
try:
    hotel = float(input("And last but not least, how much will you use on food? "))
except ValueError:
     print("Please type in only numbers.")
 
