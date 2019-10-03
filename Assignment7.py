# This program will open our random.txt file from Assignment 6, read the numbers generated on that file, find the total
# of those numbers, and tell how many individual numbers were on that file.
# Author: Jessica Strait, CMPSC 131 Sec 001

# First, we will tell the program to open the random.txt file. We will also tell is to read the first line of the file.

file = open(r'C:\Users\jessl\Desktop\random.txt', "r")
numbers = file.readline()

# Next, we will use two different variables to define the sum of the numbers and the quantity of numbers. We define them as zero.

total = 0
quantity = 0

# We will create a while loop to ensure that each line is read on our file. The while loop will include changing the string to
# integers, increasing the total by the new number, increasing the quantity by one, printing the new number, and defining our
# new line to be read to prevent an infinite loop.

while numbers != "":
    randomNumber = int(numbers)
    total += randomNumber
    quantity +=1
    print(randomNumber)
    numbers = file.readline()

# We must remember to close our file once our loop completes.

file.close()

# Finally, we will print the quantity of numbers in the file and the total of the numbers.

print("There are", quantity, "random numbers in this file.")
print("The sum of these numbers is", str(total)+".")
