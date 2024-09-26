# Elijah Dixon
# 9/26/2024
# P1HW1
# Get integer input from from the user and perform a calc (thats the new slang for "calculation").

# Display output to user
print("-----Calculating Exponents-----")
print()
print()

#Get info from user
base_value = float(input("Enter an integer as the base value: "))
exponent = float(input("Enter an integer as the exponent: "))
print()
print()

#Calcuate the value of the exponent math
exponent_calc = base_value ** exponent

#Display the results of our calc (which is again, the hip and new slang for, "calculation"). I love calcing! Its so fun.
print(base_value, "raised to the power of", exponent, "is", exponent_calc, "!!")
print()
print()

#Time to start calcing with addition and subtraction. I did the same as before but with addition and subtraction.
print("-----Addition and Subtraction-----")
print()
print()

start_int = float(input("Enter a starting integer: "))
add_int = float(input("Enter an integer to add: "))
sub_int = float(input("Enter an integer to subtract: "))
print()
print()

calc2 = start_int + add_int - sub_int

print(start_int, "+", add_int, "-", sub_int, "is equal to", calc2)
print()
print()
print("Thank you!")
print()
input("~~Press ENTER to close.~~")
