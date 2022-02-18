import random

# Constants
WAGE_PER_HOUR = 20
Full_DAY_HOUR = 8
PART_TIME_HOUR = 6
WORKING_DAY_PER_MONTH = 20

# using random to checking the attendance
attendance_check = random.randint(0, 2)
print(f'Attendance {attendance_check}')

# calculating the daily employee wage
daily_emp_wage = WAGE_PER_HOUR * Full_DAY_HOUR
print('Wage per day is : {}'.format(daily_emp_wage))

# calculating the part-time employee wage
part_time_emp_wage = WAGE_PER_HOUR * PART_TIME_HOUR
print('Part Time Wage per day is : {}'.format(part_time_emp_wage))

# Using case statement the values are stored in list of dict
employee_wage = {
    0: {'attendance': 'absent', 'wage': 0, 'working_hour': 0},
    1: {'attendance': 'present', 'wage': daily_emp_wage, 'working_hour': Full_DAY_HOUR},
    2: {'attendance': 'part-time', 'wage': part_time_emp_wage, 'working_hour': PART_TIME_HOUR}
}
print('Employee Wage is checks according to attendance :', employee_wage.get(attendance_check))
# variables
day_count = 0
total_employee_wage = 0

# using while loop checking the condition working days per month is greater than day
while WORKING_DAY_PER_MONTH > day_count:
    day_count += 1
    wage_of_employee = employee_wage.get(attendance_check).get('wage')
    total_employee_wage += wage_of_employee
print('Total Employee wage  per month is : {}'.format(total_employee_wage))
print('Day is : {}'.format(day_count))

