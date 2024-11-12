# Elijah Dixon
# 11/12/2024
# P4HW1
# Using loops to gather information from a user, and display it in a usable fashion.

# Empty list to store user values. "numscoresQ" is what will check if the number of scroes inout is a number.

scores = []
numscoresQ = False

# Getting the AMOUNT of grades the user will input.
numscores = input("How many scores would you like to enter? ")
print()
        
while numscoresQ == False:
        try:
            int(numscores)
        except:
            print("Only numbers, please.")
            numscoresQ = False
            numscores = input("How many socres would you like to enter? ")
            print()
        else:
            numscoresQ = True

numscores = int(numscores)

# Loop to get each item neccessary.
for item in range(numscores):
    scoreinput = int(input(f"Enter score #{item + 1}: "))
    # Loop to make sure this score is VALID.
    while scoreinput > 100 or scoreinput < 0:
        print(f"Sorry, {scoreinput} is not a valid score. Only numbers between 0-100 allowed.")
        scoreinput = int(input(f"Enter score #{score + 1} again, please: "))
    # Adding this score to the list.
    scores.append(scoreinput)

# Printing and formatting time.



