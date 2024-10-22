# Elijah Dixon
# 10/19/2024
# P2HW2
# Making a progaram that will take information inputted by a user, store that info in a list, and use the list to return useful information on said data.

# Getting the user's input for their information.

m1= float(input("Enter grade for Module 1: "))
m2= float(input("Enter grade for Module 2: "))
m3= float(input("Enter grade for Module 3: "))
m4= float(input("Enter grade for Module 4: "))
m5= float(input("Enter grade for Module 5: "))
m6= float(input("Enter grade for Module 6: "))

# Creating a list based on that information.
modules = [m1, m2, m3, m4, m5, m6]

# Assigning variables to each detail of the list that we will print later. This will make it a little easier to reference in the code later!
HiGrd = max(modules)
LoGrd = min(modules)
SumGrd = sum(modules)

# The average is the most important, we can't calculate this in one command (like max/min) without importing a module.
AvgGrd = SumGrd/len(modules)

# Print the results, formatted similarly to the example.
print()
print("------------Results!-------------")
print()
print(f"{'Lowest Grade: ':<20}{LoGrd}")
print(f"{'Highest Grade: ':<20}{HiGrd}")
print(f"{'Sum of Grades: ':<20}{SumGrd}")
print(f"{'Average: ':<20}{AvgGrd:.2f}")
print()
print("-----------------------------------------")

# To prevent the program from instantly closing.
print()
input("Press ENTER to close.")
