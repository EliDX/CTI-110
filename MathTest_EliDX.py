#EliDX
#10/3/24
#In-class examples of math equations.

#Impoer random library for usage!
import random

#Manual input of values from the user!
'''
side1 = float(input("Side 1's value: "))
side2 = float(input("Side 2's value: "))
'''

#Random input of values by the program!
side1 = random.randint (1,100)
side2 = random.randint (1,100)

#Calculation of the hypotenuse.
hypotenuse = (side1 ** 2 )+ (side2 ** 2)

#Print the results!
print(f"The hypotenuse of a right triangle with side lengths of {side1} and {side2} is {hypotenuse}")
