# Author: Jessica Strait
# This project can determine if a year is a leap year or not using the modulus operator.

def is_leap(year):
    # Initialize variables to false.
    leap = False
    divide_4 = False
    divide_100 = False
    # Check that the input is an integer.
    if type(year) != int:
        return 'TypeError'
    # If a year is divisible by four, it is a leap year, unless it is divisible by 100.
    # The modulus checks if there is a remainder when dividing two integers.
    if year % 4 == 0:
        divide_4 = True
        leap = True
    # If a year is divisible by 100, it is not a leap year, unless it is divisible by 400.
    if year % 100 == 0 and divide_4:
        divide_100 = True
        leap = False
    if divide_100 and divide_4 and year % 400 == 0:
        leap = True
    return leap

year = int(input())
