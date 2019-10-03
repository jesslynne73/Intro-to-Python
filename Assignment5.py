# This program will serve as a conversion table for Celsius to Fahrenheit temperatures. The user will input a
# value of temperatures to be displayed, and the program will use the conversion formula to display the table.
# Author: Jessica Strait, CMPSC 131 Sec 001

# First, our program will prompt the user to input how many temperatures should be displayed. We will assign this value
# variable n as an integer.

n = int(input("Enter the number of Celsius temperatures to be displayed."))

# Next, we will create our table headings.

print("Celsius\t    Fahrenheit")

# Finally, we will use a for loop to solve for all the requested temperature list. We will format our answers to have
# only one decimal place, and we will line up the solutions to the table headings.

for n in range(0, n+1):
    print("  ", 0+n, "\t      ", format(float(n*(9/5)+32), ".1f"))
