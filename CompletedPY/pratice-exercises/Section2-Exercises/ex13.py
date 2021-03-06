"""
Write a function that, given a year and month,
prints to the console the month calendar.
The expected output format is as follows (the example is for December 2017):

Mon Tue Wed Thu Fri Sat Sun
                  1   2   3
  4   5   6   7   8   9  10
 11  12  13  14  15  16  17
 18  19  20  21  22  23  24
 25  26  27  28  29  30  31

ET: 3 hours
"""
import calendar
print(calendar.month(2017, 12))