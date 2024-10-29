# Elijah Dixon
# 10/29/24
# P3HW2
# Using if/else statements to calculate user-inputted values, specifically to find the pay of an employee.

# Gathering essential basic employee information.
employee_name = input("Enter the employee's name: ")
employee_hours = float(input("Enter the number of hours worked: "))
employee_rate = float(input("Enter the per-hour pay rate: "))

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

''''
# Felt like testing the variables (◕‿◕✿)... might delete later.
print()
print(f"Testing... Testing... \nName: {employee_name}\nHours: {employee_hours}\nPay per Hour: {employee_rate}\nRegular Pay: {employee_RegPay}")
print(f"\nOvertime Hours: {employee_OverHours}\nOvertime Pay: {employee_OverPay}\nGross (icky) Pay: {employee_GrossPay}")
'''

# Organizing and formatting the data to be outputted.
print()
print(",ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸")  
print()
print(f"Employee Name: {employee_name}")
print()
print(f"{'Total Hours':<20}{'Hourly Pay Rate':<20}{'Overtime Hours':<20}{'Overtime Pay':<20}{'Regular Pay':<20}{'Gross Pay':<20}")
print("* - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - * - *")
print(f"{employee_hours:<20}${employee_rate:<19.2f}{employee_OverHours:<20}${employee_OverPay:<19.2f}${employee_RegPay:<19.2f}${employee_GrossPay:<19.2f}")
print()
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`°º¤ø,¸¸,ø¤º°`")
print()
print()
# To prevent instant closing.
input("Press ENTER to close.")


