# Using Python built-in libraries.

# Import the date-time library to use in my program.

import datetime

# Assign the current date and time to a variable.
time = datetime.datetime.now()
month = time.month
month_word = time.strftime("%B")
today = datetime.datetime.today()

#Display the date and time.
print(f"The current date and time is: {time}")
print(f"The current month is: {month}")
print(f"The current month is: {month_word}")
print(f"Today is {today}")
print()
print()

# Get the weekday, and give a number output from 0-6. (0 = monday, 6 = sunday)
weekday = today.weekday()
weekday = int(weekday)
print(f"The day of the week is {weekday}\n")

'''
# You could also do this to make them give a response.
weekday = input(int("Give me a weekdat from 0 (monday) to 6( sunday): "))
'''


#if else statements to determine the day of the week's normal name.
if weekday == 0:
    weekday_word = "Monday"

elif weekday == 1:
    weekday_word = "Tuesday"

elif weekday == 2:
    weekday_word = "Wednesday"

elif weekday == 3:
    weekday_word = "Thursday"

elif weekday == 4:
    weekday_word = "Friday"

elif weekday == 5:
    weekday_word = "Saturday"

elif weekday == 6:
    weekday_word = "Sunday"

else:
    print("Invalid day of the week!")
    weekday_word = "INVALID"

print(f"The day of the week is {weekday_word}")

input("")
