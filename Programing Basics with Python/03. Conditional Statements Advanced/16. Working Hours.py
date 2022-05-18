hours = int(input())
day_of_week = input()
is_working_day = day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or\
                 day_of_week == 'Thursday' or day_of_week == 'Friday' or day_of_week == 'Saturday'
is_working_hour = 10 <= hours <= 18
if is_working_day and is_working_hour:
    print('open')
else:
    print('closed')
