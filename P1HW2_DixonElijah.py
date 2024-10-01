 # Elijah Dixon
 # 9/26/24
 # P1HW2
 # I have been taskes to create a program that can do basic math on any number that is entered.

#Before I concider any code, I need to tell what this application will do.
print("This program calculates and displays travel expenses.")

#I need to get the program to gather information from the user and store them as variables.
#The error checking uses a string of regular expression code, I was able to figure it out with my professor.
#It tells what caracters are allowed in a string of text, allowing the program to limit letters from being inputted for number fields.
import re

budget = input("Enter a budget: ")
# This regex matches an optional sign, digits, and an optional decimal part.
pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'
while not re.match(pattern, budget):
    print("Letters not allowed")
    budget = input("Enter a budget: ")

# Loop breaks if budget matches the pattern. Then it is converted into a float!
budget = float(budget)
