# Elijah Dixon
# 10/29/24
# P3HW2
# Using if/else statements to calculate user-inputted values, specifically to find the pay of an employee.
# Then, totaling those values and displaying it for ANY number of employees.

# Variables to hold the totals and number of employees.
tot_employee = 0 
employee_names = []
tot_regular = 0
tot_overtime = 0
tot_gross = 0

# Asking if the user would like to continue.
keep_goin = "not exit"

# Here is where I start the while loop.
print("This program can calculate the pay for an employee based on their pay rate and hours worked. The default value for 'regular hours' is 40.")
print()

while keep_goin.lower() != "exit":
    # Gathering essential basic employee information.
    employee_name = input("Enter an employee's name: ")
    employee_hours = float(input(f"Enter the number of hours {employee_name} worked: "))
    employee_rate = float(input(f"Enter the per-hour pay rate for {employee_name}: "))

    # Calculating overtime pay. If the employee has worked overtime, the extra hours are calculated at 1.5 * the regular pay rate.
    # After that 40 is multiplied by the pay rate, since they only get paid regular pay for the first 40.
    # If not, all overtime values are set to zero.
    if employee_hours > 40:
        employee_OverHours = employee_hours - 40
        employee_OverPay = employee_OverHours * (1.5 * employee_rate)
        employee_RegPay = 40 * employee_rate
    else:
        employee_OverHours = 0
        employee_OverPay = 0
        employee_RegPay = employee_hours * employee_rate


    # Calculating the employees gross pay.
    employee_GrossPay = employee_RegPay + employee_OverPay

    # Adding these values to the totals to be stored for later.
    tot_employee = tot_employee + 1
    employee_names.append(employee_name)
    tot_regular = tot_regular + employee_RegPay
    tot_overtime = tot_overtime + employee_OverPay
    tot_gross = tot_gross + employee_GrossPay

    # Organizing and formatting the data to be outputted.
    print()
    print(":-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:")  
    print()
    print(f"Employee Name: {employee_name}")
    print()
    print(f"{'Total Hours':<20}{'Hourly Pay Rate':<20}{'Overtime Hours':<20}{'Overtime Pay':<20}{'Regular Pay':<20}{'Gross Pay':<20}")
    print("* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *")
    print(f"{employee_hours:<20}${employee_rate:<19.2f}{employee_OverHours:<20}${employee_OverPay:<19.2f}${employee_RegPay:<19.2f}${employee_GrossPay:<19.2f}")
    print()
    print(":-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:")
    print()
    print()

    # Ask if they want to keep going.
    keep_goin = input("Press ENTER to keep going, or type 'exit' to end the program. ")

print()

print(f"Total number of employees entered: {tot_employee}")
print(f"Employees: {employee_names}")
print()
print(f"Total amount paid out for regular hours: ${tot_regular:.2f}")
print(f"Total amount paid out for overtime: ${tot_overtime:.2f}")
print(f"Total amount paid out in gross: ${tot_gross:.2f}")
# To prevent instant closing.
print()
input("Thanks for using this program! Press ENTER to close.")


