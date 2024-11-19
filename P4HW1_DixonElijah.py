# Elijah Dixon
# 11/12/2024
# P4HW1
# Using loops to gather information from a user, and display it in a usable fashion.

# Empty list to store user values. "numscoresQ" is what will check if the number of scores input is a number.

scores = []
numscoresQ = False

# Getting the AMOUNT of grades the user will input, using the numscores variable.
numscores = input("How many scores would you like to enter? ")
print()

# This uses the numscoresQ boolean to make sure that the numscores value is correct.       
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

# Loop to get each item neccessary. I used a try exept mixed with a while loop to prevent letters and numbers over 100 or under 0.

for item in range(numscores):
    scoreinputQ = False
    while scoreinputQ == False:
        try:
            scoreinput = float(input(f"Enter score #{item + 1}: "))
            print()
            while scoreinput > 100 or scoreinput < 0:
                print(f"Sorry, {scoreinput} is not a valid score. Only numbers between 0-100 allowed.")
                scoreinput = float(input(f"Enter score #{item + 1} again: "))
                print()
        except ValueError:
            print("No letters allowed, please!")
            print()
        else:
            scoreinputQ = True
            
    scores.append(scoreinput)

# Printing and formatting time.
# I will set variables for the lowest score, average, and reuse the code I made in P2HW2 to get the letter grade.
# I added the sum to get the average, and the highest grade just because.
# I concidered chaning the variable names to use "scr" to abbreviate score since I used that so much, but it wouldve messed with the if/else.

LoGrd = min(scores)
HiGrd = max(scores)
SumGrd = sum(scores)
AvgGrd = SumGrd/len(scores)

# This is the grade-getting function.
if AvgGrd >= 90:
    LGrade = "A"
