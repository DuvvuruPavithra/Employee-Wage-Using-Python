import random

# Constants
WAGE_PER_HOUR = 20
Full_DAY_HOUR = 8

# using random to checking the attendance
attendance_check = random.randint(0, 1)
print(f'Attendance {attendance_check}')

# calculating the daily employee wage
daily_emp_wage = WAGE_PER_HOUR * Full_DAY_HOUR
print('Wage per day {}'.format(daily_emp_wage))
