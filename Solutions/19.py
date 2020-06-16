'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import time

start = time.time()

# Use of datetime module to check if dates are Sunday
from datetime import date

sum = 0

# Function to check if first day is a Sunday
for year in range(1901, 2001): # Years in 20th century: 1901 - 2000
    for month in range(1, 13): # January to December
        day = date(year, month, 1)
        if day.weekday() == 6: # Value of Sunday is 6
        	sum += 1

print(sum)

end = time.time()

print(end - start) # Executed in 0.00200 seconds