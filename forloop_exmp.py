# For loop using range function with one parameter. It is the stop value.
'''
for var in range(5):
    print(var + 1)
    #print("dinosaur")
'''

# For loop using the range function with parameters. The first is the stop value, the second is the end value.
'''
for item in range(7,end_num+1):
    print(item)
'''
# Print the loop using the range function with three parameters.
# The third number specifies how many steps to take between numbers, in this case 5 each time (5 10 15 20 25 30 etc.)
'''
for cat in range (0,101,5):
    print (cat)
'''

# Loop through a list and print each item.
'''
myList = ["one", 2, 2.5, "three", 4, 4.5, "five", True]

for thing in myList:
    print(thing)
'''

numList = [10, 20, 30, 40, 50]

total = 0
for num in numList:
    total = total + num
print(f"The final total is {total}.")
