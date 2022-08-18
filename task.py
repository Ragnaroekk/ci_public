import math

# This function takes in an integer value that represents the number of seconds 
# since the epoch: January 1st 1970. The function takes num_sec and converts it 
# to a date and returns it as a string with the following format: MM-DD-YYYY. 


def check_for_leap_year(years):
    """Returns true if years is a leap year.
    per https://www.mathsisfun.com/leap-years.html A year is a leap year if:
    1. Leap Years are any year that can be exactly divided by 4
    2. except if it can be exactly divided by 100, then it isn't
    3. except if it can be exactly divided by 400, then it is
    research from: https://cboard.cprogramming.com/c-programming/68421
    -converting-seconds-years-months-etc.html"""
    return years % 400 == 0 or (years % 4 == 0 and years % 100 != 0)


def get_current_days_of_the_month(months, years):
    """Returns the current number of days per month based on year"""
    days_of_the_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # update February to be 29 days for leap years
    if check_for_leap_year(years):
        days_of_the_month[2] = 29

    return days_of_the_month[months]


def my_datetime(num_sec):
    """This function takes in an integer value that represents the number of
    seconds since the epoch: January 1st 1970. The function takes num_sec and
    converts it to a date and returns it as a string with the following
    format: MM-DD-YYYY. Research from:
    https://docs.python.org/3/library/datetime.html,
    https://stackoverflow.com/questions/46269991/
    how-do-i-use-to-convert-seconds-to-minutes-and-seconds-in-python
    https://stackoverflow.com/questions/4048651/python-function-to-convert-
    seconds-into-minutes-hours-and-days/4048773
    https://grass.osgeo.org/grass79/manuals/libpython/_modules/temporal/
    datetime_math.html
    """
    seconds_in_a_day = 86400
    first_day_of_the_month = 1
    first_month_of_the_year = 1
    current_day = 1
    current_month = 1
    months_in_a_year = 12
    # Epoch time starts at 01-01-1970
    current_year = 1970

    total_days = math.floor(num_sec / seconds_in_a_day)

    while total_days > 0:
        current_day += 1
        # reset the day to 1 each time you roll over to the next month
        if current_day > get_current_days_of_the_month(current_month,
                                                       current_year):
            current_day = first_day_of_the_month
            current_month += 1
            # reset the month to 1 each time you roll over to the next year
            if current_month > months_in_a_year:
                current_month = first_month_of_the_year
                current_year += 1
        total_days -= 1

    return f"{current_month:02d}-{current_day:02d}-{current_year}"