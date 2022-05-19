'''

@Author: Akshay palande

@Date: 2022-05-12 11:00:30

@Last Modified by: Akshay Palande

@Last Modified time: 2022-5-12 11:00:30

@Title : Basic Python programming

'''

# 5. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
print(calendar.month(year, month))

