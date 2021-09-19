# To get current date and time
# We need to use the datetime library
from datetime import datetime, timedelta

current_date = datetime.now()

# The now function returns a datetime object
print('Today is ' + str(current_date))

today = datetime.now()
print('Today is ' + str(today))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was ' + str(yesterday))

# Use date functions to control date formatting
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))

# Converting a string to a datetime object
birthday = input('When is your birthday (dd/mm/yyyy)?')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))