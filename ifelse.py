# If/else statements.
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# NOTE: the basic "if" statement will only work with one else statement/ vice versa. The else will only work with the last if statement read.
# Use "elif" for mutiple ifs. Will stop at the first true if statement.
if num1 > num2:
    print(f"{num1} is greater than {num2}.")

elif num1 == num2:
    print(f"{num1} is equal to {num2}.")

else:
    print(f"{num1} is NOT greater than {num2}.")
'''

# Get an input from the user.
age = int(input("Enter an age: "))
'''
if age > 65:
    life_stage = "Senior"

elif age > 17:
    life_stage = "Adult"

elif age > 12:
    life_stage = "Teenager"

elif age > 5:
    life_stage = "Child"

elif age > 0:
    life_stage = "Baby"

print (f"You are {age} years old and are a... {life_stage}!")

input("press enter to close")
'''

if age >= 0 and age <= 5:
    life_stage = "Baby/Toddler"

if age >= 6 and age <= 12:
    life_stage = "Child"

if age >= 13 and age <= 17:
    life_stage = "Teenager"

if age >= 18 and age <= 65:
    life_stage = "Adult"

if age >= 65 and age <= 65:
    life_stage = "Senior"

if age <= 150:
    life_stage = "DEAD"

print (f"You are {age} years old and are a... {life_stage}!")
