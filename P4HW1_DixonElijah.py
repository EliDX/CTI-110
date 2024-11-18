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

'''
# This will serve to work the same as the numscoresQ code did, bit for scoreinput.
scoreinputQ = False
while scoreinputQ == False:
        try:
            int(numscores)
        except:
            print("Only numbers, please.")
            scoreinputQ = False
            scoresinput = input("How many socres would you like to enter? ")
            print()
        else:
            scoreinputQ = True
'''

# Loop to get each item neccessary. 
for item in range(numscores):
    scoreinput = int(input(f"Enter score #{item + 1}: "))

    # Loop to make sure this score is VALID.
    while scoreinput > 100 or scoreinput < 0:
        print(f"Sorry, {scoreinput} is not a valid score. Only numbers between 0-100 allowed.")
        scoreinput = int(input(f"Enter score #{item + 1} again, please: "))
    # Adding this score to the list.
    scores.append(scoreinput)

# Printing and formatting time.
# I will set variables for the lowest score, average, and reuse the code I made in P2HW2 to get the letter grade. I added the sum to get the average, and the highest grade just because.
# I concidered chaning the variable names to use "scr" to abbreviate score since I used that so much, but it wouldve messed with the big if else staement to  find the letter score.

LoGrd = min(scores)
HiGrd = max(scores)
SumGrd = sum(scores)
AvgGrd = SumGrd/len(scores)

# This is the grade-getting function.
if AvgGrd >= 90:
    LGrade = "A"

if AvgGrd >= 80 and AvgGrd <= 89:
    LGrade = "B"

if AvgGrd >= 70 and AvgGrd <= 79:
    LGrade = "C"

if AvgGrd >= 60 and AvgGrd <= 69:
    LGrade = "D"

if AvgGrd >= 0 and AvgGrd <= 59:
    LGrade = "F"

# The results. (edited version of the older one.)
print()
print("------------Results!-------------")
print()
print(f"{'Lowest Grade: ':<20}{LoGrd:.1f}")
scores.remove(LoGrd)
print(f"{'Modified List: ':<20}{scores}")
print(f"{'Average: ':<20}{AvgGrd:.2f}")
print(f"{'Sores Average: ':<20}{LGrade}") 
print()
print("-----------------------------------------")



# To prevent the program from instantly closing.
print()
input("Press ENTER to close.")
