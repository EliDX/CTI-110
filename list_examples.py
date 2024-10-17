# In class list examples!!!!!! WOHOO OMG YESSSSS SLAYYY

# Create a scrumptious empty list.

myplants = []

myplants.append("Anthirium")
myplants.append("Thanksgiving Cactus")
myplants.append("Domino Peace Lily")
myplants.append("ZZ Plant")
myplants.append("Lace Aloe")
myplants.append("False Galaxy Aralia")
# Display the list IMMEDIATELY!!!!!
print(myplants)
print()

# Print item #3.
print("Printing one plant...")
print(myplants[3])
print()

# Print items 1 to 3. The thng goes beginning:UP TO THIS NUMBER
print("Printing just 3...")
print(myplants[1:4])
print()

# Remove from list by its value.
print("Oops, my anthirium rotted... Gotta remove it.")
myplants.remove("Anthirium")
print(myplants)
print()

# Remove an item from the list by its index number.
print("Oops, my aralia dried out... Gotta remove it.")
myplants.pop(4)
print(myplants)
print()

# Number list.

n1= int(input("gimme a numby wumby!!! "))
n2= int(input("gimme a numby wumby!!! "))
n3= int(input("gimme a numby wumby!!! "))
n4= int(input("gimme a numby wumby!!! "))

numbers = [n1, n2, n3, n4]

print(numbers)
print()
# How many numbers in the numbers list????

print(f"There are {len(numbers)} items in the numbers list.")
print()

# Get highest number in the list.
print(f"The largest number is {max(numbers)}!")
print()
      
# Get the minimym number in the list.  
print(f"The most itty-bitty number is {min(numbers)}!")
print()

# Get the sum of all the numbers in the list.
print(f"The sum of the numbers is {sum(numbers)}!")
print()

# GEt THE AVERGAE.
average = sum(numbers)/len(numbers)

#PRINT!!!
print(f"The average of the numbers list is {average}.")
