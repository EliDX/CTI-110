# Elijah Dixon
# 10/8/2024
# P2LAB1
# Calculating the values of a circle using the radius using Pythons built in math liabrary.

#Importing the math library.
import math

print(f"The value of pi is {math.pi}\n")
      
#Get radius from user.
radius = float(input("What is the radius of the circle? "))
print()

#Calculate the diameter.
diameter = 2 * radius

#Display the diameter with one decimal place
print(f"The diameter of the circle is {diameter:.2f}\n")

#Calculate the circumference.
circumfrence = 2 * math.pi * radius

#Display the circumference.
print(f"The circumference of the circle is {circumfrence:.2f}\n")

#Calculate the area.
area = math.pi * (radius ** 2)

#Display the area.
print(f"The area of the circle is {area:.3f}\n")

#Empty input to prevent the app instantly closing.
input("")
