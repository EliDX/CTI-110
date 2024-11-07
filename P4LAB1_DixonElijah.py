# Elijah Dixon
# 11/17/24
# P4LAB1
# Using turtle graphics to create images.

# Importing the turtle, and chainging the background color.
import turtle
wn = turtle.Screen()
wn.bgcolor("#e1ffa0")

# The birth of my beautiful son. 
glorby = turtle.Turtle()
glorby.pensize(5)
glorby.pencolor("green")

glorby.shapesize(stretch_wid=3, stretch_len=3, outline=2)

# While loop to draw a square.
num = 0

while num < 4:
    glorby.forward(150)
    glorby.right(90)
    num += 1
print("While (SQUARE) loop ends.")

# For loop for the triangle! Also I changed the line color.
glorby.pencolor("red")

for triangle in range(0,3):
    glorby.left(120)
    glorby.forward(150)
print("For (TRIANGLE) loop ends.")

