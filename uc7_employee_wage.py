import random

import random

# Constants
WAGE_PER_HOUR = 20
Full_DAY_HOUR = 8
PART_TIME_HOUR = 6
WORKING_DAY_PER_MONTH = 20
TOTAL_WORKING_HRS = 100


def employee_wage():
    # variables
    total_working_hour = 0
    total_wage = 0
    total_working_day = 0
    total_employee_wage = 0

    # using while loop checking the condition working days per month is greater than total working day
    while total_working_day <= WORKING_DAY_PER_MONTH and total_working_hour < 100:
        attendance_check = random.randint(0, 2)
        print(f'Attendance {attendance_check}')

        if attendance_check == 2:
            print('Employee is full time')
            wage_per_day = WAGE_PER_HOUR * Full_DAY_HOUR
            total_wage = total_wage + wage_per_day
            total_working_hour += Full_DAY_HOUR
            total_working_day += 1

        elif attendance_check == 1:
            print('Employee is part time')
            wage_per_day = WAGE_PER_HOUR * PART_TIME_HOUR
            total_wage = total_wage + wage_per_day
            total_working_hour += PART_TIME_HOUR
            total_working_day += 1

        else:
            print('Employee is Absent')
            wage_per_day = 0
            total_wage = total_wage + wage_per_day

        print('Total working hour : {}'.format(total_working_hour))
        print("Total working day : ", total_working_day)
        print("Monthly Employee wage : ", total_wage)


employee_wage()
