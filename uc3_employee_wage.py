import random

# Constants
WAGE_PER_HOUR = 20
Full_DAY_HOUR = 8
PART_TIME_HOUR = 6

# using random to checking the attendance
attendance_check = random.randint(0, 1)
print(f'Attendance {attendance_check}')

# calculating the daily employee wage
daily_emp_wage = WAGE_PER_HOUR * Full_DAY_HOUR
print('Wage per day is : {}'.format(daily_emp_wage))

# calculating the part-time employee wage
part_time_emp_wage = WAGE_PER_HOUR * PART_TIME_HOUR
print('Part Time Wage per day is : {}'.format(part_time_emp_wage))


