#!/usr/bin/python
#Check if a year is leap year or not

#Note this is a basic program, your code will break if you enter a non integer
#This problem will be solved in advanced programs section
year = int(input("Enter a year: "))

#This method uses the current gregorian calendar

#A function that returns true if the year is leap else false is returned
def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if is_leap_year(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
