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

# Use of datetime module to check if dates are Sunday

from datetime import date

x = 0

for year in range(1901, 2001): # Years 1901 - 2000
    for month in range(1, 13): # January to December
        day = date(year, month, 1) # Get weekday of first day of all months and years within range
        if day.weekday() == 6: # Sunday == 6
        	x += 1

print(x)